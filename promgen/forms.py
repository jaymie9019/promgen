from django import forms


class ExporterForm(forms.Form):
    job = forms.CharField()
    port = forms.IntegerField()
    path = forms.CharField(required=False)
    project_id = forms.HiddenInput()
