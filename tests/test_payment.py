import unittest
from app import app, db, Payment
from config import Config

class PaymentTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config.from_object(Config)
        self.client = app.test_client()

        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_payment(self):
        response = self.client.post('/payments', json={
            'user_id': 1,
            'amount': 100.0,
            'status': 'pending'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Payment created', response.data)

    def test_create_payment_missing_field(self):
        response = self.client.post('/payments', json={
            'user_id': 1,
            'amount': 100.0
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
