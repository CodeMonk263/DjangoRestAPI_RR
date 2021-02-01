from django import forms

from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = [
            'userId',
            'id',
            'title',
            'body'
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        title = data.get('title', None)
        if (title == ""):
            raise forms.ValidationError("Title cannot be empty")
        return super().clean(*args,**kwargs)