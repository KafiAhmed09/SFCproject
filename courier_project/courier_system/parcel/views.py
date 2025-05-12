from django.shortcuts import render


from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.calculate_charge()  
            order.save()
            return redirect('order_summary', pk=order.pk)
    else:
        form = OrderForm()
    
    return render(request, 'create_order.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Order

def order_summary(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_summary.html', {'order': order})
