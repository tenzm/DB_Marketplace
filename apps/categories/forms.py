from django import forms
from apps.categories.models import Category


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
