from django.shortcuts import render
from cs_challenge_list import models
from codeschool.shortcuts import render_context, get_object_or_404, redirect

def index(request):
    challenge_lists = dict()
    challenge_lists['challenge_lists'] = models.ChallengeList.filter_by_user(request)
    return render(
            request,
            'cs_challenge_list/challenge-index.jinja2',
            challenge_lists)

def new(request):
    return render_context(
             request,
             'cs_challenge_list/new.jinja2')

def rank(request):
    return render(
            request,
            'cs_challenge_list/challenge-rank.jinja2')

def challenge_list_detail(request, pk):
    challenge_list = get_object_or_404(models.ChallengeList, pk=pk)
    questions = challenge_list.questions.all()

    return render_context(
            request,
            'cs_challenge_list/challenge-list-detail.jinja2',
            challenge_list=challenge_list,
            questions=questions)

def challenge_question(request,list_pk,question_pk):
    challenge_list = get_object_or_404(models.ChallengeList, pk=list_pk)
    question = get_object_or_404(models.ChallengeQuestion, pk=question_pk)

    return render_context(
             request,
             'cs_challenge_list/question-detail.jinja2',
             challenge_list=challenge_list,
             question=question)
