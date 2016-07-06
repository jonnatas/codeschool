from wagtail.tests.utils import WagtailPageTests
from .models import TutorialPage
from cs_core.models import Faculty

class TutorialPageTests(WagtailPageTests):

	def test_test_can_create_tutorial_page(self):
		self.assertCanNotCreateAt(TutorialPage, Faculty)


	def test_can_create_tutorial_inside_tutorial(self):
		self.assertCanCreateAt(TutorialPage, TutorialPage)
