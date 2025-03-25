from django.shortcuts import render ,redirect
from django.urls import reverse_lazy

# Create your views here.

from django.core.mail import send_mail

from .models import Contact  ,Registrar
from .forms import ContactModelForm
from django.views.generic import TemplateView ,ListView ,DetailView,CreateView ,UpdateView ,DeleteView

# landding page :
class LandingpageView(TemplateView):
    template_name='landing-page.html'
# def landing_page(request):
#      return render(request,'landing-page.html')


# create :
class ContactListView(ListView):
    template_name="leads/contactList.html"
    queryset=Contact.objects.all()
    context_object_name='contacts'

# def contactList(request):
#     contacts=Contact.objects.all()
#     context={
#         "contacts":contacts
#     }
#     return render(request,"leads/contactList.html",context)

###detail:
class ContactDetailView(DetailView):
    template_name="leads/contactDetail.html"
    queryset=Contact.objects.all()
    context_object_name='contacts'

# def contactDetail(request,pk):
#     contacts=Contact.objects.get(id=pk)
#     context={
#         "contacts":contacts
#     }
#     return render(request,"leads/contactDetail.html",context)

class ContactCreateView(CreateView):
    template_name="leads/contactCreate.html"
    queryset=Contact.objects.all()
    form_class=ContactModelForm
    success_url=reverse_lazy('contacts:contact-list')
    def form_valid(self, form):
        send_mail(
            subject="a contact has been created ",
            message="go to the site to see the new contact",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super().form_valid(form)

# def contactCreate(request):
#     form=ContactModelForm()
#     if request.method=="POST":
#         form=ContactModelForm(request.POST)
#         if form.is_valid():
#          form.save()
#          return redirect("/contacts")
#     context={
#         "form":form
#     }
#     return render(request,"leads/contactCreate.html",context)
    
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
class ContactUpdateView(UpdateView):
    template_name="leads/contactUpdate.html"
    queryset=Contact.objects.all()
    form_class=ContactModelForm
    context_object_name='contacts'
    success_url=reverse_lazy('contacts:contact-list')

# def contactUpdate(request,pk):
#     contacts=Contact.objects.get(id=pk)
#     form=ContactModelForm(instance=contacts)
#     if request.method=="POST":
#         form=ContactModelForm(request.POST,instance=contacts)
#         if form.is_valid():
#             form.save()
#             return redirect("/contacts")
#     context={
#         "form":form,
#         "contacts":contacts
#     }
#     return render(request,"leads/contactUpdate.html",context)

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

class ContactDeleteView(DeleteView):
    template_name="leads/contactDelete.html"
    queryset=Contact.objects.all()
    context_object_name='contacts'
    success_url=reverse_lazy('contacts:contact-list')
# def contactDelete(request,pk):
#     contacts=Contact.objects.get(id=pk)
#     contacts.delete()
#     return redirect("/contacts")
   











