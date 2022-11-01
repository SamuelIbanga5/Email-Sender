from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField, RichTextFormField
from .models import Message

class ContactForm(forms.ModelForm):
    subject = forms.CharField(label="Subject", max_length=100)
    email = forms.EmailField(max_length=50, label='email')
    message = forms.CharField(widget=CKEditorWidget)

    class Meta:
        model = Message
        fields = ('message', )
