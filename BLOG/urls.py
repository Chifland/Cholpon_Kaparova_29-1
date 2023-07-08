"""
URL configuration for BLOG project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from BLOG import settings
from posts.views import (
    MainPageCBV,
    ProductsCBV,
    CategoriesCBV,
    ProductDetailCBV,
    ProductCreateCBV,
    CategoryCreateCBV,
)

from users.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPageCBV.as_view()),
    path('products/', ProductsCBV.as_view()),
    path('categories/', CategoriesCBV.as_view()),
    path('products/<int:pk>/', ProductDetailCBV.as_view()),
    path('products/create/', ProductCreateCBV.as_view()),
    path('products/createcategory/', CategoryCreateCBV.as_view()),
    path('users/register/', register_view),
    path('users/login/', login_view),
    path('users/logout/', logout_view),

]

''' http://localhost:8000/hello/'''

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
