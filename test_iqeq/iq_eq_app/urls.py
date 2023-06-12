from django.urls import path
from iq_eq_app import views

urlpatterns = [
    path("api/create_user", views.initalize_user, name="api/create_user"),
    path("api/fill_iq", views.save_iq, name="api/fill_iq"),
    path("api/fill_eq", views.save_eq, name="api/fill_eq"),
    path("api/get_test_res", views.view_user, name="api/get_test_res"),
]
