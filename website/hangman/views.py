from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.models import ToDoList

def hangman(response, id):
    ls = ToDoList.objects.get(id=id)
    if ls in ToDoList.objects.all():
        items = ls.item_set.all()
        words = [item.text for item in items]
        return render(response, 'hangman/hangman.html', {'words': words})
    return render(response, "hangman/hangman.html", {})

def menu(response):
    ls = ToDoList.objects.filter(user=response.user)
    return render(response, "hangman/menu.html", {"ls": ls})