from django import forms
from .models import Item
INPUT_CLASSES = 'w-full py-6 px-6 rounded-xl border'
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','type','price','category','description','photo')
        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'type':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'photo': forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })

        }
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','type','price','category','description','photo','is_sold')
        widgets = {
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'type':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'photo': forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })

        }
    