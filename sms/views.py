from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import datetime
import urllib2
import urllib
import json
import re

def lookup():
    url = 'http://api.statsfc.com/premier-league/top-scorers.json?key=free'

    req_response = urllib.urlopen(url)
    req_results = req_response.read()

    results = json.loads(req_results)

    msg = ''
    for i in range(5):
        elt = results[i]
        msg = msg + str(results.index(elt)+1) + '. ' + elt['player'] +'(' + elt['team'] + ') '+ str(elt['goals']) +'\n'


    return msg



@csrf_exempt
def receive(request):
    # POST means we should process things
    if request.method == 'POST':
        msg = lookup()
        return HttpResponse(msg)

    else:
        return render_to_response('sms/receive.html',
                                  dict(),
                                  context_instance=RequestContext(request))
