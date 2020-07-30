from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[
    path('', views.index),
    path('blog/', views.blog),
    path('blog/<pk>',views.detailpost),
    path('blog/newpost/', views.newpost),
    path('blog/<pk>/delete/', views.remove_post),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)