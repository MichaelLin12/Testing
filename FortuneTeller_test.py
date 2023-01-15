import unittest
from unittest.mock import patch, MagicMock
import FortuneTeller as ft

class TestFortuneTeller(unittest.TestCase):

    def setUp(self) -> None:
        self.oracle = ft.Oracle()
        return super().setUp()

    def test_synthesizeQuestion(self):
        actual = '   8932Will *8I succeed in life? '
        expected = 'will+i+succeed+in+life'
        self.assertEquals(self.oracle.synthesizeQuestion(actual),expected,'SynthesizeQuestion did not properly synthesize')

    @patch('FortuneTeller.requests')
    def test_predictFuture(self,mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'reading':'Yes'}
        
        
        mock_requests.get.return_value = mock_response
        self.assertEqual(self.oracle.predictFuture("Will I win the Lottery?"),"Yes")

if __name__ == '__main__':
    unittest.main()