from django.http import HttpResponseRedirect
from django.views.generic import View, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from rules.contrib.views import PermissionRequiredMixin

from demo import forms
from demo import models


class HomeView(TemplateView):
    template_name = "demo/home.html"

    def get_context_data(self, **kwargs):
        di = super().get_context_data(**kwargs)
        di["products"] = models.Product.objects.all()
        di["domains"] = models.Domain.objects.all()
        return di


class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForm
    success_url = "/"
    permission_required = "product:create"


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


class SwitchDomainView(View):
    def get(self, *args, **kwargs):
        profile = self.request.user.userprofile
        profile.current_domain_id = kwargs["domain_id"]
        profile.save()
        return HttpResponseRedirect("/")
