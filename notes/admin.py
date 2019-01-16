from django.contrib import admin
from .models import Note

@admin.register(Note)
class MediaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Note._meta.fields]
    list_display_links = ['title', 'description', 'id']

    class Meta:
        model = Note
