from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Task
from datetime import datetime
from django.contrib import messages

@login_required
def home(request):
    # Get the tasks
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks':tasks}
    return render(request, 'main/home.html', context)

@login_required
def save_task(request):
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        task_note = request.POST.get('task_note')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        priority = request.POST.get('priority')
        tags = request.POST.get('tags')
        
        #Basic validation
        if not task_name:
            messages.error(request, 'Task name is required')
            return render(request, 'main/home.html')
        
        #date and time validation
        try:
            if due_date:
                due_date = datetime.strptime(due_date,'%Y-%m-%d').date()
            if due_time:
                due_time = datetime.strptime(due_time, '%H:%M').time()
        except ValueError as e:
            messages.error(request, 'Invalid date and time format')
            return render(request, 'main/home.html')
        
        #create task
        task = Task(
            user = request.user,
            title = task_name,
            description = task_note,
            due_date = due_date,
            due_time = due_time,
            priority = int(priority),
            tags = tags
        )
        
        task.save()
        messages.success(request, "Task successfully created")
        return redirect('home')
    else:
        return render(request, 'main/home.html')
