from django.contrib import auth
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from sign.models import Event

# Create your views here.
def index_page(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if username == '' or password == '':
            return render(request, 'index.html', {'error': 'username/password is empty.'})
        if user is not None:
            auth.login(request, user)
            response = HttpResponseRedirect('/main/')
            request.session['user'] = username
            return response
        else:
            return render(request, 'index.html', {'error': 'username/password is invalid.'})
    else:
        return HttpResponseRedirect('/')

@login_required
def main_page(request):
    username = request.session.get('user', '')
    event_list = Event.objects.all()
    return render(request, 'main.html', {'user': username,
                                         'events': event_list})