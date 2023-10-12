from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('erpw.urls')),
    path('contacts/', include('contacts.urls'), name='contacts'),
    path('inventory/', include('inventory.urls')),
    path('orders/', include ('orders.urls'), name='orders'),
]

#, authentication_form=UserLoginForm