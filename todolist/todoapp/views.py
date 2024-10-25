from django.shortcuts import render,redirect
from .models import Todo
 

def todo_view(request):
    tasks=Todo.objects.all()
    if request.method == 'POST':
        new_task=request.POST.get('add_task')
        if new_task:
            you=Todo.objects.create(task=new_task)
            you.save() 
            return redirect('/')    
         
    return render (request, 'second.html',{'tasks':tasks})


def delete_task(request,task_id):
   task_d= Todo.objects.get(id=task_id)
   task_d.delete()    
   return redirect('/')
