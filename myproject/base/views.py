from django.shortcuts import render,redirect
from .models import TaskModel,completeModel,TrashModel

# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']

        TaskModel.objects.create(
            title = title_data,
            desc = desc_data
        )
        return redirect(home)
    return render(request,'add.html')

def completed(request):
    data=completeModel.objects.all()
    return render(request,'completed.html',{'data':data})

def trash(request):
    data=TrashModel.objects.all()
    return render(request,'trash.html',{'data':data})

def about(request):
    return render(request,'about.html')
def update(request,pk):
    data=TaskModel.objects.get(id=pk)
    if request.method=='POST':
        title_data=request.POST['title']
        desc_data=request.POST['desc']
        data.title=title_data
        data.desc=desc_data
        data.save()
        return redirect('home')
    return render(request,'update.html',{'data':data})


def hcomplete(request,pk):
    data=TaskModel.objects.get(id=pk)
    completeModel.objects.create(
        title=data.title,
        desc=data.desc,
 )
    data.delete()
    return redirect('home')

def hdelete(request,pk):
    data=TaskModel.objects.get(id=pk)
    TrashModel.objects.create(
        title=data.title,
        desc=data.desc,
)
    data.delete()
    return redirect('home')

def hcompleteall(request):
    data=TaskModel.objects.all()
    for i in data:
        completeModel.objects.create(
            title=i.title,
            desc=i.desc,
        )
        i.delete()
    return redirect('home')


def hdeleteall(request):
    data=TaskModel.objects.all()
    for i in data:
        completeModel.objects.create(
            title=i.title,
            desc=i.desc,
        )
        i.delete()
    return redirect('home')

def crestore(request,pk):
    data=completeModel.objects.get(id=pk)
    TaskModel.objects.create(
        title=data.title,
        desc=data.desc,
    )
    data.delete()
    return redirect('completed')

def crestoreall(request):
    data=completeModel.objects.all()
    for i in data:
        TaskModel.objects.create(
            title=i.title,
            desc=i.desc,
        )
        i.delete()
    return redirect('completed')

def tdelete(request,pk):
    TrashModel.objects.get(id=pk).delete()
    return redirect('trash')
