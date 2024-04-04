from django import forms as f
from .models import *

class CreateListingForm(f.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateListingForm, self).__init__(*args, **kwargs)
        self.initial['categ'] = 'Category'

    class Meta:
        model = Listing
        fields = ('title', 'description', 'price', 'categ', 'image_url')

        labels = {
                'title': '',
                'description': '',
                'price': '',
                'categ': '',
                'image_url': ''
            }
        
        widgets = {
                'title': f.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
                'description': f.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
                'price': f.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price', 'min': '1'}),
                'categ': f.Select(attrs={'class': 'form-control',}, choices=Category.objects.all()),
                'image_url': f.TextInput(attrs={'class': 'form-control', 'placeholder': 'Image URL'})
            }
        
    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 1:
            raise f.ValidationError('The price must at least $1')
        
        return price


class PlaceBidForm(f.ModelForm):
    class Meta:
        model = Bid
        fields = ('amount',)

        labels = {'amount': '',}
        
        widgets = {'amount': f.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Bid'}),}


class AddCommentForm(f.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

        labels = {'text': '',}
        
        widgets = {'text': f.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment'}),}