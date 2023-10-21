from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from . forms import Todoform
from . models import Todo

# Create your views here.
class Todolistview(ListView):
    model = Todo
    template_name= 'home.html'
    context_object_name = 'task1'
class Tododetailview(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'task1'
class Updateview(UpdateView):
    model = Todo
    template_name = 'edit.html'
    context_object_name = 'form'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('detailv',kwargs={'pk':self.object.id})
class deleteview(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('listv')




def add(request):
    task1 = Todo.objects.all()
    if request.method=='POST':
        name=request.POST.get('taskname','')
        prio=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Todo(name=name,priority=prio,date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})

def delete(request,taskid):
    task2=Todo.objects.get(id=taskid)
    if request.method=='POST':
        task2.delete()
        return redirect('/')
    return render(request,'delete.html',{'task2':task2})


def update(request,id):
  task=Todo.objects.get(id=id)
  form=Todoform(request.POST or None , instance=task)
  if form.is_valid():
      form.save()
      return redirect('/')
  return render(request,'edit.html',{'task':task,'form':form})




# def detail(request):
#    task=Todo.objects.all()
#    return render(request,'detail.html',{'task1':task})
