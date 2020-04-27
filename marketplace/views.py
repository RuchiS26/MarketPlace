from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Advert, Notify
from .forms import AdForm

@login_required(login_url = 'accounts:accounts-login')
def marketplace_index(request):
	ads = Advert.objects.filter(sold = False).order_by('date_posted')
	user = request.user
	ads_count = Advert.objects.filter(user = user).count()
	return render(request, 'marketplace/marketplace-index.html', {'ads':ads,'user':user,'ads_count':ads_count})

@login_required(login_url = 'accounts:accounts-login')
def marketplace_filters(request):
	query = request.GET.get('filter',None)
	tag_undefined = False
	if(query == 'All'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).order_by('date_posted')
	elif(query == 'Other Electronics'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'Laptops'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'PC'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'Tablets'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'Mobiles'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'Clothes'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'Automotives'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	elif(query == 'Furniture'):
		filter_type = query
		ads = Advert.objects.filter(sold = False).filter(tags = filter_type).order_by('date_posted')
	else:
		tag_undefined = True

	return render(request, 'marketplace/marketplace-filter.html', {'tag_undefined':tag_undefined,'filter_type':filter_type,'ads':ads})

@login_required(login_url = 'accounts:accounts-login')
def marketplace_ads_search(request):
	query = request.GET.get('query',None)
	ads = Advert.objects.filter(Q(title__icontains=query) | Q(product__icontains=query) | Q(tags__icontains=query))

	return render(request,'marketplace/marketplace-ads-search.html',{'query':query,'ads':ads})

@login_required(login_url = 'accounts:accounts-login')
def marketplace_user(request,user):
	user = User.objects.get(username = user)
	ads = Advert.objects.filter(user = user)
	ads_count = Advert.objects.filter(user = user).count()
	return render(request, 'marketplace/marketplace-user.html', {'ads':ads,'user':user,'ads_count':ads_count})

@login_required(login_url = 'accounts:accounts-login')
def marketplace_sell(request):

	if request.method == 'POST':

		adForm = AdForm(request.POST,request.FILES)
	
		if(adForm.is_valid()):
			instance = adForm.save(commit = False)
			slug = str(instance.title) + str(Advert.objects.all().count())
			instance.user = request.user
			instance.slug = slug
			instance.save()

		return redirect('marketplace:marketplace-index')

	else:
		adForm = AdForm()
	
	return render(request, 'marketplace/marketplace-sell.html', {'adForm':adForm})


@login_required(login_url = 'accounts:accounts-login')
def marketplace_details(request,slug):
	ad = Advert.objects.get(slug = slug)
	return render(request,'marketplace/marketplace-details.html',{'ad':ad})

@login_required(login_url = 'accounts:accounts-login')
def marketplace_ad_update(request,slug):
	ad = Advert.objects.get(slug = slug)
	if(ad.user != request.user):
		messages.danger(request,f'Illegal Action!')
		return redirect('marketplace:marketplace-index')

	else:
		if(request.method == 'POST'):
			adForm = AdForm(request.POST, request.FILES, instance = ad)
			if(adForm.is_valid()):
				adForm.save()

			return redirect('marketplace:marketplace-details', slug = slug)

		else:
			adForm = AdForm(instance = ad)

	return render(request, 'marketplace/marketplace-ad-update.html',{'adForm':adForm,'ad':ad})


@login_required(login_url = 'accounts:accounts-login')
def marketplace_ad_delete_confirm(request,slug):
	ad = Advert.objects.get(slug = slug)
	if(ad.user != request.user):
		messages.danger(request,f'Illegal Action!')
		return redirect('marketplace:marketplace-index')

	else:
		return render(request,'marketplace/marketplace-ad-delete-confirm.html',{'ad':ad})

@login_required(login_url = 'accounts:accounts-login')
def marketplace_ad_delete(request,slug):
	ad = Advert.objects.get(slug = slug)
	if(ad.user != request.user):
		messages.danger(request,f'Illegal Action!')

	else:
		Advert.objects.filter(slug = slug).delete()
		messages.success(request,f'Ad Deleted')


	return redirect('marketplace:marketplace-index')

@login_required(login_url = 'accounts:accounts-login')
def marketplace_ad_mark_sold(request,slug):
	ad = Advert.objects.get(slug = slug)
	if(ad.user != request.user):
		messages.danger(request,f'Illegal Action!')

	elif(ad.sold == True):
		messages.success(request,f'Product already sold!')

	else:
		ad.sold = True;
		ad.save()

		Notify.objects.filter(product = ad).delete()

		messages.success(request,f'Product marked as sold!')

	return redirect('marketplace:marketplace-index')

@login_required(login_url = 'accounts:accounts-login')
def marketplace_ad_contact_seller(request,slug):
	ad = Advert.objects.get(slug = slug)
	if(ad.user == request.user):
		messages.danger(request,f'Illegal Action!')

	else:
		seller = User.objects.get(username = ad.user)
		user = request.user
		ads = Advert.objects.filter(user = seller)
		Notify.objects.create(user = seller, buyer = user, product = ad)
		messages.success(request,f'Seller Notified about your interest!')
		return render(request,'marketplace/marketplace-user.html',{'user':seller,'ads':ads})


@login_required(login_url = 'accounts:accounts-login')
def marketplace_user_notifications(request,user):
	ads_count = Advert.objects.filter(user = request.user).count()
	notifications = Notify.objects.filter(user = request.user).order_by('id')

	return render(request, 'marketplace/marketplace-user-notifications.html',{'notifications':notifications,'ads_count':ads_count})
