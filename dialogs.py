import movies

""" Here is generated the dialogue which will use alexa to response  """


DB = movies.Movies()

def get_welcome_response():

    session_attributes = {}
    card_title = "Welcome to Best Movies"
    speech_output = "Welcome to Best Movies, you can find movies just said as follow: " \
                    "search movies between nineteen sixty five and nineteen eighty five. Or " \
                    "search movies for nineteen eighty five. What do you want to search"

    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_help_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Best Movies Help"

    speech_output = "In Best Movies You will find movies from 1930 and onwards. " \
    "you can hear the title, capsule review and publication date. You can use this app by saying:  " \
    "search movies between nineteen sixty five and nineteen eighty five. Or " \
    "search movies for nineteen eighty five. what you want to search"

                    
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_cancel_response(intent, session):
    session_attributes = session.get('attributes', { })
    session_attributes = {} if session_attributes == None else session_attributes
    session_attributes["last_last_intent"] = session_attributes.get("last_intent", None)
    card_title = "Best Movies will stop, do you really want to ?"
    speech_output = "Best Movies will stop, do you really want to"

    reprompt_text = speech_output
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def yes_response(intent, session):
    session_attributes = {}
    should_end_session = True
    card_title = "Goodbye"
    speech_output = ""
    intent_name = session_attributes.get("last_intent", None)

    if  intent_name == "AMAZON.StopIntent" or intent_name == "AMAZON.CancelIntent":
        speech_output = "Goodbye"
    else:
        speech_output = "Thank you, Goodbye"

    reprompt_text = speech_output
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def not_response(intent, session):
    session_attributes = {}
    should_end_session = True
    card_title = "Resuming Best Movies!"
    speech_output = "Resuming Best Movies"
    intent_name = session_attributes.get("last_last_intent", None)

    if intent_name == "BestMoviesIntentRead":
        session['attributes']['last_intent'] = 'BestMoviesIntent'
        session['attributes']['publication_date_one'] = session_attributes.get('publication_date_one', None)
        session['attributes']['publication_date_two'] = session_attributes.get('publication_date_two', None)

        intent['slots']['ReadOrder'] = session_attributes.get('ReadOrder', None)
        read_n = intent['slots']['ReadN'] = session_attributes.get('ReadN', None)

        response = read_n_or_all(intent, session)
    elif intent_name == "BestMoviesIntentRead":
        intent['slots']['publication_date_one'] = {
            "name": "PublicationDateRangeOne",
            "value": session_attributes.get('publication_date_one', None)
          }

        intent['slots']['publication_date_two'] = {
            "name": "PublicationDateRangeTwo",
            "value": session_attributes.get('publication_date_two', None)
          }

        response = get_best_thousand_movies(intent, session)
    else:
        response = get_welcome_response()

    return response

