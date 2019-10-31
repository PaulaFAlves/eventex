from django.test import TestCase
from eventex.subscription.models import Subscription
from datetime import datetime


class SubscriptionModelTest(TestCase):
	def setUp(self):
		self.obj = Subscription(
			name='Henrique Bastos',
			cpf='12345678901',
			email='henrique@bastos.net',
			phone='21-232323233'
			)
		self.obj.save()
	
	def test_create(self):
		self.assertTrue(Subscription.objects.exists())		

	def test_created_at(self):
		"""Subscription must have an auto created_at attr."""
		self.assertIsInstance(self.obj.created_at, datetime)
