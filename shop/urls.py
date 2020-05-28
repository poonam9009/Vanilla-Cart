from.import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = "shopHome"),
    path('about/',views.about,name = "about us"),
    path('contact/',views.contact,name = "contect"),
    path('search/', views.search, name="search"),
    path('tracker/', views.tracker, name="tracker"),
    path("productview/<int:myid>", views.productview, name="Productview"),
    path('checkout/', views.checkout, name="checkout"),
    path('handelrequest/', views.handelrequest, name="handelrequest"),
]
