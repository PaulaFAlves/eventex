from django.test import TestCase
from eventex.subscription.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):
	def setUp(self):
		self.form = SubscriptionForm()

	def test_form_has_field(self):
		"""Form must have 4 fields."""
		expected = ['name', 'cpf', 'email', 'phone']
		self.assertSequenceEqual(expected, list(self.form.fields))