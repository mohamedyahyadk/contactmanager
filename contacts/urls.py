from django.urls import path

from .views import ContactCreateView,ContactDetailView, ContactUpdateView,ContactDeleteView ,ContactListView
app_name='contacts'
urlpatterns=[
    path('',ContactListView.as_view(),name='contact-list'),
    path('create/',ContactCreateView.as_view() ,name='contact-create'),
    path('<int:pk>/',ContactDetailView.as_view(),name='contact-detail'),
    path('<int:pk>/update/',ContactUpdateView.as_view() ,name='contact-update'),
    path('<int:pk>/delete/',ContactDeleteView.as_view() ,name='contact-delete'),
]