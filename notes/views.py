from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from .models import Note
from .forms import NoteEditForm, NoteAddForm

def home(request):
    context = {}
    if not request.user.is_anonymous:
        context['notes_to_do'] = Note.objects.filter(author=request.user, status='0')
        context['notes_in_progress'] = Note.objects.filter(author=request.user, status='1')
        context['notes_done'] = Note.objects.filter(author=request.user, status='2')

    return render(request,'home.html', context)

@login_required
def note_page(request, username, note_id):
    note = get_object_or_404(Note, id=note_id)
    context = {'note':note}

    return render(request,'note_page.html',context)

@login_required
def note_edit(request, username, note_id):
    note = get_object_or_404(Note, id=note_id)
    form = NoteEditForm(model_to_dict(note))
    context = {'form':form, 'note':note}
    if request.method == 'POST':
        form = NoteEditForm(request.POST)
        note.title= request.POST['title']
        note.description=request.POST['description']
        note.status=request.POST['status']
        note.save()
        return redirect(note)
    return render(request,'note_edit_page.html',context)

@login_required
def note_add(request):
    form = NoteAddForm()
    context = {'form':form}
    if request.method == 'POST':
        form = NoteAddForm(request.POST)
        new_note = Note(status=request.POST['status'],\
                        title= request.POST['title'],\
                        description=request.POST['description'],\
                        author=request.user)
        new_note.save()
        return redirect(new_note.get_absolute_url())
    return render(request,'note_add_page.html',context)
