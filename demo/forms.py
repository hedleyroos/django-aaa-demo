from django import forms

from demo import models


class ProductForm(forms.ModelForm):

    class Meta:
        model = models.Product
        fields = "__all__"
