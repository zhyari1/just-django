from django import forms
from .models import Transaction

class SendTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'transaction_type', 'category', 'date']  # Remove 'sender_account' and 'receiver_account'

class TransactionFilterForm(forms.Form):
    sender_account = forms.CharField(max_length=100, required=False)
    receiver_account = forms.CharField(max_length=100, required=False)
    amount_min = forms.DecimalField(required=False, decimal_places=2, max_digits=10, label='Min Amount')
    amount_max = forms.DecimalField(required=False, decimal_places=2, max_digits=10, label='Max Amount')
    transaction_type = forms.ChoiceField(choices=Transaction.TRANSACTION_TYPE_CHOICES, required=False)
    category = forms.CharField(max_length=100, required=False)
    description = forms.CharField(max_length=255, required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
