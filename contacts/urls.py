from django.urls import path

from .views import contactList ,contactDetail ,contactCreate,contactUpdate ,contactDelete
urlpatterns=[
    path('',contactList),
    path('create/',contactCreate),
    path('<int:pk>/',contactDetail),
    path('<int:pk>/update/',contactUpdate),
    path('<int:pk>/delete/',contactDelete),
]