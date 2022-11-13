from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile, Indication
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'auth/login.html', {'form': form})


def logout(request):
    logout(request)


@csrf_exempt
def add_sugar_data(request):
    if request.method == 'POST':
        try:
            telegram_id = request.POST['user']
            user = UserProfile.objects.get(telegram_id=telegram_id)
            data = request.POST['data']
            new_item = Indication.objects.create(user=user, data=data)
            return HttpResponse(data)
        except Exception as e:
            return HttpResponse(e)
