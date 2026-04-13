from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Post
from .forms import UploadForm


class IndexView(ListView):
    model = Post
    template_name = 'gallery/index.html'
    context_object_name = 'posts'
    paginate_by = 6


class ImageUploadView(CreateView):
    model = Post
    form_class = UploadForm
    template_name = 'gallery/upload.html'
    success_url = reverse_lazy('gallery:success')


class SuccessView(TemplateView):
    template_name = 'gallery/success.html'
