from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Hiarison Gigante', cpf='60211656321',
                    email='gigantedesousa@gmail.com', phone='21-99618-6180')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'gigantedesousa@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Hiarison Gigante',
            '60211656321',
            'gigantedesousa@gmail.com',
            '21-99618-6180'
        ]
        
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
