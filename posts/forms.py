from django import forms


class CategoriesCreateForm(forms.Form):
    title = forms.CharField(max_length=50)



class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=30, min_length=3)
    # description = forms.CharField(widget=forms.Textarea())
    measure = forms.CharField(max_length=10)
    cost = forms.FloatField()
    amount = forms.IntegerField()
    # categories = forms.CharField

