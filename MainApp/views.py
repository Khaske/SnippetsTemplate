from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, redirect
from MainApp.models import Snippet


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': Snippet.objects.all(),
        'count': Snippet.objects.count(),
    }
    return render(request, 'pages/view_snippets.html', context)

def snippet_detail(request, snippet_id: int):
    try:
        context = {
            'snippet': Snippet.objects.get(pk=snippet_id),
        }
        return render(request, 'pages/page_snippet.html', context)
    except:
        return HttpResponseNotFound('Сниппет не найден!')