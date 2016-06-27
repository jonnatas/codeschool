from django.shortcuts import render

def index(request):
	context = {
		'x': 2,
		'y': 3,
	}

	return render(request, 'cs_content/index.jinja2', context)
# Create your views here.
