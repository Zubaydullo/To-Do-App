from django.shortcuts import render, redirect
from .models import TodoList, Category
from django.http import HttpResponse

# @unauthenticated_user
def index(request):
    
    todos = TodoList.objects.all()
    categories = Category.objects.all()

    if request.method == "POST":
        if "taskAdd" in request.POST:
            #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo


       
    return render(request, 'index.html', {'todos': todos, 'categories': categories})
            


