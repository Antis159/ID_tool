from django import forms


class IdUpload(forms.Form):
    text = forms.CharField(label='Enter ID(s) you wish to validate', label_suffix='', widget=forms.Textarea)
class IdGenerate(forms.Form):
    text = forms.CharField(label='How many ID(s) do you wish to generate', label_suffix='')
