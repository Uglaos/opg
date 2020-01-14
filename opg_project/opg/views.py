from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm


@login_required()
def product_list(request):
    context = {
        'product_list': Product.objects.filter(user=request.user),
        'title': 'Pregled proizvoda',
    }
    return render(request, 'opg/product_list.html', context)


@login_required()
def add_product(request):
    if request.method == 'POST':
        p_form = ProductForm(request.POST)
        if p_form.is_valid():
            form = p_form.save(commit=False)
            form.user = request.user
            form.save()
            product = p_form.cleaned_data.get('name')
            messages.success(request, f'Dodali ste novi proizvod "{product}"!')
            return redirect('product_list')
    else:
        p_form = ProductForm()

    context = {
        'p_form': p_form,
        'title': 'Dodavanje proizvoda',
    }
    return render(request, 'opg/add_product.html', context)


@login_required()
def detail(request, product_id):
    try:
        products = Product.objects.filter(user=request.user)
        p = products.get(pk=product_id)
        if request.method == 'POST':
            p_form = ProductForm(request.POST, instance=p)
            if p_form.is_valid():
                form = p_form.save(commit=False)
                form.user = request.user
                form.save()
                product = p_form.cleaned_data.get('name')
                messages.success(request, f'Ažurirali ste proizvod "{product}"!')
                return redirect('product_list')
        else:
            p_form = ProductForm(instance=p)
        context = {
            'p_form': p_form,
            'title': 'Editiranje proizvoda',
        }
    except Product.DoesNotExist:
        raise Http404("Proizvod ne postoji!")
    return render(request, 'opg/product.html', context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, f'Izbrisali ste proizvod "{product}"!')
        return redirect('product_list')
    context = {
        'product_list': Product.objects.filter(user=request.user),
        'title': 'Pregled proizvoda',
    }
    return render(request, 'opg/product_list.html', context)
