from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
import json

class NumberToEnglishTest(TestCase):

    def setUp(self):
        self.client = Client()
        with open('config.json') as config_file:
            self.cfg = json.load(config_file)

    def test_valid_get_request(self):
        url = reverse('num_to_english')  
        response = self.client.get(url, {'number': '123.45'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(data['num_in_english'], 'One hundred twenty three point four five')

    def test_valid_post_request(self):
        url = reverse('num_to_english')  
        data = {'number': '456.78'}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(data['num_in_english'], 'Four hundred fifty six point seven eight')

    def test_invalid_number_format(self):
        url = reverse('num_to_english') 
        response = self.client.get(url, {'number': 'abc'})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Invalid number format')

    def test_number_out_of_range(self):
        url = reverse('num_to_english')
        response = self.client.post(url, json.dumps({'number': '1000000000000001'}), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['status'], 'error')
        min = str(self.cfg['min_number'])
        max = str(self.cfg['max_number'])
        msg = 'Number out of range, valid range is (' + min + ',' + max + ')'
        self.assertEqual(data['message'], msg)
