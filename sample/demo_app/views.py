from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

from .forms import TaskForm
from .tasks import demo_task


class HomeView(FormView):
    template_name = 'demo_app/home.html'
    form_class = TaskForm
    success_url = reverse_lazy('demo_app:home')

    def form_valid(self, form):
        response = super().form_valid(form)

        demo_task.delay(form.cleaned_data['message'])

        return response
