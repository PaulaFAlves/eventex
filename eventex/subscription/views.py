from django.shortcuts import render
from eventex.subscription.forms import SubscriptionForm


def subscribe(request):
	context = {'form': SubscriptionForm()}
	return render(request, 'subscription/subscription_form.html', context)