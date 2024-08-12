from .models import Tutor
from django import forms

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['classdate','mode','classhour']
        labels = {'classdate': 'Date', 'mode':'Mode','classhour':'Hour'}
        widgets = {
            'classdate': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'mode': forms.TextInput(attrs={'class':'form-control'}),
            'classhour':forms.NumberInput(attrs={'class':'form-control','step': '0.01'})
        }

class TutorEditForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['classdate','mode','classhour']
        labels = {'classdate': 'Date', 'mode':'Mode','classhour':'Hour'}
        widgets = {
            'classdate': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'mode': forms.TextInput(attrs={'class':'form-control'}),
            'classhour':forms.NumberInput(attrs={'class':'form-control','step': '0.01'})
        }