
import django_filters
from Myapp.models import *
from django import forms


import django_filters
from django import forms

class FoodFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'choice': ['exact'],
            'price':['gte','lte']
        }
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'widget': forms.TextInput(attrs={'class': 'form-control'}),
                },
            },
        }

    def __init__(self, *args, **kwargs):
        super(FoodFilter, self).__init__(*args, **kwargs)
        # Customize individual fields if needed
        # self.filters['name__icontains'].widget.attrs['class'] = 'form-control'
        self.filters['choice'].field.empty_label = "Select category"
