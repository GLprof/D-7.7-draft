from django import forms
from django.core.exceptions import ValidationError
from .models import P

class PForm(forms.ModelForm):

    class Meta:
        model = P
        fields = [
            'title_p',
            'category_p',
            'description_p',
            'cost_p',
            'quantity_p',
        ]





