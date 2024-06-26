

from django.shortcuts import render, redirect
from .models import Transaction
from .form  import TransactionFilterForm
from .filter import TransactionFilter
from django.http import HttpResponse

def your_view(request):
    if request.method == 'POST':
        form = TransactionFilterForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            transaction_type = form.cleaned_data.get('transaction_type')
            category = form.cleaned_data.get('category')
            amount_min = form.cleaned_data.get('amount_min')
            amount_max = form.cleaned_data.get('amount_max')

            transactions = Transaction.objects.all()
            if start_date:
                transactions = transactions.filter(date__gte=start_date)
            if end_date:
                transactions = transactions.filter(date__lte=end_date)
            if transaction_type:
                transactions = transactions.filter(transaction_type=transaction_type)
            if category:
                transactions = transactions.filter(category=category)
            if amount_min:
                transactions = transactions.filter(amount__gte=amount_min)
            if amount_max:
                transactions = transactions.filter(amount__lte=amount_max)
                
            

            # Insert data into the database
            for transaction in transactions:
                transaction.save()

            return redirect('your_success_url')  # Redirect to success page
    else:
        form = TransactionFilterForm()

    filter = TransactionFilter(request.GET, queryset=Transaction.objects.all())
    return render(request, 'transaction_list.html', {'filter': filter})




def view(request) : 
    return HttpResponse({"slaw"})