from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages


from .models import Task



class HomePageView(View):


    template_name='index.html'

    def get(self,request,*args,**kwargs):
        tasks=Task.objects.all()

        context={
            'tasks':tasks
        }
        return render(request,self.template_name,context)


    def post(self,request,*args,**kwargs):
        name=request.POST.get('name')

        phone_number=request.POST.get('phone_number')

        new_todo=Task(name=name,phone_number=phone_number)

        new_todo.save()

        return redirect('todo:home')


class DeleteView(View):
    def get(self,request,id,*args,**kwargs):
        task_to_delete=Task.objects.filter(id=id).first()

        task_to_delete.delete()

        messages.info(request,'Task Deleted Successfully')

        return redirect('todo:home')


class UpdateView(View):


    template_name='update.html'

    def get(self,request,id,*args,**kwargs):
        

        task=Task.objects.filter(id=id).first()

        context={
            'task':task
        }
        return render(request,self.template_name,context)


    def post(self,request,id,*args,**kwargs):
        task_to_update=Task.objects.filter(id=id).first()

        new_task_data=request.POST.get('name')

        task_to_update.name=new_task_data

        task_to_update.save()

        messages.success(request,'Task Updated Successfully')

        return redirect('todo:home')