from django.forms import DateInput
from django_filters import FilterSet, DateTimeFilter
from .models import P

class PFilter(FilterSet):
    datetime_p = DateTimeFilter(field_name='datetime_p', lookup_expr='gt',
                                label='Позже указываемой даты',
                                widget=DateInput(
                                attrs={'placeholder': 'Select a date', 'type': 'date'}),
                                )
    class Meta:
        model = P
        fields = {
            'title_p': ['icontains'],
            'cost_p': [
                'lt',
                'gt',
            ],
        }