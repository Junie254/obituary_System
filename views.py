
from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Obituary
from .forms import ObituaryForm
from django.contrib import messages

def submit_obituary(request):
    if request.method == "POST":
        form = ObituaryForm(request.POST)
        if form.is_valid():
            obituary = form.save(commit=False)
            obituary.slug = slugify(obituary.name)
            obituary.save()
            messages.success(request, 'Obituary submitted successfully!')
            return redirect('view_obituaries')
    else:
        form = ObituaryForm()
    return render(request, 'obituary_form.html', {'form': form})

def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})

def home(request):
    return render(request, 'home.html')
