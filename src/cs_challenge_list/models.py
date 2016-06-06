from codeschool import models
from django import forms
from cs_questions.models import CodingIoQuestion
from cs_core.models import ProgrammingLanguage

class ChallengeList(models.Model):
    """ Describes the challenge list created by the user """
    name = models.CharField(max_length=50)
    long_description = models.TextField(blank=True)
    short_description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class ChallengeQuestion(CodingIoQuestion, models.ListItemModel):
    """ Describes the extention of a class Question """
    class Meta:
        root_field = "challenge_list"

    challenge_list = models.ForeignKey(
            ChallengeList,
            related_name="questions")

    def __str__(self):
        return self.name

ChallengeList.itens = models.ListItemSequence.as_items(ChallengeQuestion)

