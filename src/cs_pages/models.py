from django.db import models
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
    
    def render(self, value):
        lang = value['language'].ref
        code = escape(value['code'])
        data = '<ace-editor mode="%s">%s</ace-editor>' % (lang, code)
        return mark_safe(data)

class userInputBlock(CodeBlock):
    """interative code blocks """
    
    def render(self, value):
        lang = 'python'
        code = escape(value['code'])
        data = '<script type="text/javascript"> function outf(text) { var mypre = document.getElementById("output"); mypre.innerHTML = mypre.innerHTML + text; } function builtinRead(x) { if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined) throw "File not found: '" + x + "'"; return Sk.builtinFiles["files"][x];}function runit() { var prog = document.getElementById("yourcode").value; var mypre = document.getElementById("output"); mypre.innerHTML = ''; Sk.pre = "output"; Sk.configure({output:outf, read:builtinRead}); (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = \'mycanvas\'; var myPromise = Sk.misceval.asyncToPromise(function() { return Sk.importMainWithBody("<stdin>", false, prog, true); }); myPromise.then(function(mod) { console.log(\'success\'); }, function(err) { console.log(err.toString()); });} </script> <h3>Try This</h3> <form> <textarea id="yourcode" cols="40" rows="10">import turtlet = turtle.Turtle()t.forward(100)print "Hello World" </textarea><br /> <button type="button" onclick="runit()">Run</button> </form> <pre id="output" ></pre> <div id="mycanvas"></div> '
        return mark_safe(data)            


class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock()),
        ('interactive_code', InputCodeBlock()),
        ('user_input', userInputBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    template = 'cs_pages/home_page.jinja2'
