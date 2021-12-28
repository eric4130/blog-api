
from django.contrib import admin
from django.urls import path, include
admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('api/v1/', include('djoser.urls')),
    # path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('blog_entries.urls')),

]
