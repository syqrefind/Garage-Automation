from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
=======
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("This is the manager's page.")
>>>>>>> Yunqi
