from django.shortcuts import render
from .models import Accounts


def home(request):
    data = Accounts.objects.all()[:3]
    print("****", data)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести', 'info': data})