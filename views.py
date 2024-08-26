from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from .forms import SignUpForm

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
