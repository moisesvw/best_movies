from test_helper import *
from dialogs import *

class TestDialogs(unittest.TestCase):

  def test_get_thousand_movies_emtpy_session_empty_event(self):
    event = fixtures.FIXTURES["query_movies_two_dates_event"]
    result = get_best_thousand_movies(event['request']['intent'], event['session'])
    self.assertTrue('found' in result['response']['outputSpeech']['text'])

  def test_read_two_movies_event(self):
    event = fixtures.FIXTURES["read_two_movies_event"]
    result = read_n_or_all(event['request']['intent'], event['session'])
    self.assertTrue('Summary' in result['response']['outputSpeech']['text'])
    self.assertTrue(result['response']['shouldEndSession'])

  def test_read_all_movies_event(self):
    event = fixtures.FIXTURES["read_all_movies_event"]
    result = read_n_or_all(event['request']['intent'], event['session'])

    self.assertTrue('Summary' in result['response']['outputSpeech']['text'])
    self.assertTrue(result['response']['shouldEndSession'])
