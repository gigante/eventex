from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Hiarison Gigante', cpf='12345678901',
                    email='exemplo@gmail.com', phone='+55 21 9900 9900')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'exemplo@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Hiarison Gigante',
            '12345678901',
            'exemplo@gmail.com',
            '+55 21 9900 9900'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
