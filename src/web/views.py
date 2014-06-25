from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect


def index(request):
    ctx = {}
    return render_to_response('web/index.html', ctx, context_instance=RequestContext(request))
