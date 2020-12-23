from django.urls import path
from .import views
urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about",views.about,name="aboutUs"),
    path("address",views.address,name="address"),
    path("contact",views.contact,name="contactUs"),
    path("tracker",views.tracker,name="trakingstatus"),
    path("productView",views.productView,name="productView"),
    path("checkout",views.checkout,name="checkout"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("payment",views.payment,name="payment"),
]