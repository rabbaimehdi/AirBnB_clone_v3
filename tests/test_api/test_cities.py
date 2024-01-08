#!/usr/bin/python3
from api.v1.app import app as app
from flask import Flask, make_response, jsonify, json
import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "Testing FileStorage")
class FlaskTestCase(unittest.TestCase):
    data = {"name": "California"}

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.app = app

    def test_post_method(self):
        tester = app.test_client(self)
        response = tester.post('/api/v1/states', json=self.data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 201)
