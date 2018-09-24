from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Record

def post_list(request):
    records = Record.objects.all()
    return render(request, 'blog/post_list.html', {'records': records})

def post_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, 'blog/post_detail.html', {'record': record})