def get_best_thousand_movies(intent, session):
    """ gets the movies due dates.
    """

    card_title = "Querying movies."
    session_attributes = {}
    should_end_session = True

    if 'PublicationDateRangeOne' in intent['slots'] or 'PublicationDateRangeTwo' in intent['slots']:
        publication_date_one = intent['slots'].get('PublicationDateRangeOne', {}).get('value', None)
        publication_date_two = intent['slots'].get('PublicationDateRangeTwo', {}).get('value', None)

        movies = DB.thousand_best_movies(publication_date_one=publication_date_one, publication_date_two=publication_date_two)

        num_movies = len(movies)
        print '#num movies', str(num_movies), '\n'

        if num_movies == 1:
            row = movies[0]
            speech_output = "There is only 1 movie, " + movie(row) + "."
            reprompt_text = movie(row)
            should_end_session = True
        elif num_movies > 0 :
          should_end_session = False
          speech_output = "I found  " + \
                          str(num_movies) + \
                          "  Movies in DataBase. You can ask me how to read them by saying, " \
                          "Read first two, or Read last Ten, or Read All."
          reprompt_text = "You can ask me how to read them by saying, " \
                          "Read first two, or Read last Ten, or Read All."
          session_attributes = {
            'publication_date_one': publication_date_one,
            'publication_date_two': publication_date_two,
            'last_intent': 'BestMoviesIntent'
            }
        else:
          speech_output = not_found_movies(publication_date_one, publication_date_two)
          reprompt_text = not_found_movies(publication_date_one, publication_date_two)
    else:
        speech_output = "I'm not sure what years are you trying to query." \
                        "You can tell me your which years you want by saying, " \
                        "what are the best movies between 1995 and 1996."
        reprompt_text = "I'm not sure what years are you trying to query." \
                        "You can tell me your which years you want by saying, " \
                        "what are the best movies between 1995 and 1996."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def read_n_or_all(intent, session):
    card_title = "Reading movies."
    session_attributes = {}
    should_end_session = True

    if session.get('attributes', {}) != None and "last_intent" in session.get('attributes', {}):
        if session['attributes']['last_intent'] == 'BestMoviesIntent':
            publication_date_one = session['attributes'].get('publication_date_one', None)
            publication_date_two = session['attributes'].get('publication_date_two', None)

            read_order = intent['slots'].get('ReadOrder', {}).get('value', None)
            read_n = intent['slots'].get('ReadN', {}).get('value', None)

            movies = DB.thousand_best_movies(publication_date_one=publication_date_one, publication_date_two=publication_date_two)
            movies = map(movie, movies)
            num_movies = len(movies)

            if num_movies > 0 and read_order != None: 
                speech_output = speak_n(data=movies, order=read_order, read_n=read_n)
                reprompt_text = "You can tell me which years you want by saying, " \
                                "what are the best movies between 1995 and 1996."
            else:
                speech_output = not_found_movies(publication_date_one, publication_date_two)
                reprompt_text = not_found_movies(publication_date_one, publication_date_two)
        else:
            return get_help_response()

    else:
        return get_help_response()


    speech_l = build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
    response = build_response(session_attributes, speech_l)

    return response

def not_found_movies(yearone, yeartwo):
    given_year = {
        "?": "given year",
        "False": "given year",
        False: "given year",
    }
    text = ""
    if yearone != None and yeartwo != None:
        text = "I don't have rated movies for range " + str(yearone) + " and " + str(yeartwo)
    elif yearone != None and yeartwo == None:
        text = "I don't have rated movies for " + given_year.get(str(yearone).isdigit(), str(yearone))
    elif yearone == None and yeartwo != None:
        text = "I don't have rated movies for " + given_year.get(str(yearone).isdigit(), str(yearone))
    else:
        text = "I don't have rated movies for given years"

    return text

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

""" extract the information which will be read to the user from a movie """
def movie(row):
    msg = "The title is " + row['title'] + ". Summary: "\
    + row['summary'] + '. Publication Date: ' + row['year'] \
    + ". Actors: " + row['leading_actors'] + ". Country: " + row['country'] + " ."
    return msg

"""
    this function orders the queried movie data
"""
def speak_n(data=[], order='None', read_n=None):
    limit = 25
    order_ = order.lower()
    text = "Looks like there is nothing to do."
    movie_joiner = "  Next Movie is:  "
    nothing_fn = lambda a, b, c: text

    function_for = {
        "1st": lambda joiner, data, sentence: sentence + joiner.join( data[:n] ),
        "first": lambda joiner, data, sentence: sentence + joiner.join( data[:n] ),
        "last":  lambda joiner, data, sentence: sentence + joiner.join( data[-n:] ),
        "all":  lambda joiner, data, sentence: sentence + joiner.join( data[0:limit] ),
    }


    read_n = str(read_n)
    if not read_n.isdigit():
        read_n = '0'

    n = int(read_n)

    if n < 2:
        n = 1
        fn = function_for.get(order_, nothing_fn)
        text = fn(movie_joiner, data, "")
    elif n > limit:
        n = limit
        fn = function_for.get(order_, nothing_fn)
        sentence = "The number of movies to read exceed the limit I will read twenty five movies this time, "
        text = fn(movie_joiner, data, sentence) + ". this is the end thank you!"

    else:
        fn = function_for.get(order_, nothing_fn)
        text = fn(movie_joiner, data, "I'll start to read the movies, ") + ". this is the end thank you!"

    return text

