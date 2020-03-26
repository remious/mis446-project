from django.urls import path
from django.contrib.auth import views as auth_views
from . import views 
from users import views as user_views
from .views import PostListView, SupplierView, MenuView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='mis446/login.html'), name='ACRMS-Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mis446/logout.html'), name='ACRMS-Logout'),
    path('register/', user_views.register, name="Register"),
    path('home/', views.home, name='ACRMS-Home'),
    path('checkout/', views.checkout, name='Checkout'),
    path('confirmation/', views.confirmation, name='Confirmation'),
    path('edit-menu/', MenuView.as_view(), name='Edit Menu'),
    path('edit-suppliers/', SupplierView.as_view(), name='Edit Suppliers'),
    path('edit-inventory/', PostListView.as_view(), name='Edit Inventory'),
     path('user-manual/', views.user_manual, name='User Manual'),
      path('admin-manual/', views.admin_manual, name='Admin Manual'),
]
