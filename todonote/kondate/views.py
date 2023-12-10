from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
    )
from django.core.paginator import Paginator
from .models import Kondate

from consts import ITEM_PER_PAGE

class KondateList(LoginRequiredMixin, ListView):
    model = Kondate
    template_name = 'kondate/kondate_list.html' 
    paginate_by = ITEM_PER_PAGE

class DetailKondateList(LoginRequiredMixin, DetailView):
    model = Kondate
    template_name = 'kondate/kondate_detail.html'

class CreateKondateList(LoginRequiredMixin, CreateView):
    model = Kondate
    fields = "__all__"
    template_name = 'kondate/kondate_create.html'
    success_url = reverse_lazy('list-kondate')

class UpdateKondateList(LoginRequiredMixin, UpdateView):
    model = Kondate
    fields = "__all__"
    template_name = 'kondate/kondate_update.html'
    success_url = reverse_lazy('list-kondate')


class DeleteKondateList(LoginRequiredMixin, DeleteView):
    model = Kondate
    template_name = 'kondate/kondate_confirm_delete.html'
    success_url = reverse_lazy('list-kondate')

def index_view(request):
    object_list = Kondate.objects.order_by('eatday')

    paginator = Paginator(object_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.page(page_number)

    return render(request, 'kondate/index.html', {'object_list': object_list, 'page_obj': page_obj,},)

