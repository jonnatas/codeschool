from django.shortcuts import render

def index(request):
    return render(
            request,
            'cs_challenge_list/challenge-index.jinja2')
