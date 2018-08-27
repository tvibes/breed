from django.conf.urls import url
from  django.contrib import admin
from accounts.views import login_view, signup_view, logout_view
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm

urlpatterns = [
    url('^signup/$', accounts_views.signup_view, name='signup'),
    url('^profile/$', accounts_views.profile, name='profile'),
    url('^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url('^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login', kwargs={"authentication_form":UserLoginForm}),
    url(r'^reset_password/$',
        auth_views.PasswordResetView.as_view(
            template_name='accounts/reset_password.html',
            email_template_name='accounts/password_reset_email.html',
            subject_template_name='accounts/reset_password_subject.txt',
        ),
        name='reset_password'
        ),
    url('^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='accounts/reset_password_done.html'),
        name='reset_password_done'
        ),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
       auth_views.PasswordResetConfirmView.as_view(
           template_name='accounts/reset_password_confirm.html'),
       name='password_reset_confirm'),
    url(r'^reset_complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/reset_password_complete.html'),
        ),
]
