"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

#실제 URL 패턴을 명시하는건 앱 폴더에 수동으로 urls.py를 생성
#해서 설정하고 config에 urls.py는 어떤 앱에 urls.py를
#참조할 것인지를 약간 상위 라우팅 개념?
# 아니다 root DNS 느낌이다.
from django.contrib import admin
from django.urls import path, include
from Board import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('MTV/', include('MTV.urls')),
    path('common/', include('common.urls')),
    path('Board/', include('Board.urls')),
    path('',views.BoardList.as_view(),name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
