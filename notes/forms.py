from django import forms
from .choices import STATUS_CHOICES
from .models import Note

class NoteAddForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title'}),max_length=64, required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Description'}),max_length=256, required=True)
    status = forms.ChoiceField(choices = STATUS_CHOICES, widget=forms.Select(attrs={'class' : 'custom-select', 'placeholder': 'Choose status'}), required=True)

    class Meta:
        model = Note
        fields = ('status', 'title', 'description')

class NoteEditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Title'}),max_length=64, required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Description'}),max_length=256, required=True)
    status = forms.ChoiceField(choices = STATUS_CHOICES, widget=forms.Select(attrs={'class' : 'custom-select', 'placeholder': 'Choose status'}), required=True)

    class Meta:
        model = Note
        fields = ('status', 'title', 'description')
