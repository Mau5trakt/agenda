from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Contact
from .forms import ContactForm
# Create your views here.

def index(request):

    contacts = Contact.objects.all()

    return render(request, 'people/index.html', {'contacts': contacts})

def add_contact(request):
    form = ContactForm(request.POST)

    if request.POST:
        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            Contact.objects.create(name=cd['name'], email=cd['email'], phone=cd['phone'])

            return redirect(reverse('people:index'))


    return render(request, 'people/add.html', {'form': form})

def edit(request, id):
    contact = get_object_or_404(Contact, id=id)

    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(reverse('people:index'))

    else:
        form = ContactForm(instance=contact)

    return render(request, 'people/edit.html', {'form': form})
