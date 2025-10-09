from django import forms
from .models import Chaivariety

class ChaiVarietyForm(forms.Form):
    chai_variety=forms.ModelChoiceField(queryset=Chaivariety.objects.all(),
                                        empty_label="Select a Chai Variety",
                                        label="Chai Variety",
                                        
                                        help_text="Choose your favorite chai variety")
