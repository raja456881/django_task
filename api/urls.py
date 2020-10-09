from django.urls import path
from.import views
urlpatterns = [
    path("register",views.resgister.as_view(), name="register"),
    path("login",views.loginview.as_view(), name="login"),
    path("api/v1/calculate",views.calculta.as_view(),name="api1"),

]
