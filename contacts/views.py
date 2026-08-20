from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.")
            return redirect("contacts:index")
    else:
        form = ContactForm()

    return render(request, "contacts/index.html", {"form": form})