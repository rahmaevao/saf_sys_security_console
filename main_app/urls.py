from django.urls import path
from main_app.views import all_premises_view, concrete_premises_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', all_premises_view, name='home'),
    path('premises/<int:num_of_premises>/', concrete_premises_view)
]

urlpatterns += staticfiles_urlpatterns()
