from django import forms

from .models import Logger
SHIFTS = tuple([
    (id, shift) for id, shift in enumerate(
        'morning afternoon evening'.split()
    )
])

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField(help_text='enter exact time')

class LogForm(forms.ModelForm):
    class Meta:
        model = Logger
        fields = '__all__'

