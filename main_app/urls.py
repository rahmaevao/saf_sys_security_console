from django.urls import path
from main_app.views import all_premises_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from main_app.models import Premises


urlpatterns = [
    path("", all_premises_view, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
