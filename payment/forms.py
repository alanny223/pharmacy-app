from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="Full Name", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Full Name'}), required=True)
    shipping_email = forms.CharField(label="Email", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email Address'}), required=True)
    shipping_address1 = forms.CharField(label="Address 1", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Address1'}), required=True)
    shipping_address2 = forms.CharField(label="Address 2", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Address2'}), required=False)
    shipping_city = forms.CharField(label="City",
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
                                    required=True)
    shipping_state = forms.CharField(label="State",
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
                                     required=False)
    shipping_zipcode = forms.CharField(label="Zipcode", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Zipcode'}), required=False)
    shipping_country = forms.CharField(label="Country", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Country'}), required=True)
    shipping_phone = forms.CharField(label="Phone", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city',
                  'shipping_state', 'shipping_zipcode', 'shipping_country', 'shipping_phone']

        exclude = ['user', ]


class PaymentForm(forms.Form):
    card_name = forms.CharField(label="Card Name",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name On Card'}),
                                required=True)
    card_number = forms.CharField(label="Card Number",
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number'}),
                                  required=True)
    card_exp_date = forms.CharField(label="Card Expiry Date", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Expiration Date'}), required=True)
    card_cvv_number = forms.CharField(label="Card Cvv Number", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'CVV Code'}), required=True)
    card_address1 = forms.CharField(label="Card Address1", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Billing Address 1'}), required=True)
    card_address2 = forms.CharField(label="Card Address2", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Billing Address 2'}), required=False)
    card_city = forms.CharField(label="Card City",
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Billing City'}),
                                required=True)
    card_region = forms.CharField(label="Card Region", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Billing region'}), required=False)
    card_zipcode = forms.CharField(label="Card Zipcode", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Billing Zipcode'}), required=True)
    card_country = forms.CharField(label="Card Country", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Billing Country'}), required=True)
