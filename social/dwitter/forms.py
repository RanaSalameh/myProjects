from django import forms
from .models import Dweet

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label="", # removes the Body text that previously showed up due to a 
                  #Django default setting that renders the name of a form field as its labe
    )
    class Meta:
        model = Dweet
        #هون يا بنحط الفيلدز اللي بدنا اياها تظهر يا بنعمل exclude
        exclude = ("user", ) #exclude the user field from Dweet Model Class