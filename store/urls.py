from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('store/', views.store, name='pharmacy'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_info/', views.update_info, name='update_info'),
    path('product/<int:pk>/', views.product, name='product'),
    path('product/<int:pk>/', views.product, name='product'),
    path('product/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

# URL pattern for the store application's home page
