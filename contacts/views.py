from django.shortcuts import render ,redirect


# Create your views here.



from .models import Contact  ,Registrar
from .forms import ContactModelForm
def contactList(request):
    contacts=Contact.objects.all()
    context={
        "contacts":contacts
    }
    return render(request,"leads/contactList.html",context)

def contactDetail(request,pk):
    contacts=Contact.objects.get(id=pk)
    context={
        "contacts":contacts
    }
    return render(request,"leads/contactDetail.html",context)


def contactCreate(request):
    form=ContactModelForm()
    if request.method=="POST":
        form=ContactModelForm(request.POST)
        if form.is_valid():
         form.save()
         return redirect("/contacts")
    context={
        "form":form
    }
    return render(request,"leads/contactCreate.html",context)
    
# def contactCreate(request):
#     form=ContactForm()
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#          name=form.cleaned_data["name"]
#          email=form.cleaned_data["email"]
#          phone=form.cleaned_data["phone"]
#          registrar=Registrar.objects.first()
#          Contact.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             registrar=registrar
#          )
#          return redirect("/contacts")
#     context={
#         "form":form
#     }
#     return render(request,"leads/contactCreate.html",context)

def contactUpdate(request,pk):
    contacts=Contact.objects.get(id=pk)
    form=ContactModelForm(instance=contacts)
    if request.method=="POST":
        form=ContactModelForm(request.POST,instance=contacts)
        if form.is_valid():
            form.save()
            return redirect("/contacts")
    context={
        "form":form,
        "contacts":contacts
    }
    return render(request,"leads/contactUpdate.html",context)

# def contactUpdate(request,pk):
#     contacts=Contact.objects.get(id=pk)
#     form=ContactForm()
#     if request.method=="POST":
#         form=ContactForm(request.POST)
#         if form.is_valid():
#             name=form.cleaned_data["name"]
#             email=form.cleaned_data["email"]
#             phone=form.cleaned_data["phone"]
#             registrar=Registrar.objects.first()
#             contacts.name=name
#             contacts.email=email
#             contacts.phone=phone
#             contacts.registrar=registrar
#             contacts.save()
#             return redirect("/contacts")
#     context={
#         "form":form,
#         "contacts":contacts
#     }
#     return render(request,"leads/contactUpdate.html",context)

def contactDelete(request,pk):
    contacts=Contact.objects.get(id=pk)
    contacts.delete()
    return redirect("/contacts")
   











