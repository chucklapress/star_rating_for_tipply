from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView
from app.models import Book

# Create your views here.
class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            return render(request, "user_create_view.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create_view.html", {"form": form})

class IndexView(ListView):
    template_name = 'index.html'
    model = Book

    def get_queryset(self):
        return Book.objects.all()

from django.contrib.auth.mixins import LoginRequiredMixin
class BookCreateView(CreateView):
    login_url = "/login/"
    model = Book
    fields = ['title','author','genre','cost']
    success_url = '/'
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(BookCreateView, self).form_valid(form)
