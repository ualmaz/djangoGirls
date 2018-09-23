from django.shortcuts import render
from django.utils import timezone
from .models import Record

def post_list(request):
    records = Record.objects.all()
    return render(request, 'blog/post_list.html', {'records': records})