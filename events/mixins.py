from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render

class AdminOrOrganizerOrParticipantRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True
            elif user.groups.filter(name__icontains='admin').exists():
                return True
            elif user.groups.filter(name__icontains='organizer').exists():
                return True
            if user.groups.filter(name__icontains='participant').exists():
                return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'no_permission.html')

class AdminOrOrganizerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True
            elif user.groups.filter(name__icontains='admin').exists():
                return True
            elif user.groups.filter(name__icontains='organizer').exists():
                return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'no_permission.html')

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True
            elif user.groups.filter(name__icontains='admin').exists():
                return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'no_permission.html')


class OrganizerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_superuser:
                return True
            elif user.groups.filter(name__icontains='organizer').exists():
                return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'no_permission.html')


class ParticipantRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name__icontains='participant').exists():
                return True
        return False

    def handle_no_permission(self):
        return render(self.request, 'no_permission.html')
