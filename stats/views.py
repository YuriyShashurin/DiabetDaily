from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from .models import UserProfile, Indication
from django.views.decorators.csrf import csrf_exempt
from .forms import LoginForm, SignupForm


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


class RegisterView(TemplateView):
    template_name = 'auth/register.html'
    error = 'Gfg'
    form = SignupForm()

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = self.form
        context['error'] = self.error
        return self.render_to_response(context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['check_password']:
                new_user = UserProfile.objects.create(
                    username=cd['username'],
                    password=cd['password'],
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    email=cd['email'],

                )
                new_user.save()
                print(new_user)
                user = authenticate(username=cd['username'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        self.error = ''
                        return redirect('/')
                    else:
                        self.error = 'Аккаунт заблокирован'
                        return redirect('/signup')
            else:
                print('не совпадают')
                self.error = 'Пароли не совпадают'
        else:
            self.error = 'Введены неверные данные'


@login_required
def add_sugar_data(request):
    if request.method == 'POST':
        try:
            telegram_id = request.POST['user']
            user = UserProfile.objects.get(telegram_id=telegram_id)
            data = request.POST['data']
            new_item = Indication.objects.create(user=user, data=data)
            new_item.save()
            return redirect('/')
        except Exception as e:
            return HttpResponse(e)
