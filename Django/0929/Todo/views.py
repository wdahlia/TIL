from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.

#main page
def main(request):
    return render(request, 'Todo/main.html')

#todo page
def todo(request):
    result = []
    # create 한 쿼리문을 사이트에 받아온다
    Todo_result = Todo.objects.order_by('id').all()
    result.append(Todo_result)

    context = {
        'result' : result,
    }

    return render(request, 'Todo/todo.html', context)

def create(request):
    # 제출 받은 값을 create 해준다
    today = request.GET.get('today')
    priority = request.GET.get('priority')
    date = request.GET.get('date')
    print(today, priority, date)

    Todo.objects.create(content=today, priority=priority, deadline=date)

    return redirect('Todo:todo')

# update
def update(request, todo_pk):
    id = Todo.objects.get(id = todo_pk)
    if id.completed == False:
        id.completed = True
    else:
        id.completed = False
    id.save()

    return redirect('Todo:todo')



# delete
def delete(request, todo_pk):
    id = Todo.objects.get(id = todo_pk)
    id.delete()

    return redirect('Todo:todo')


# checkbox check 했을때 새로고침해도 reset 방지 = redirect

def check(request, todo_pk):
    id = Todo.objects.get(id = todo_pk)
    if id.completed == False:
        id.completed == True
    else:
        id.completed == False
    id.save()
        

    return redirect('Todo:todo')
