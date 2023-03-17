from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
path('', HomeView.as_view(), name='home'),
path('category/<slug>', CategoryView.as_view(), name='category'),
path('detail/<slug>', DetailView.as_view(), name='detail'),
path('search', SearchView.as_view(), name='search'),
path('signup', signup, name='signup'),
path('cart', CartView.as_view(), name='cart'),
path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
path('delete_cart/<slug>', delete_cart, name='delete_cart'),
path('reduce_cart/<slug>', reduce_cart, name='reduce_cart'),
path('review/<slug>', review, name='review'),
path('contact', contact, name='contact'),
path('reset_password/',
 auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name='reset_password'),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='reset_password_done'),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view, name='password_reset_confirm'),
path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view, name='password_reset_complete'),

]