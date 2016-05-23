from codeschool import models
from django import forms
from django.db import models
from cs_questions.models import Question
from cs_core.models import ProgrammingLanguage

class ChallengeQuestion(models.Model):
    """ Describes the extention of a class Question """
    # TODO: this should be inherence from Question
    name = models.CharField("question name",
            max_length=50,
            blank=False,
            null=True)
    time_limit = models.IntegerField("time limit compilation",
            blank=False,
            null=True)
    problem = models.TextField("problem description",
            blank=False,
            null=True)
    problem_input = models.CharField("problem input data",
            max_length=140,
            blank=False,
            null=True)
    problem_output = models.CharField("problem output data",
            max_length=140,
            blank=False,
            null=True)
    example = models.TextField("sample for the problem",
            blank=True,
            null=True)

    languages = ProgrammingLanguage.objects.all()
    supported_language = models.ForeignKey(
            ProgrammingLanguage,
            null=True)

    def __str__(self):
        return self.name

class ChallengeList(models.Model):
    """ Describes the challenge list created by the user """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    challenge_question = models.ManyToManyField(ChallengeQuestion)

    def __str__(self):
        return self.name

class ChallengeListRank(models.Model):
    """ Describes the Rank of the List """
    challenge_list = models.ForeignKey(
            ChallengeList,
            on_delete=models.CASCADE,
            null=True)

