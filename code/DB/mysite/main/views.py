from django.shortcuts import render, redirect
# from .models import Accounts
from .models import *
from .forms import *


def home(request):
    #data = Accounts.objects.filter(login__exact='GorNa_03_08_1988')

    data = get_hunters_by_id_sct(10)
    return render(request, 'main\static\index.html', {'title': 'Пробуем вывести', 'info': data})


    '''
    proc_add_voucher(10, 21, 0, 26703800, 1)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''
    proc_delete_voucher(1208)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''
    proc_mark_point_pricelist_irrelevant('чирок', 89)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''
    proc_add_point_pricelist('чирок', 870, 89)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''if request.method == 'POST':
        error = ''
        form = UserForm(request.POST)
        print(form)

        if form.is_valid():
            #form.save()
            return redirect('index')
        else:
            error = 'Неверные данные'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main\index.html', context)'''







