from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product, Category
from django import forms
# from django import request
from django.db.models import fields
from django.utils.text import slugify


class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
      
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget = forms.HiddenInput()
        self.fields['choice'].empty_label = "select category"


class CateForm(forms.ModelForm):
    class Meta:
        model= Category
      
        fields = '__all__'
    
    # def __init__(self, *args, **kwargs):
    #     super(CateForm, self).__init__(*args, **kwargs)
    #     # self.fields['username'].widget = forms.HiddenInput()
    #     self.fields['choice'].empty_label = "select category"