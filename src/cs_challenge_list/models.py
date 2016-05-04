from codeschool import models
from django.db import models
from cs_questions.models import Question

class ChallengeQuestion(models.Model):
    """ Describes the extention of a class Question """
    

class ChallengeList(models.Model):
    """ Describes the challenge list created by the user """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    challenge_question = models.ForeignKey(
        ChallengeQuestion,
        on_delete=models.CASCADE)

class ChallengeListRank(models.Model):
    """ Describes the Rank of the List """
    challenge_list = models.ForeignKey(
        ChallengeList,
        on_delete=models.CASCADE)
