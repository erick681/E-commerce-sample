from django.shortcuts import render , redirect
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import *
from django.db.models import Q
from .forms import *
app_name = 'item'
def items(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query','')
    category_id = request.GET.get('category',0)
    categories = Category.objects.all()
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'item/items.html',{'items':items,'query':query,'categories':categories,'category_id':int(category_id)})
def details(request,pk):
    item = get_object_or_404(Item,pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{'item':item,'related_items':related_items})
@login_required
def new(request):
    if request.method == 'POST':
        forms = ItemForm(request.POST, request.FILES)
        if forms.is_valid():
            item = forms.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:details',pk=item.id)
    else :
        forms = ItemForm()
    title = 'new Item '
    return render(request,'item/new_item.html',{'forms':forms,'title':title})
@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        forms = EditItemForm(request.POST, request.FILES,intance=item)
        if forms.is_valid():
            item = forms.save(commit=False)
            return redirect('item:details',pk=item.id)
    else :
        forms = EditItemForm(instance=item)
    title = 'Edit Item '
    return render(request,'item/new_item.html',{'forms':forms,'title':title})
@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:items')

