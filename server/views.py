from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Authentication
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from server.models import *

def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

@login_required(login_url='/users/login/')
def chef(request):
	print request.user.id
	try:
		restaurant= Restaurant.objects.get(user=request.user.id)
		tables=Table.objects.all().filter(restaurant=restaurant)
		order = Order.objects.filter(state=1,table__in=tables)
		return render_to_response('chef.html',{'orders':order},context_instance=RequestContext(request))
	except Restaurant.DoesNotExist:
		return render_to_response('error_user.html',context_instance=RequestContext(request))

#Autenticacion de usuarios
def login_user(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		if form.is_valid:
			username = request.POST['username']
			passwd = request.POST['password']
			access = authenticate(username=username, password=passwd)
			if access is not None:
				login(request, access)
				if 'next' in request.GET:
					next = request.GET['next']
				else:
					next='/'
				if next is not None:
					return HttpResponseRedirect(next)
				else:
					return index(request)
			else:
				return login_form(request,True)
	else:
		return login_form(request,False)

def login_form(request,isFirst):
	form = AuthenticationForm()
	return render_to_response('login.html',{'form':form,'message':isFirst},context_instance=RequestContext(request))

@login_required(login_url='/users/login/')
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')