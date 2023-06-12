from django.urls import include, path

urlpatterns = [
    path("", include("iq_eq_app.urls")),
]
