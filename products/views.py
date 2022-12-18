from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,TemplateView
from .forms import ProductForm
from .models import ProductItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orders.models import OrderItem, Order
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from orders.forms import CheckoutForm

# Create your views here.
class ProductListView(ListView):
    model = ProductItem
    template_name = 'products/list.html'
    context_object_name = 'products' 
    paginate_by = 120

class ProductDetailView(DetailView):
    model = ProductItem
    template_name = 'products/detail.html'
    context_object_name = 'product'

    
def addproduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            object = form.save(commit=False)
            slug = form.cleaned_data.get('title').replace(' ', '-')
            object.slug = slug
            object.save() 
            messages.success(request,'Product added successfully')
            return redirect('product_list')
        else:
            messages.error(request, 'Error adding product')
    else:
        form = ProductForm()
    return render(request, 'products/add.html',{'form': form})

def add_to_cart(request):
    id = request.POST.get('id')
    qty = request.POST.get('qty')
    print(id, qty)
    item = get_object_or_404(ProductItem, id=id)
    print(item)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    # if OrderItem already exists, just update the quantity
    order_item.quantity = qty
    order_item.save()
    request.session['cart_items'] = OrderItem.objects.filter(user=request.user, ordered=False).count()
    return JsonResponse({'status': 'success', 'message': 'Item added to cart'})

def remove_from_cart(request, id):
    item = get_object_or_404(ProductItem, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product_detail", slug=item.slug)
        

def show_cart(request):
    # get the data from orderitem table
    orders = OrderItem.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        ctx = {'orders': orders}
        return render(request, 'products/cart.html', ctx)
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("product_list")

def search(request):
    if request.method == 'GET':
        search_term = request.GET.get('search')
        products = ProductItem.objects.filter(title__icontains=search_term)
        ctx = {'object_list': products}
        return render(request, 'products/search.html', ctx)
    else:
        return redirect('product_list')

def checkout(request):
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('product_list')
    ctx = {'form': form}
    return render(request, 'products/checkout.html', ctx)