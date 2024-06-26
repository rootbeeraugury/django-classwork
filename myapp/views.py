from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .default_data import load_default_data
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Invention
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Invention, Category
from .forms import InventionForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#class from which all class based views inherit
class BaseView(TemplateView):
    default_title = 'yeehaw'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('title', self.default_title)
        return context

def function_view(request):
    context = {
        'page_title': 'Function-Based View',
        'page_heading': 'Welcome to the Function-Based View',
        'page_content': 'This is the content generated by the function-based view.',
    }
    return render(request, 'bootswatch.html', context)

def load_default_data_view(request):
    load_default_data()  # Call the load_default_data function
    return JsonResponse({'status': 'success'})

class InventionListView(ListView):
    model = Invention
    template_name = 'invention_list.html'
    context_object_name = 'inventions'

class InventionDetailView(DetailView):
    model = Invention
    template_name = 'invention_view.html'
    context_object_name = 'invention'

class InventionCreateView(LoginRequiredMixin, CreateView):
  model = Invention
  form_class = InventionForm
  template_name = 'create_invention.html'
  success_url = reverse_lazy('invention-list')

class InventionUpdateView(LoginRequiredMixin, UpdateView):
  model = Invention
  form_class = InventionForm
  template_name = 'update_invention.html'
  success_url = reverse_lazy('invention-list')

class InventionDeleteView(LoginRequiredMixin, DeleteView):
  model = Invention
  success_url = reverse_lazy('invention-list')


class ClassView(BaseView):
  template_name = 'bootswatch.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'Class-Based View',
          'page_heading': 'Welcome to the Class-Based View',
          'page_content': 'This is the content generated by the class-based view.',
      })
      return context

class about(BaseView):
  template_name = 'about.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'about',
          'page_heading': "Here's my about page :)",
          'page_content': 'Lorem ipsum dolor amet...',
      })
      return context

class home(BaseView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'home',
          'page_heading': "website home/landing page",
          'page_content': 'welcome!',
      })
      return context

class portfolio(BaseView):
  template_name = 'portfolio.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'portfolio',
          'page_heading': "here's where i'd keep my portfolio if i had one",
      })
      return context

class printingpress(BaseView):
  template_name = 'printingpress.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'portfolio',
          'page_heading': "the printing press was invented in 1440 by johannes gutenberg",
      })
      return context

class cats(BaseView):
  template_name = 'cats.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': 'my cats',
          'page_heading': "i have 2 cats - nemo & cherrie",
      })
      return context

class aliens(BaseView):
  template_name = 'aliens.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context.update({
          'title': '[xfiles theme]',
          'page_heading': "the truth is out there",
      })
      return context

class ThemeView(BaseView):
  template_name = 'theme.html'

  def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      # Add additional context data if needed
      return context

  def post(self, request, *args, **kwargs):
      theme = request.POST.get('theme')
      response = HttpResponseRedirect(reverse('theme'))
      response.set_cookie('theme', theme)
      return response
