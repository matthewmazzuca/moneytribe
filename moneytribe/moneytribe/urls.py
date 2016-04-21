from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'moneytribe.views.home', name='home'),
    # url(r'^dev/$', 'newsletter.views.dev', name='dev'),

    # # url(r'^contact/$', 'newsletter.views.contact', namespace='contact'),
    # url(r'^about/$', 'protractr.views.about', name='about'),

    # url(r'^features/$', 'protractr.views.features', name='features'),
    # url(r'^pricing/$', 'protractr.views.pricing', name='features'),
    # # url(r'^blog/', include('blog.urls')),
    # url(r'^posts/', include("posts.urls", namespace='posts')),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',
    #                       {'next_page': '/'}),
    # url(r'^jobs/', include('jobs.urls')),
    # url(r'^userdata/', include('userdata.urls')),
    # url(r'^projects/', include("projects.urls", namespace='projects')),
    # url(r'^milestones/', include("milestones.urls", namespace='milestones')),
    # url(r'^chat/', include("chat.urls", namespace='chat')),
    # url(r'^files/', include("files.urls", namespace='files')),

    # url(r'^messages/', include('messages.urls', namespace='message', app_name='message')),

]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)