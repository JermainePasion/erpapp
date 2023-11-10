from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from users.views import register
from inventory.views import dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('', include('erpw.urls')),
    path('contacts/', include('contacts.urls'), name='contacts'),
    path('inventory/', include('inventory.urls')),
    path('invoice/', include ('invoice.urls'), name='invoice'),
    path('orders/', include ('orders.urls'), name='orders'),
    path("dashboard/",dashboard, name = "dashboard"),
]


if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#, authentication_form=UserLoginForm