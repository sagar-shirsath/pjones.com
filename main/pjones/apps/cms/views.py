from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response("cms/index.html", context_instance=RequestContext(request))

def about(request):
    return render_to_response("cms/about.html", context_instance=RequestContext(request))

def manager(request):
    return render_to_response("cms/manager.html", context_instance=RequestContext(request))

def careers(request):
    return render_to_response("cms/careers.html", context_instance=RequestContext(request))

def director(request):
    return render_to_response("cms/director.html", context_instance=RequestContext(request))

def company(request):
    return render_to_response("cms/company.html", context_instance=RequestContext(request))

def projects(request):
    return render_to_response("cms/projects.html", context_instance=RequestContext(request))

def help(request):
    return render_to_response("cms/help.html", context_instance=RequestContext(request))

def services(request):
    return render_to_response("cms/services.html", context_instance=RequestContext(request))

def contact(request):
    return render_to_response("cms/contact.html", context_instance=RequestContext(request))
