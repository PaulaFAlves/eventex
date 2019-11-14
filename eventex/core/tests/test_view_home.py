from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase): # TestCase já vem com o django, que extende o testcase do unittest que vem com python
	def setUp(self):
		self.response = self.client.get(r('home')) # / é a raiz do nosso site. client é um objeto dentro do testcase que 
		# vem com o django, capaz que realizar requisições contra o próprio django, sem passar pela infra da rede.

	def test_get(self):
		"""GET / must return status code 200"""
		self.assertEqual(200, self.response.status_code)

	def test_template(self):
		"""must use index.html"""
		self.assertTemplateUsed(self.response, 'index.html')

	def test_subscription_link(self):
		self.assertContains(self.response, 'href="/inscricao/"')

