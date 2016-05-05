import pytest
import pytest_django
import pytest_selenium
from codeschool.testing import use_db
from cs_questions.tests.test_logic import question as question_io


@pytest.fixture(scope='session')
def base_url(live_server):
    return live_server.url


@pytest.mark.django_db
def test_io_questions_detail(base_url, selenium, question_io):
    pk = question_io.pk
    selenium.get('%s/questions/%s/' % (base_url, pk))
    L = selenium.find_elements_by_css_selector('ace-editor')
    assert len(L) == 1