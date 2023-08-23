from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'stock', 'image')

class SizeSelectionForm(forms.Form):
    sizes = forms.MultipleChoiceField(
        choices=[
            ('220', '220'),
            ('230', '230'),
            ('240', '240'),
            ('250', '250'),
            ('260', '260'),
            ('270', '270'),
        ],
        widget=forms.CheckboxSelectMultiple
    )