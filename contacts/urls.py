from django.urls import path

from .views import contactList ,contactDetail ,contactCreate,contactUpdate ,contactDelete
app_name='contacts'
urlpatterns=[
    path('',contactList,name='contact-list'),
    path('create/',contactCreate ,name='contact-create'),
    path('<int:pk>/',contactDetail,name='contact-detail'),
    path('<int:pk>/update/',contactUpdate ,name='contact-update'),
    path('<int:pk>/delete/',contactDelete ,name='contact-delete'),
]