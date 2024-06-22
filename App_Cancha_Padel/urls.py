from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('pages/', views.pages_list_view, name='pages_list'),
    path('pages/<int:page_id>/', views.page_detail_view, name='page_detail'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup_view, name='signup'),
    path('accounts/profile/', views.profile_view, name='profile'),
    ]