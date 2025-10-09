from django.shortcuts import render,get_object_or_404
from .models import Chaivariety,Store
from .forms import ChaiVarietyForm
def all_chai(request):
    chai=Chaivariety.objects.all()
    return render(request, "chai/all_chai.html",{"chai":chai})

def chai_detail(request,chai_id):
    chai=get_object_or_404(Chaivariety,id=chai_id)
    return render(request, "chai/chai_details.html",{"chai":chai})

def chai_stores(request):
    stores=None
    if request.method=="POST":
        form=ChaiVarietyForm(request.POST)
        if form.is_valid():
            selected_chai=form.cleaned_data['chai_variety']
            stores=Store.objects.filter(chai_variety=selected_chai)
    else:
        form=ChaiVarietyForm()
    return render(request, "chai/chai_stores.html",{"form":form,"stores":stores})
    # If no stores found, you might want to add a message to the template