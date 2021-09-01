from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from demo import forms
from demo import models


class HomeView(TemplateView):
    template_name = "demo/home.html"

    def get_context_data(self, **kwargs):
        di = super().get_context_data(**kwargs)
        di["products"] = models.Product.objects.all()
        return di


class ProductCreateView(CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = "/"


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = "/"
    permission_required = "products.change_product"


class ProductDetailView(DetailView):
    model = models.Product

    def get_context_data(self, **kwargs):
        di = super().get_context_data(**kwargs)
        return di
