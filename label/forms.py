from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PatientForm(forms.Form):
    CHOICES_AP = [('0', 'Normal'),('1', 'Apical Anterior'),('2', 'Basal'),('3', 'Septal'),('4', 'Deleted')]
    CHOICES_lat = [('0', 'Normal'),('1', 'Septal'),('2', 'Posterolateral'),('3', 'Deleted')]

    label_ap = forms.ChoiceField(choices=CHOICES_AP, widget=forms.RadioSelect, label="AP", label_suffix=":")
    label_lat = forms.ChoiceField(choices=CHOICES_lat, widget=forms.RadioSelect, label="Lateral", label_suffix=":") #, initial="3"

    def clean_label_ap(self):
        data = self.cleaned_data['label_ap']
        # Check if there is no data.
        if len(data) < 1 :
            raise ValidationError(_("can't be empty!"))
        # Remember to always return the cleaned data.
        return data

    def clean_label_lat(self):
        data = self.cleaned_data['label_lat']
        # Check if there is no data.
        if len(data) < 1 :
            raise ValidationError(_("can't be empty!"))
        # Remember to always return the cleaned data.
        return data
