from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Cronjob
from .forms import CronjobForm

# Create your views here.

def home(request):
    return render(request,'home.html')

@login_required
def cronjob_list(request):
    cronjobs = Cronjob.objects.filter(user=request.user).order_by('id')
    return render(request,'cronjob_list.html',{'cronjobs':cronjobs})  

@login_required
def cronjob_create(request):
    if request.method=='POST':
        form=CronjobForm(request.POST,user=request.user)
        if form.is_valid():
            cronjob=form.save(user=request.user,commit=False)
            cronjob.save()
            return redirect('cronjob_list')
    return render(request,'cronjob_create.html')
