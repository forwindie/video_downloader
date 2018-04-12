from django import forms
from convapp.models import Query


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('link',)
