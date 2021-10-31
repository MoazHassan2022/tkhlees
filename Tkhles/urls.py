from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from . import views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.policies, name="policies"),
    path("add", views.add, name="add"),
    path("addCreditor", views.addCreditor, name="addCreditor"),
    path("addDebtor", views.addDebtor, name="addDebtor"),
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)