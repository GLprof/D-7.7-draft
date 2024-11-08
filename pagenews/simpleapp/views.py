from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import PForm
from .models import P
from .filters import PFilter

class PList(ListView):
    model = P
    ordering = 'title_p'
    template_name = "flatpages/p.html"
    context_object_name = 'p'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, p=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context

class PDetail(DetailView):
    model = P
    template_name = 'flatpages/p_id.html'
    context_object_name = 'p_id'

    def get_context_data(self, p_id=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = None
        return context

def creat_p(request):

    if request.method == 'POST':
        form = PForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/p/')
    form = PForm()
    return render(request, 'flatpages/p_creat.html', {'form': form})


def update_p(request, pk):
    p_object = get_object_or_404(P, pk=pk)
    if request.method == 'POST':
        form = PForm(request.POST, instance=p_object)
        if form.is_valid():
            form.save()
            return redirect('/p/')
    form = PForm
    return render(request, 'flatpages/p_update.html', {'form': form})


def delete_p(request, pk):
    p_object = get_object_or_404(P, pk=pk)
    if request.method == 'POST':
        p_object.delete()
        return redirect('/p/')
    return render(request, 'flatpages/p_delete.html', {'object': p_object})


