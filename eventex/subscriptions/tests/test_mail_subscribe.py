from time import time

from django.core import mail

from django.shortcuts import resolve_url as r
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        self.startTime = time()
        data = dict(name='Ramiro Alvaro', cpf='12345678901', email='ramiroalvaro.ra@gmail.com', phone='31-991387178')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def tearDown(self):
        delta = time() - self.startTime
        print("{:.3f}".format(delta))

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'ramiroalvaro.ra@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Ramiro Alvaro',
            '12345678901',
            'ramiroalvaro.ra@gmail.com',
            '31-991387178',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
