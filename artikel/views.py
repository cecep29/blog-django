from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Artikel


# Create your views here.
class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_list.html'
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        list_kategori = self.model.objects.values_list('kategory', flat=True).distinct()
        self.kwargs.update({'list_kategori': list_kategori})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)


class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_kategori_list.html'
    context_object_name = 'artikel_list'
    ordering = ['-published']
    paginate_by = 2

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategory=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        list_kategori = self.model.objects.values_list('kategory', flat=True).distinct().exclude(kategory=self.kwargs['kategori'])
        self.kwargs.update({'list_kategori': list_kategori})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)



class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/artikel_detail.html'
    context_object_name = 'artikel'

    def get_context_data(self, *args, **kwargs):
        list_kategori = self.model.objects.values_list('kategory', flat=True).distinct()
        self.kwargs.update({'list_kategori': list_kategori})
        artikel_serupa = self.model.objects.filter(kategory=self.object.kategory).exclude(id=self.object.id)
        self.kwargs.update({'artikel_serupa': artikel_serupa})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)