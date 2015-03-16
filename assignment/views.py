from django.shortcuts import render
from assignment import models
#from assignment.models import Entry
from django.utils import feedgenerator
from django.shortcuts import render_to_response, RequestContext
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext


def index(request):
	return render_to_response('index.html',
	{}, context_instance=RequestContext(request))


def zadatak(request):
	return render_to_response('zadatak.html',
	{}, context_instance=RequestContext(request))

	
def url2(request):
	return render_to_response('url2.py',
	{}, context_instance=RequestContext(request))
	
def url3(request):
	return render_to_response('url3.py',
	{}, context_instance=RequestContext(request))


