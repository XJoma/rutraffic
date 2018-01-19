from django.contrib import auth
from django.shortcuts import render

from fee.models import Fee


def fee(request):
    fee = Fee.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['fees'] = fee
    context['username'] = user
    return render(request, 'fee.html', context)
