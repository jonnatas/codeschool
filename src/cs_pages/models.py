import copy
from codeschool import models
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
from codeschool.models import User



class LanguageChooserBlock(blocks.ChooserBlock):
    target_model = ProgrammingLanguage
    widget = forms.Select

    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        else:
            return value


class CodeBlock(blocks.StructBlock):
    """
    Code Highlighting Block
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
    """interative code blocks """
    
    block_id = blocks.CharBlock(max_length=50)

    def render(self, value):
        lang = value['language'].ref
        code = escape(value['code'])
        id_value = value['block_id']
        data = '<ace-editor mode="%s" id="input-code-%s">%s</ace-editor>' % (lang, id_value, code)
        return mark_safe(data)

class userInputBlock(CodeBlock):
    """interative code blocks """

    expected_result = blocks.TextBlock()
    
    def render(self, value):
        lang = 'python'
        code = escape(value['code'])
        data = '<h3>Try This</h3> <form><ace-editor id="yourcode" mode="python">%s</ace-editor><br /> <button type="button" onclick="runit()">Run</button> </form> <pre id="output" ></pre> <!-- If you want turtle graphics include a canvas --><div id="mycanvas"></div> ' % (code)
        return mark_safe(data)            


class TutorialPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock()),
        ('interactive_code', InputCodeBlock()),
        ('skulpt_python_code', userInputBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    template = 'cs_pages/tutorial_page.jinja2'

    def get_progress_for_user(self, user):
        """dsfsdfsd"""

        return TutorialProgress.for_user(user, self)

    def get_proxy_for_user(self, user):
        progress = self.get_progress_for_user(user)
        return TutorialPageProxy(self, progess)

    def get_context(self, request):
        progress = self.get_progress_for_user(request.user)
        context = super().get_context(request)
        context.update({
            'progress': progress, 
            'body': progress.get_updated_body()
        })
        return context

class TutorialPageProxy:
    def __init__(self, tutorial, progress):
        self.tutorial = tutorial
        self.progess = progress
        self.body = copy.deepcopy(tutorial.body)

    def __getattr__(self, attr):
        return getattr(self.tutorial, attr)



class TutorialProgress(models.Model):
    user = models.ForeignKey(User)
    tutorial = models.ForeignKey(TutorialPage)

    @classmethod
    def for_user(cls, user, tutorial):
        """fdgdfgdfgd"""

        try:
            return cls.objects.get(user=user, tutorial=tutorial)
        except cls.DoesNotExist:
            return cls.objects.create(user=user, tutorial=tutorial)

    def get_updated_body(self):
        body = TutorialPage.objects.get(pk=self.tutorial.pk).body

        return body


class InputBlockProgress(models.Model):
    progress = models.ForeignKey(TutorialProgress)
    body = progress.get_updated_body()

    refs = []

    for block in body:
        if isinstance(block.block, InputCodeBlock):
            ref_dict = {
                "language" : block.block.child_blocks["language"] ,
                "id" : block.block.child_blocks["block_id"]
            }

            refs.append[ref_dict]

    def get_input_code_source_from_id(self, id_code):
        pass


