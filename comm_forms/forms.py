from django import forms
from .models import Comm_Form
from news.models import Post

class Comm_Form_Forms(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Post.objects.all())
    class Meta:
        model = Comm_Form
        fields = ['book', 'name']