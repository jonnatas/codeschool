from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock

from pygments import highlight
from pygments.formatters import get_formatter_by_name
from pygments.lexers import get_lexer_by_name


from django.utils.safestring import mark_safe
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

    language = blocks.ChoiceBlock(choices=LANGUAGE_CHOICES)
    code = blocks.TextBlock()

    class Meta:
        icon = 'code'

    def render(self, value):
        src = value['code'].strip('\n')
        lang = value['language']

        lexer = get_lexer_by_name(lang)
        formatter = get_formatter_by_name(
            'html',
            linenos=None,
            cssclass='codehilite',
            style='default',
            noclasses=False,
        )
        return mark_safe(highlight(src, lexer, formatter))

class HomePage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    template = 'cs_pages/home_page.jinja2'
