from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList
# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.POST.get("newItem"):
            txt = response.POST.get("new")
            defi = response.POST.get("definition")

            if (len(txt) > 0 and len(defi) > 0):
                ls.item_set.create(text=txt, definition=defi, complete=False)
            else:
                print("invalid")
        elif response.POST.get("deleteItem"):
            item_id = response.POST.get("deleteItem")
            item = ls.item_set.filter(id=item_id)
            if item.exists():
                item.delete()

        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def home(response):
    return render(response, "main/home.html", {})


def view(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in response.user.todolist.all():
        items = ls.item_set.all()
        flashcards = [
            {'front': item.text, 'back': item.definition} for item in items
            ]
        return render(response, 'main/view.html', {'flashcards': flashcards})
    return render(response, "main/view.html", {})


def menu(response):
    ls = ToDoList.objects.filter(user=response.user)
    return render(response, "main/menu.html", {"ls": ls})

def lists(response):
    ls = ToDoList.objects.filter(user=response.user)
    return render(response, "main/lists.html", {"ls": ls})
