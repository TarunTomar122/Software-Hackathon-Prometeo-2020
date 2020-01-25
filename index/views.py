from django.shortcuts import render, redirect
from django.shortcuts import redirect,get_object_or_404
from django.views.generic import CreateView, ListView
from .models import User, Article
from django.views.generic import CreateView, ListView,View
from .forms import DoctorSignupForm, DoctorDetailForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    return render(request, 'home.html')


class SignupView(CreateView):
    model = User
    form_class = DoctorSignupForm
    template_name = 'signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile', self.request.user.id)


@login_required
def profile(request, pk):
    if request.method == 'POST':
        u_form = DoctorDetailForm(
            request.POST, request.FILES, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile', pk)

    else:
        u_form = DoctorDetailForm(instance=request.user)

    context = {
        'form': u_form
    }
    return render(request, 'profile.html', context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'image', 'body', 'date']
    template_name = 'create_article.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticlesListView(ListView):
    model = Article
    template_name = 'listarticles.html'
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10

class ShowDoctors(ListView):
    model = User
    template_name = 'listdoctors.html'
    context_object_name = 'doctors'
    paginate_by = 10

class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Article, pk=kwargs['pk'])
        context = {'post': post}
        return render(request, "article.html", context)

class DoctorDetailView(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(User, pk=kwargs['pk'])
        context = {'post': post}
        return render(request, "doctor.html", context)        

def MapView(request):
    return render(request,'maps.html')