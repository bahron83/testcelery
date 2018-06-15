from django import forms

class ExecuteSumForm(forms.Form):
    x = forms.IntegerField()
    y = forms.IntegerField()