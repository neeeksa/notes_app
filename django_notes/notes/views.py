from django.shortcuts import render,redirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    data = {
        'title': 'Home page',
    }
    return render(request, 'notes/index.html', data)


def all_notes(request):
    notes = Notes.objects.all()
    return render(request, 'notes/all_notes.html', {'notes': notes})


def create(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_notes')  # Перенаправление на страницу всех заметок после создания
    else:
        form = NotesForm()
    return render(request, 'notes/create.html', {'form': form})


class NotesDetailView(DetailView):
    model = Notes
    template_name = 'notes/notes-view.html'
    context_object_name = 'notes'


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    template_name = 'notes/create.html'  # Использование того же шаблона, что и для создания
    success_url = reverse_lazy('all_notes')


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = reverse_lazy('all_notes')
    template_name = 'notes/notes-delete.html'










