from django.urls import path
from main_app.views import all_premises_view, concrete_premises_view, premises_switch_mode
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', all_premises_view, name='home'),
    path('premises/<int:num_of_premises>/',
         concrete_premises_view,
         name='concrete_premises_view'),
    path('premises/<int:num_of_premises>/premises_switch_mode/',
         premises_switch_mode),
]

urlpatterns += staticfiles_urlpatterns()
