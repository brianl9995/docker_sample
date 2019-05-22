from django import forms


class TaskForm(forms.Form):
    message = forms.CharField(label='Mensaje')
