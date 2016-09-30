from datetime import datetime
from time import time

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.startTime = time()
        self.obj = Subscription(
            name='Ramiro Alvaro',
            cpf='12345678901',
            email='ramiroalvaro.ra@gmail.com',
            phone='31-991387178'
        )
        self.obj.save()

    def tearDown(self):
        delta = time() - self.startTime
        print("{:.3f}".format(delta))

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Ramiro Alvaro', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False."""
        self.assertEqual(False, self.obj.paid)
