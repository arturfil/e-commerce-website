from django.contrib import admin
from django.urls import path, include
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    path('shop/',include('shop.urls')),
    path('search/', include('search_app.urls')),
    path('cart/', include('cart.urls')),
    path('order/', include('order.urls')),
    path('account/create/', views.signUpView, name="signup"),
    path('account/login/', views.signInView, name="signin"),
    path('account/logout/', views.signOutView, name="signout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)