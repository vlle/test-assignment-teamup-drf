from django.urls import path
from iq_eq_app import views

urlpatterns = [
    path("api/create_user", views.initalize_user),
    path("api/fill_iq", views.save_iq),
    path("api/fill_eq", views.save_eq),
    path("api/get_test_res", views.view_user),
]
