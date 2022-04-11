
from django.shortcuts import render, redirect

from home.forms import ContactUs


def home_page(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = ContactUs()

    return render(request, 'home_page.html', {'form': form})
