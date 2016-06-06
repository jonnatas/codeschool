from django.shortcuts import render
from cs_challenge_list import models
from codeschool.shortcuts import render_context, get_object_or_404, redirect

def index(request):
    challenge_lists = dict()
    challenge_lists['challenge_lists'] = models.ChallengeList.objects.all() # TODO: change this to get the challenge lists of the user
    return render(
            request,
            'cs_challenge_list/challenge-index.jinja2',
            challenge_lists)

def challenge_list_detail(request, pk):
    challenge_list = get_object_or_404(models.ChallengeList, pk=pk)
    questions = challenge_list.questions.all()

    return render_context(
            request,
            'cs_challenge_list/challenge-list-detail.jinja2',
            challenge_list=challenge_list,
            questions=questions)

def rank(request):
    return render(
            request,
            'cs_challenge_list/challenge-rank.jinja2')
