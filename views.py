from django.shortcuts import render
import sys
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail



def home(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		message=request.POST['message']
		send_mail('New Query', message, email,
    	['test@gmail.com'], fail_silently=False)
		return HttpResponse('OK')

	else:
		ctx = RequestContext(request, {})   
		return render_to_response('index.html', 
                              {
                              }, context_instance=ctx)




