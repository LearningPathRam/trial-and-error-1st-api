"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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


from django.urls import path
from .views import luckynumber
from .views import luckynumber_form, result_page

urlpatterns = [
    path('', luckynumber_form, name='luckynumber_form'),
    path('luckynumber/', result_page, name='result_page'),
    # The following line is for direct access to the luckynumber function with a name parameter
    path('luckynumber/<str:name>/', luckynumber),
]
