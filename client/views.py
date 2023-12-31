from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from client.forms import ClientForm
from client.models import Client


# Create your views here.
class ClientCreateView(LoginRequiredMixin, CreateView):
    """Создание нового клиента"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_all')

    def form_valid(self, form):
        self.object = form.save()
        self.object.from_user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Изменение/обновление уже созданного клиента"""

    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_all')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление клиента"""

    model = Client
    success_url = reverse_lazy('client:client_all')


class ClientListView(ListView):
    """Просмотр всех созданных клиентов"""

    model = Client
    extra_context = {
        'title': "Созданные клиенты",
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Client.objects.filter(from_user=self.request.user)
        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Просмотр одного клиента"""

    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Client.objects.filter(pk=self.object.pk, user=self.request.from_user)
        return context
