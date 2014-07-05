from django import forms
from django.forms.extras.widgets import SelectDateWidget

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(max_length= 100, required=False)
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("MOAR WERDZ!")
        return message


        
class RandomGameForm(forms.Form):
    p_years = ('1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990')
    onwed_choices = (('yes','Yes, only my games'), ('no','No, only games I don\'t own'),
    ('all','All games ever made, ever!'))
    owned = forms.ChoiceField(widget=forms.RadioSelect, choices=onwed_choices)
    year = forms.DateField(widget=SelectDateWidget(years = p_years))
    # owned = forms.RadioSelect