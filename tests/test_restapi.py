import unittest

import requests

from apirestful.api import status


class TestRestApi(unittest.TestCase):
    """
    NB!
    To run these tests the service must be run  localhost at  port 5000
    """

    def test_get_wrong_api_query(self):
        r = requests.get('http://localhost:5000/qwer/1')
        assert r.status_code == status.HTTP_404_NOT_FOUND

    def test_get_ok_status(self):
        r = requests.get('http://localhost:5000/api/stats')
        assert r.status_code == status.HTTP_200_OK


