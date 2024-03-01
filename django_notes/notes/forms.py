from .models import Notes
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note title',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'YYYY-MM-DD',
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Note text',
            })
        }

