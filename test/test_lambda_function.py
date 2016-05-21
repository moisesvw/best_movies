from test_helper import *
from lambda_function import *

class TestLambdaFunction(unittest.TestCase):

  def test_help_intent(self):
    event = fixtures.FIXTURES["help_intent_after_open_app"]
    result = lambda_handler(event, None)
    self.assertTrue('In Best Movies' in result['response']['outputSpeech']['text'])

  def test_stop_intent(self):
    event = fixtures.FIXTURES["stop_intent_after_open_app"]
    result = lambda_handler(event, None)
    expected = "Best Movies will stop, do you really want to"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])
    event = fixtures.FIXTURES["stop_none_session"]
    result = lambda_handler(event, None)
    expected = "Best Movies will stop, do you really want to"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

  def test_cancel_intent(self):
    event = fixtures.FIXTURES["cancel_after_open_app"]
    result = lambda_handler(event, None)
    expected = "Best Movies will stop, do you really want to"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

  def test_yes_after_cancel_intent(self):
    event = fixtures.FIXTURES["yes_intent_without_info"]
    result = lambda_handler(event, None)
    expected = "Goodbye"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

    event = fixtures.FIXTURES["yes_intent_with_info"]
    result = lambda_handler(event, None)
    expected = "Goodbye"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

  def test_initial_intent(self):
    event = fixtures.FIXTURES["initial_request"]
    result = lambda_handler(event, None)

    expected = "Welcome to Best Movies, you can find movies just said as follow:"
    # pdb.set_trace()
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

  def test_read_all_intent(self):
    event = fixtures.FIXTURES["read_all"]
    result = lambda_handler(event, None)
    # pdb.set_trace()
    expected = "The title is Room With a View. Summary"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

    event2 = fixtures.FIXTURES["read_all_error"]
    result2 = lambda_handler(event2, None)

    # pdb.set_trace()
    expected = "In Best Movies You will find movies from"
    self.assertTrue(expected in result2['response']['outputSpeech']['text'])

  def test_should_end_session_bad_call(self):
    event = fixtures.FIXTURES["should_end_session_bad_call"]
    result = lambda_handler(event, None)

    expected = "I don't "
    # pdb.set_trace()
    self.assertTrue(expected in result['response']['outputSpeech']['text'])
    self.assertTrue(result['response']['shouldEndSession'])


  def test_read_all_error_reported(self):
    event = fixtures.FIXTURES["read_all_error_reported"]
    result = lambda_handler(event, None)
    # pdb.set_trace()
    expected = "In Best Movies You will find movies from 1930"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

  def test_query_movies_1962(self):
    event = fixtures.FIXTURES["query_movies_1962"]
    result = lambda_handler(event, None)

    expected = "There is only 1 movie,"
    self.assertTrue(expected in result['response']['outputSpeech']['text'])


  def test_query_movies_1935_only_return_one_result(self):
    event = fixtures.FIXTURES["query_movies_1935"]
    result = lambda_handler(event, None)

    expected = "There is only 1 movie, The title is Bride of Frankenstein."
    # pdb.set_trace()
    self.assertTrue(expected in result['response']['outputSpeech']['text'])

  def test_query_movies_1965_read_first_and_last(self):
    event = fixtures.FIXTURES["read_first_1965"]
    result = lambda_handler(event, None)
    expected = "The title is Dr Zhivago. Summary: The life of a Russian physician and poet who, although married to another, falls in love with a political activist's wife and experiences hardship during the First World War and then the October Revolution.. Publication Date: 1965. Actors: Geraldine Chaplin, Julie Christie, Omar Sharif. Country: USA ."

    response = result['response']['outputSpeech']['text']

    self.assertTrue(response == expected)

    event = fixtures.FIXTURES["read_last_1965"]
    result = lambda_handler(event, None)
    expected = "The title is Alphaville. Summary: A U.S. secret agent is sent to the distant space city of Alphaville where he must find a missing person and free the city from its tyrannical ruler.. Publication Date: 1965. Actors: Anna Karina, Eddie Constantine. Country: France ."
    response = result['response']['outputSpeech']['text']

    self.assertTrue(response == expected)



