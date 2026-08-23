"""
URL configuration for config project.

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('tourism/', include(('tourism.urls', 'tourism'), namespace='tourism')),        # 👈 вот он namespace!
    path('consulting/', include(('consulting.urls', 'consulting'), namespace='consulting')),
    path('linguistics/', include(('linguistics.urls', 'linguistics'), namespace='linguistics')),
    path('about/', include(('about.urls', 'about'), namespace='about')),
    path('contacts/', include(('contacts.urls', 'contacts'), namespace='contacts')),
    path('cases/', include(('cases.urls', 'cases'), namespace='cases')),
    path('assistant/', include('assistant.urls')),
    # ... остальные по аналогии
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)