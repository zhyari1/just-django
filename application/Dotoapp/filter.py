import django_filters
from django import forms
from .models import Transaction, Category

class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    amount = django_filters.RangeFilter() # this is done doesn't need any thing 
    min_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')

    class Meta:
        model = Transaction
        fields = {
            'sender_account': ['exact'],
            'receiver_account': ['exact'],
            'amount': ['exact', 'range'],
            'transaction_type': ['exact'],
            'category': ['exact'],
            'description': ['icontains'],
            'date': ['exact', 'year', 'month', 'day'],
        }
