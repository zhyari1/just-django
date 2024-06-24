import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = {
            'transaction_type': ['exact'],
            'category': ['exact'],
            'amount': ['gte', 'lte'],
            'date': ['exact', 'year', 'month', 'day'],
        }
