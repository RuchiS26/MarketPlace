from django.urls import path
from . import views

app_name='marketplace'

urlpatterns=[
	path('', views.marketplace_index, name="marketplace-index" ),
	path('filters/', views.marketplace_filters, name="marketplace-filters" ),
	path('ad-search/', views.marketplace_ads_search, name="marketplace-ads-search" ),
	path('user/<str:user>/', views.marketplace_user, name="marketplace-user" ),
	path('user/<str:user>/notifications/', views.marketplace_user_notifications, name="marketplace-user-notifications" ),
	path('sell/', views.marketplace_sell, name="marketplace-sell"),
	path('ad/<str:slug>', views.marketplace_details, name="marketplace-details"),
	path('ad/<str:slug>/update/', views.marketplace_ad_update, name="marketplace-ad-update"),
	path('ad/<str:slug>/delete/', views.marketplace_ad_delete, name="marketplace-ad-delete"),
	path('ad/<str:slug>/delete/confirm/', views.marketplace_ad_delete_confirm, name="marketplace-ad-delete-confirm"),
	path('ad/<str:slug>/mark-sold/', views.marketplace_ad_mark_sold, name="marketplace-ad-mark-sold"),
	path('ad/<str:slug>/contact-seller/', views.marketplace_ad_contact_seller, name="marketplace-ad-contact-seller"),
]