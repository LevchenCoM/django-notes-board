from django.urls import path
from notes import views

urlpatterns = [
    path('<username>/<int:note_id>/', views.note_page, name='note_page'),
    path('<username>/<int:note_id>/edit/', views.note_edit, name='note_edit'),
    path('add/', views.note_add, name='note_add'),
]
