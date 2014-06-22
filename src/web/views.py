from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect


def index(request):
    ctx = {}
    if user.is_authenticated():
        return HttpResponseRedirect('/admin/')
    else:
        return render_to_response('web/index.html', ctx, context_instance=RequestContext(request))
