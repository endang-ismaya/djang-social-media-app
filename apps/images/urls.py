from django.urls import path


from apps.images import views


urlpatterns = [
    path("", views.index, name="images.index"),
]
