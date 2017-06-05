from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^People/(?P<pk>[\-\w]+)/$', core_views.user_profile, 
        name='user_profile'),
    url(r'^People/(?P<pk>[\-\w]+)/edit/$', core_views.edit_user, 
        name='user_edit'),
    url(r'^Consultations/$', core_views.consults, name='consults'),
    url(r'^Consultations/new/$', core_views.consult_new, name='consult_new'),
    url(r'^Consultations/(?P<pk>[0-9]+)/$', core_views.consult_detail, name='consult_detail'),
    url(r'^Consultations/(?P<pk>[0-9]+)/edit/$', core_views.consult_edit, name='consult_edit'),
    url(r'^Species/$', core_views.species, name='species'),
    url(r'^Places/$', core_views.places, name='places'),
    url(r'^People/$', core_views.people, name='people'),
    url(r'^About/$', core_views.about, name='about'),
    url(r'^Login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^Logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^Signup/$', core_views.signup, name='signup'),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^uploads/form/$', core_views.consult_new, name='model_form_upload'),
    # url(r'^draceditor/', include('draceditor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)