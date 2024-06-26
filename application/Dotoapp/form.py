from django import forms
from .models import Transaction

class SendTransactionForm(forms.ModelForm): # sabing the inserted data form user  submit in the database that we created the model for 
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'transaction_type', 'category', 'date']  # Remove 'sender_account' and 'receiver_account'

class TransactionFilterForm(forms.Form): # this use for the form user input submittion and make the input compare with the database condition for not getting error  and the accpecting the input user 
    # and the after filtering it goes to transaction filter just for  sql enjection   , the oparation for trancation is continue need more info about how to work 
    # 
    sender_account = forms.CharField(max_length=100, required=False)
    receiver_account = forms.CharField(max_length=100, required=False)
    amount_min = forms.DecimalField(required=False, decimal_places=2, max_digits=10, label='Min Amount')
    amount_max = forms.DecimalField(required=False, decimal_places=2, max_digits=10, label='Max Amount')
    transaction_type = forms.ChoiceField(choices=Transaction.TRANSACTION_TYPE_CHOICES, required=False)
    category = forms.CharField(max_length=100, required=False)
    description = forms.CharField(max_length=255, required=False)
    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
