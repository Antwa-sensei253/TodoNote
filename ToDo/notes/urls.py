from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name='notes_list'),
    path('create/', views.CreateNote, name='create_note'),
    path('edit/<int:note_id>/', views.edit_note, name='edit_note'),
    path('delete/<int:note_id>/', views.delete_note, name='delete_note'),
]