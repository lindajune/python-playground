# You only want to mock an object for a part of the test scope
# You are already using too many decorators or parameters, which hurts your test’s readability.

import unittest
from unittest.mock import patch

from requests.exceptions import Timeout

import learn_unittest_mock.learn_mock


class PatchContextManagerTest(unittest.TestCase):
    def test_context_manager(self):
        with patch('learn_unittest_mock.learn_mock.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                learn_unittest_mock.learn_mock.get_holidays()

            mock_requests.get.asser_called_once()


if __name__ == '__main__':
    unittest.main()
