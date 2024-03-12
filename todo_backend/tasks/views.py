from django.shortcuts import render, redirect
from .models import Task
from django.http import JsonResponse

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
        return redirect('task_list')

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

def toggle_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

# views.py

from django.shortcuts import render, redirect
from .forms import CVForm
from .models import CV
from django.contrib import messages

def create_cv(request):
       if request.method == 'POST':
           form = CVForm(request.POST)
           if form.is_valid():
               # Xử lý dữ liệu ở đây - lưu vào database, gửi email, etc.
               # Redirect đến trang mới hoặc hiển thị thông báo thành công
               messages.success(request, 'CV đã được tạo!')
               return redirect('success-url')
               # In dữ liệu ra console
               
       else:
           form = CVForm()

       return render(request, 'tasks/create_cv.html', {'form': form})

def view_cv(request, pk):
    cv = CV.objects.get(pk=pk)
    return render(request, 'cv_template.html', {'cv': cv})