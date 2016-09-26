from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_form_has_fields(self):
        """Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='abcd5678901')
        # self.assertFormErrorMessage(form, 'cpf', 'CPF deve conter apenas números.')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits."""
        form = self.make_validated_form(cpf='12345')
        # self.assertFormErrorMessage(form, 'cpf', 'CPF deve ter 11 números.')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_capitalized(self):
        """Name must be capitalized."""
        form = self.make_validated_form(name='RAMIRO alvaro')
        self.assertEqual('Ramiro Alvaro', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email and phone are optional, but one must be informed."""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_regression_invalid_email_and_not_phone(self):
        data = dict(name='Ramiro Alvaro', cpf='12345678901', email='ramiroalvaro.ra@gmail.com', phone='31-991387178')
        data['email'] = 'asdf'
        del data['phone']
        form = SubscriptionForm(data)
        self.assertEqual(False, form.is_valid())

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Ramiro Alvaro', cpf='12345678901', email='ramiroalvaro.ra@gmail.com', phone='31-991387178')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
