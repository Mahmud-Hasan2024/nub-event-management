from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from users.forms import CreateUserForm, CustomLoginForm, CustomPasswordChangeForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import Group
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView
from users.forms import CustomLoginForm
from django.views.generic import DetailView, UpdateView
from users.forms import EditProfileForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your views here.
User = get_user_model()

def get_user_role(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.groups.filter(name='admin').exists():
            return 'admin'
        elif request.user.groups.filter(name='organizer').exists():
            return 'organizer'
        elif request.user.groups.filter(name='participant').exists():
            return 'participant'
    return None

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()

            participant_group, created = Group.objects.get_or_create(name='participant')
            user.groups.add(participant_group)

            messages.success(request, 'A Confirmation mail sent. Please check your email')
            return redirect('login')

    context = {'form' : form}
    return render(request, 'registration/register.html', context)

class CustomLoginView(LoginView):
    form_class = CustomLoginForm

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        return next_url if next_url else super().get_success_url()



def activate_user(request, user_id, token):
    user = User.objects.get(pk=user_id)
    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account has been activated. You can now log in.")
        return redirect('login')
    else:
        return render(request, 'registration/activation_invalid.html')


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = get_user_role(self.request)
        return context


class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'edit_profile.html'
    context_object_name = 'form'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        return redirect('profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = get_user_role(self.request)
        return context


class ChangePassword(PasswordChangeView):
    template_name = 'change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was changed successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = get_user_role(self.request)
        return context
    

class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'change_password_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = get_user_role(self.request)
        return context



class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'reset_password.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['protocol'] = 'https' if self.request.is_secure() else 'http'
        context['domain'] = self.request.get_host()
        context['user_role'] = get_user_role(self.request)
        return context

    def form_valid(self, form):
        messages.success(self.request, 'A reset email has been sent. Please check your email.')
        return super().form_valid(form)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'reset_confirm.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Password reset successfully.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_role'] = get_user_role(self.request)
        return context
