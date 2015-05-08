from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # construct a dict to pass to the template engine as its context
    # note the key 'boldmessage' is the same
    context_dict = {'boldmessage': "I am bold font form the context"}

    # return a rendered response to send to the client
    # the first param is the template we wish to use
    return render(request, 'rango/index.html', context_dict)
# Create your views here.
