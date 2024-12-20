from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from MainApp.forms import SnippetForm
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # создаём пустую форму при запросе методом GET
    if request.method == 'GET':
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': SnippetForm()
            }
        return render(request, 'pages/snippet_add.html', context)
    # получаем данные из формы и на их основе создём новый сниппет в БД
    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets-list")
        return render(request, "pages/snippet_add.html", {'form':form})



def snippets_page(request):
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': Snippet.objects.all(),
        'count': Snippet.objects.count(),
        }
    return render(request, 'pages/snippets_list.html', context)

def snippet_detail(request, snippet_id: int):
    try:
        snippet = Snippet.objects.get(pk=snippet_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet c id = {snippet_id} не найден!')
    else:
        context = {
            'pagename': 'Просмотр сниппета',
            'snippet': snippet,
        }
        return render(request, 'pages/snippet_detail.html', context)
    
def snippet_edit(request, snippet_id: int):
    pass
    
def snippet_delete(request, snippet_id: int):
    if request.method == "POST":
        snippet = get_object_or_404(Snippet, id=snippet_id)
        snippet.delete()
    return redirect("snippets-list")