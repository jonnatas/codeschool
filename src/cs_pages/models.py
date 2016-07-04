from django.db import models
import copy
from codeschool import models
import django.middleware.csrf
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django import forms

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name

from cs_core.models import ProgrammingLanguage
from codeschool.utils import lazy, delegate_to
from codeschool.models import User


class LanguageChooserBlock(blocks.ChooserBlock):
    """ 
    Block that let user choose a language
    """

    target_model = ProgrammingLanguage
    widget = forms.Select

    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block (pygments)
    """
    LANGUAGE_CHOICES = (
        ('python', 'Python'),
        ('bash', 'Bash/Shell'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('scss', 'SCSS'),
    )

    language = LanguageChooserBlock()
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language'].ref

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='default',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))


class InputCodeBlock(CodeBlock):
    """
    interative code blocks 
    """
    
    block_id = blocks.CharBlock(max_length=50)

    def render(self, value):
        lang = value['language'].ref
        code = escape(value['code'])
        id_value = value['block_id']
        html_id = "input-code-%s" % id_value
        data = (       '''<ace-editor mode="%s" id="input-code-%s">%s</ace-editor>
            <button onclick="srvice('/tutorial/send-input-block', {id: %r, source: $('#%s')[0].getValue()})">
            Send</button>'''
        ) % (lang, id_value, code, id_value, html_id)
        return mark_safe(data)


class SkulptPythonBlock(CodeBlock):
    """
    interative code blocks
    """

    def render(self, value):
        lang = 'python'
        code = escape(value['code'])
        data = '<h3>Try This</h3> <form><ace-editor id="yourcode" mode="python">%s</ace-editor><br /> <button type="button" onclick="runit()">Run</button> </form> <pre id="output" ></pre> <!-- If you want turtle graphics include a canvas --><div id="mycanvas"></div> ' % (code)
        return mark_safe(data)


class TutorialPage(Page):
    """
    wagtail tutorial page
    """

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('print_code', CodeBlock()),
        ('interactive_code', InputCodeBlock()),
        ('skulpt_python_code', SkulptPythonBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
    
    template = 'cs_pages/tutorial_page.jinja2'

    def get_progress_for_user(self, user):
        """
        get all tutorial progress made by user
        """

        return TutorialProgress.for_user(user, self)

    def get_proxy_for_user(self, user):
        """
        get a tutorial page proxy for the current user
        """

        progress = self.get_progress_for_user(user)
        return TutorialPageProxy(self, progess)

    def get_context(self, request):
        progress = self.get_progress_for_user(request.user)
        context = super().get_context(request)
        context.update({
            'progress': progress, 
            'body': progress.get_updated_body(),
            'blocks': progress.get_updated_blocks()
        })
        return context     


class TutorialPageProxy:
    """
    create a proxy of tutorial page
    """

    def __init__(self, tutorial, progress):
        self.tutorial = tutorial
        self.progess = progress
        self.body = copy.deepcopy(tutorial.body)

    def __getattr__(self, attr):
        return getattr(self.tutorial, attr)


class TutorialProgress(models.Model):
    """
    tutorial progress user
    """

    user = models.ForeignKey(User)
    tutorial = models.ForeignKey(TutorialPage)

    @classmethod
    def for_user(cls, user, tutorial):
        """
        get the TutorialProgress for the current user if exists
        if not, create a new tutorial
        """

        try:
            return cls.objects.get(user=user, tutorial=tutorial)
        except cls.DoesNotExist:
            return cls.objects.create(user=user, tutorial=tutorial)

    def get_updated_body(self):
        """
        get the page body updated for user
        """

        body = TutorialPage.objects.get(pk=self.tutorial.pk).body

        return body

    def get_updated_blocks(self):
        """
        get all InputCodeBlocks updated for user
        """

        body = self.get_updated_body()

        refs = []

        for block in body:
            if isinstance(block.block, InputCodeBlock):
                ref_dict = {
                    "language" : block.value["language"] ,
                    "block_id" : block.value["block_id"]
                }

                self.get_block_for_tutorial(ref_dict["block_id"])

                refs.append(ref_dict)

        return refs

    def get_block_for_tutorial(self, block_id):
        """
        get all block progress for tutorial
        """

        return InputBlockProgress.for_tutorial(self, block_id)



class InputBlockProgress(models.Model):
    """
    progress of InputBlock for current user
    """

    progress = models.ForeignKey(TutorialProgress)
    block_id = models.CharField(max_length=50)
    user = delegate_to('progress')
    tutorial = delegate_to('progress')
    body = delegate_to('tutorial')

    @property
    def block(self):
        return self.block
    
    @property
    def value(self):
        return self.value

    @property
    def language(self):
        return self.language

    @classmethod
    def for_tutorial(cls, progress, block_id):
        """
        get the block progress for the tutorial
        """

        try:
            return cls.objects.get(progress=progress, block_id=block_id)
        except cls.DoesNotExist:
            return cls.objects.create(progress=progress, block_id=block_id)


    def get_input_code_source_from_id(self, id_code):
        pass

