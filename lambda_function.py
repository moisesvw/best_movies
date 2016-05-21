"""
This function was build base on amazon Alexa Skill tutorial
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import dialogs
import config

APP_ID = config.ENV['app_id']

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
        This is important to avoid request from other unexpected applications
    """
    if (event['session']['application']['applicationId'] != APP_ID):
        raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        response = on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        response =  on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        response = on_session_ended(event['request'], event['session'])

    return response


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """
        Called when the user launches the skill without specifying what theywant
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    return dialogs.get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    """ a condition per every intent """
    if intent_name == "BestMoviesIntent":
        return dialogs.get_best_thousand_movies(intent, session)
    elif intent_name == "BestMoviesIntentRead":
        return dialogs.read_n_or_all(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return dialogs.get_help_response()
    elif intent_name == "AMAZON.StopIntent" or intent_name == "AMAZON.CancelIntent":
        return dialogs.get_cancel_response(intent, session)
    elif intent_name == "AMAZON.YesIntent":
        return dialogs.yes_response(intent, session)
    elif intent_name == "AMAZON.NoIntent":
        return dialogs.not_response(intent, session)
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """
        Called when the user ends the session.
        Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
