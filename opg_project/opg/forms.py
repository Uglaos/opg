from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user',)
        labels = {
            'name': 'Ime proizvoda',
            'category': 'Kategorija proizvoda',
        }

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-lg-3'
    helper.field_class = 'col-lg-7'
    helper.layout = Layout(
        Field('name', 'category',),
    )
    helper.form_method = 'POST'
