from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from . import forms

# Create your views here.

def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'notes.html', {'notes': notes})

def CreateNote(request):
    if request.method == 'POST':
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:notes_list')
    else:
        form = forms.NoteForm()
    return render(request, 'create_note.html', {'form': form})

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = forms.NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('dashboard:notes_list')
    else:
        form = forms.NoteForm(instance=note)
    return render(request, 'note.html', {'form': form, 'note': note})

def toggle_status(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.status = not note.status
    note.save()
    return redirect('dashboard:notes_list')

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('dashboard:notes_list')