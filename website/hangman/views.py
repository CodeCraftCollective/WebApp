from django.shortcuts import render
from django.http import HttpResponseRedirect
def hangman(response):
    return render(response, "hangman/hangman.html", {})