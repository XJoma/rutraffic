from django.contrib import auth
from django.shortcuts import render

from company.models import Company


def company(request):
    company = Company.objects.all().order_by('-id')
    user = auth.get_user(request).username
    context = {}
    context['companys'] = company
    context['username'] = user
    return render(request, 'company.html', context)
