from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import Task


class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo-list')

    def get_success_url(self):
        return self.success_url or self.get_redirect_url()


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class TodoListView(ListView):
    model = Task
    template_name = 'todo_list.html'
    context_object_name = 'tasks'
