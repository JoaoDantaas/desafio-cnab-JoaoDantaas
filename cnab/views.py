from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cnab
from django.db import models

def list(request):
    get = Cnab.objects.all()
    total = Cnab.objects.aggregate(models.Sum('value'))
    return render(request, 'list.html', {'operations': get, 'total': total})
    ...

def upload_file(request):
    if request.method == 'POST':
        with open("CNAB.txt", "wb") as file:
            for chunk in request.FILES["file"].chunks():
                file.write(chunk)
        path = "CNAB.txt"
        with open(path, "r", encoding="utf-8") as cnab_read:
            list = []
            for line in cnab_read.read().split("\n"):
                list.append(line)
        for li in list:
            type = li[0]
            date = li[1:9]
            value = li[9:19]
            cpf = li[19:30]
            card = li[30:42]
            hour = li[42:48]
            store_owner = li[48:62]
            store_name = li[62:]

            Cnab.objects.create(
                type = type,
                date = date,
                value = value,
                cpf = cpf,
                card = card,
                hour = hour,
                store_owner = store_owner,
                store_name = store_name
        )
        return HttpResponseRedirect('list/')
    else:
        return render(request, 'upload_cnab.html')