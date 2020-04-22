from django.urls import path
from . import views 

app_name = "accounts"

urlpatterns = [

		path('', views.login_view, name = "accounts-login"),
		path('logout/', views.logout_view, name = "accounts-logout"),
		path('setup/', views.setup, name = "accounts-setup"),
		path('edit/', views.edit_profile, name = "accounts-edit"),
]