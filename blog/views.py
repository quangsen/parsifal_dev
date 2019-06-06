from django.shortcuts import render, get_object_or_404
from .models import Entry


def entries(request):
    entries = Entry.objects.filter(status=Entry.PUBLISHED)
    context = {
        'entries': entries
    }
    return render(request, 'blog/entries.html', context)


def entry(request, slug):
    blog_entry = get_object_or_404(Entry, slug=slug, status=Entry.PUBLISHED)
    context = {
        'entry': blog_entry
    }
    return render(request, 'blog/entry.html', context)
