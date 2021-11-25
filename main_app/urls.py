from django.urls import path
from main_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main_app.models import Premises


home_list_view = views.HomeListView.as_view(
    queryset=Premises.objects.order_by,
    context_object_name="all_premises",
    template_name="main_app/home.html",
)


urlpatterns = [
    path("", home_list_view, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]

urlpatterns += staticfiles_urlpatterns()
