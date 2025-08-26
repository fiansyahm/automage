from django import forms
from .models import Cronjob

class CronjobForm(forms.ModelForm):
    class Meta:
        model = Cronjob
        fields = ['name','url','schedule']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CronjobForm, self).__init__(*args, **kwargs)

    def save(self,user, commit=True):
        cronjob = super(CronjobForm, self).save(commit=False)
        cronjob.user = user
        if commit:
            cronjob.save()
        return cronjob
