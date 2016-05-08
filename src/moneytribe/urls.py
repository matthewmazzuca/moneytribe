from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'moneytribe.views.home', name='home'),
    url(r'^404/$', 'moneytribe.views._404', name='404'),

    url(r'^agents/$', 'moneytribe.views.agents', name='agents'),
    url(r'^blog-single/$', 'moneytribe.views.blog_single', name='blog-single'),
    url(r'^blog/$', 'moneytribe.views.blog', name='blog'),
    url(r'^car-insurance/$', 'moneytribe.views.car_insurance', name='car_insurance'),
    url(r'^claims/$', 'moneytribe.views.claims', name='claims'),
    url(r'^contact/$', 'moneytribe.views.contact', name='contact'),
    url(r'^get-a-car-insurance-quote/$', 'moneytribe.views.get_a_car_insurance_quote', name='get-a-car-insurance-quote'),
    url(r'^get-a-house-insurance-quote/$', 'moneytribe.views.get_a_house_insurance_quote', name='get-a-house-insurance-quote'),
    url(r'^get-a-life-insurance-quote/$', 'moneytribe.views.get_a_life_insurance_quote', name='get-a-life-insurance-quote'),
    url(r'^get-a-travel-insurance-quote/$', 'moneytribe.views.get_a_travel_insurance_quote', name='get-a-travel-insurance-quote'),
    url(r'^house-insurance/$', 'moneytribe.views.house_insurance', name='house-insurance'),
    url(r'^life-insurance/$', 'moneytribe.views.life_insurance', name='life-insurance'),
    url(r'^travel-insurance/$', 'moneytribe.views.travel_insurance', name='travel-insurance'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),

    # while logged in

    url(r'^profile/$', 'moneytribe.views.profile', name='profile'),
    url(r'^usersettings/$', 'moneytribe.views.usersettings', name='usersettings'),
    url(r'^messages/$', 'moneytribe.views.messages', name='messages'),
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