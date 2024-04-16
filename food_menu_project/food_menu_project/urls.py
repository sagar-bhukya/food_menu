"""
URL configuration for food_menu_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include



#login functionality is going to use an inbuilt view from django
from users import views as user_views
from django.contrib.auth import views as authentication_view


from users.views import login_user,register,logout_user,profilepage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('food.urls')),

    #from users to register form
    path('register/',register,name="register"),

    #for login and logout
    # path('login/',authentication_view.LoginView.as_view(template_name="users/login.html"),name='login'),# after running registration/login.html so i have to users/login.html
    # path('logout/',authentication_view.LogoutView.as_view(template_name="users/logout.html"),name='logout'),

    path('login/',login_user, name='login'),
    path('logout/',logout_user, name='logout'),

    #profile 
    path('profile/',profilepage,name="profile"),

]
urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)