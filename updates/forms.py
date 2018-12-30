from .models import Update
from django import forms


class UpdateForm(forms.ModelForm):

    class Meta:
        model = Update
        fields = '__all__'
