from django.shortcuts import render
from item.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    return render(request,'dashbord/index.html',{'items':items})
