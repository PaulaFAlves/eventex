from django.shortcuts import render
from eventex.subscription.forms import SubscriptionForm
from django.http import HttpResponseRedirect, Http404
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings
from django.shortcuts import resolve_url as r
from eventex.subscription.models import Subscription


def new(request):
	if request.method == 'POST':
		return create(request)
	
	return empty_form(request)


def empty_form(request):
	return render(request, 'subscription/subscription_form.html', 
					{'form': SubscriptionForm()})


def create(request):
	form = SubscriptionForm(request.POST)

	if 	not form.is_valid():
		return render(request, 'subscription/subscription_form.html', 
						{'form': form})

	subscription = form.save()

	_send_mail('Confirmação de inscrição', 
				settings.DEFAULT_FROM_EMAIL, 
				subscription.email, 
				'subscription/subscription_email.txt',
				{'subscription': subscription})

		
	return HttpResponseRedirect(r('subscription:detail', subscription.pk))
	



def detail(request, pk):
	try:
		subscription = Subscription.objects.get(pk=pk)
	except Subscription.DoesNotExist:
		raise Http404
		
	return render(request, 'subscription/subscription_detail.html',
					{'subscription': subscription})



def _send_mail(subject, from_, to, template_name, context):
	body = render_to_string(template_name, context)
	mail.send_mail(	subject, body, from_, [from_, to])


