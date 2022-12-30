from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import items
from .forms import ItemForm
from django.template import loader

#For Views
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 

# Create your views here.

def index(request):
    list = items.objects.all()
    context = {
        'list' : list,
    }
    return render(request,'food/index.html',context)

class IndexClassView(ListView):
    model = items
    template_name = 'food/index.html'
    context_object_name = 'list'



def item(request):
    return HttpResponse("<h1>This is Item in a Views</h1>")

def detail(request,item_id):
    item = items.objects.get(pk=item_id)
    context = {
        'item' : item,
    }
    return render(request,'food/detail.html',context)

class FoodDetail(DetailView):
    model = items
    template_name = 'food/detail.html'
     

def create_item(request):
    form = ItemForm(request.POST or None)

    if(form.is_valid()):
        form.save()
        return redirect('food:index')

    return render(request,"food/item-form.html", {'form' : form})

# class based view of CreateItem
class CreateItem(CreateView):
    model = items
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item-form.html'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

def update_item(request,id):
    item = items.objects.get(id=id)
    form = ItemForm(request.POST or None , instance=item)

    if form.is_valid():
        form.save()
        return redirect("food:index")
    
    return render(request,"food/item-form.html",{'form':form , 'item': item})

def delete_item(request,id):
    item = items.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request,'food/delete-item.html',{'item' : item})