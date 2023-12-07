from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import ToDoList
from .forms import CreateNewList
from django.core.mail import send_mail
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
            if form.cleaned_data["check"] == True:
                mail = response.user.username + "wants to approve list: " + t.name + ", id: " + str(t.id)
                #send_mail("List Approval Request", mail, 'user@gmail.com' ,['sivan.obiacoro@gmail.com'])
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def home(response):
    return render(response, "main/home.html", {})


def view(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in ToDoList.objects.all():
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
    ls = ToDoList.objects.filter(approved=True)
    return render(response, "main/lists.html", {"ls": ls})

def admin_approval(request):
    word_lists = ToDoList.objects.all()
    if request.user.is_superuser:
        if request.method == "POST":
            id_list = request.POST.getlist('boxes')
            word_lists.update(approved=False)
            print(id_list)
            for item_id in id_list:
                    ToDoList.objects.filter(id=int(item_id)).update(approved=True)
            return redirect("lists")
        else:
            return render(request, 'main/admin_approval.html', {"word_lists":word_lists})
    else:
        return redirect("/")
    return render(request, 'main/admin_approval.html')