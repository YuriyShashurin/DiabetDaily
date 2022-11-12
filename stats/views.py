from django.http import HttpResponse
from django.shortcuts import render
from .models import UserProfile, Indication
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def login(request):
    pass


def logout(request):
    pass


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



