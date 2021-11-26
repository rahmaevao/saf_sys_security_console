from django.shortcuts import render
from django.views.generic import ListView
from main_app.models import Premises


class AllPremisesView(ListView):
    model = Premises

    def get_context_data(self, **kwargs):
        context = super(AllPremisesView, self).get_context_data(**kwargs)
        return context


all_premises_view = AllPremisesView.as_view(
    queryset=Premises.objects.order_by,
    context_object_name="all_premises",
    template_name="main_app/home.html",
)


def concrete_premises_view(request, num_of_premises):
    premises = Premises.objects.get(pk=num_of_premises)
    return render(
        request,
        'main_app/premises.html',
        {
            'premises': premises,
        }
    )
