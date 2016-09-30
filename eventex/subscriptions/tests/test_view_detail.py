from time import time

from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.startTime = time()
        self.obj = Subscription.objects.create(
            name='Ramiro Alvaro',
            cpf='12345678901',
            email='ramiroalvaro.ra@gmail.com',
            phone='31-991387178'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def tearDown(self):
        delta = time() - self.startTime
        print("{:.3f}".format(delta))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def setUp(self):
        self.startTime = time()

    def tearDown(self):
        delta = time() - self.startTime
        print("{:.3f}".format(delta))

    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', '00000000-0000-0000-0000-000000000000'))
        self.assertEqual(404, resp.status_code)
