from django import forms

SHIFTS = tuple([
    (id, shift) for id, shift in enumerate(
        'morning afternoon evening'.split()
    )
])

class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    shift = forms.ChoiceField(choices=SHIFTS)
    time_log = forms.TimeField()

class ModelInputForm(forms.ModelForm):
    pass

