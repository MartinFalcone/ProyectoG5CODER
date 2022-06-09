
from django.urls import path
from Appclientes.views import client_view, new_client_view

urlpatterns = [
    path("",client_view, name = "Client"),
    path("create-client/",new_client_view, name = "new_client_view"),
]



