from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item

from django.views.generic.list import ListView #ListView, a built-in Django class-based view specifically designed to display list ofobjects from a database.
from django.views.generic.detail import DetailView #detail view is nothing but anything which gives you the detail of particular item
from django.views.generic.edit import CreateView
#import from the forms
from .forms import ItemForm

# Create your views here.
def index(request):
    item_list=Item.objects.all()
    context={
        "item_list":item_list,#- Here, the key is `"item_list"` and the value is the `item_list` variable you created earlier. This means the template will have access to a variable named `item_list` that contains the list of items.
    }
    return render(request,"index.html",context)

#Class-based views are a more structured and reusable way to handle views in Django.
#class based views for List View over index function
class IndexClassView(ListView):
    model=Item
    template_name='index.html'
    context_object_name='item_list'

#detail of specific product
def detail(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        "item":item,
    }
    # return HttpResponse("The Item_id of : %s" % item_id)
    return render(request,'detail.html',context)
#class for detail view
class FoodDetailView(DetailView):
    model=Item # we have pass pk in url
    template_name='detail.html' #here we are not passing context to the detail.html so in place item context we have to give object

def create_item(request):
    form=ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request,'item-form.html',{"form":form})
#class based view for create item
class CreateItem(CreateView):
    model=Item;
    fields=['item_name','item_desc','item_price','item_image']
    template_name='item-form.html'
    
    def form_valid(self, form):#This method is called when the submitted form is valid, i.e., all the fields have been filled out correctly and there are no errors
        #form.instance: This refers to the newly created instance of the Item model based on the submitted form data.
        form.instance.user_name=self.request.user# get current user who is logged in
        return super().form_valid(form)#This line calls the form_valid method of the superclass (CreateView), which proceeds to save the new item to the database and perform any additional actions defined in the parent class, like redirecting to a success URL.
    

def update_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'item-form.html',{'form':form,'item':item})

def delete_item(request,id):
    item=Item.objects.get(id=id)

    if request.method=='POST':
        item.delete()
        return redirect('index')
    return render(request,'item-delete.html',{'item':item})
