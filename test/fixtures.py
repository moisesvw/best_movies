FIXTURES =  { 
  "initial_request": {
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": "true"
    },
    "request": {
      "type": "LaunchRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T12:11:36Z",
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "response_initial_request":{
    "version": "1.0",
    "response": {
      "outputSpeech": {
        "type": "PlainText",
        "text": "Welcome to Best Movies, contentWhat are the best movies of 1965, What are the best movies between 1965 and 1980."
      },
      "card": {
        "content": "SessionSpeechlet - Welcome to Best Movies, contentWhat are the best movies of 1965, What are the best movies between 1965 and 1980.",
        "title": "SessionSpeechlet - Welcome",
        "type": "Simple"
      },
      "reprompt": {
        "outputSpeech": {
          "type": "PlainText",
          "text": "What are the best movies of 1965, What are the best movies between 1965 and 1980."
        }
      },
      "shouldEndSession": "false"
    },
    "sessionAttributes": {}
  },

  "query_movies_two_dates_event":{
    "session": {
      "new": 'false',
      "sessionId": "session1234",
      "attributes": {},
      "user": {
        "userId": 'null'
      },
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
      }
    },
    "version": "1.0",
    "request": {
      "intent": {
        "slots": {
          "PublicationDateRangeOne": {
            "name": "PublicationDateRangeOne",
            "value": "1990"
          },
          "PublicationDateRangeTwo": {
            "name": "PublicationDateRangeTwo",
            "value": "1996"
          }
          
        },
        "name": "BestMoviesIntent"
      },
      "type": "IntentRequest",
      "requestId": "request5678"
    }
  },

  "query_movies_one_date_event":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": 'true'
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-03-30T04:02:49Z",
      "intent": {
        "name": "BestMoviesIntent",
        "slots": {
          "PublicationDateRangeOne": {
            "name": "PublicationDateRangeOne",
            "value": "1945"
          },
          "PublicationDateRangeTwo": {
            "name": "PublicationDateRangeTwo"
          }
        }
      }
    },
    "version": "1.0"
  },

  "read_two_movies_event":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "publication_date_one": "1985",
        "last_intent": "BestMoviesIntent"
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-01T05:24:27Z",
      "intent": {
        "name": "BestMoviesIntentRead",
        "slots": {
          "ReadOrder": {
            "name": "ReadOrder",
            "value": "last"
          },
          "ReadN": {
            "name": "ReadN",
            "value": "2"
          }
        }
      }
    },
    "version": "1.0"
  },

  "read_all_movies_event":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-20T03:01:37Z",
      "intent": {
        "name": "BestMoviesIntentRead",
        "slots": {
          "ReadOrder": {
            "name": "ReadOrder",
            "value": "all"
          },
          "ReadN": {
            "name": "ReadN"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  }

,

"help_intent_after_open_app":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {},
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-20T05:05:50Z",
      "intent": {
        "name": "AMAZON.HelpIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "stop_intent_after_open_app":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "publication_date_two": "1985",
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-20T18:17:17Z",
      "intent": {
        "name": "AMAZON.StopIntent",
        "slots": {

        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "cancel_after_open_app":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "AMAZON.StopIntent",
        "last_last_intent": "BestMoviesIntent",
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-20T18:38:03Z",
      "intent": {
        "name": "AMAZON.CancelIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "stop_none_session":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": None,
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": "true"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T12:31:21Z",
      "intent": {
        "name": "AMAZON.StopIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "yes_intent_with_info":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "AMAZON.StopIntent",
        "last_last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T01:59:41Z",
      "intent": {
        "name": "AMAZON.YesIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "yes_intent_without_info":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {},
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T01:59:41Z",
      "intent": {
        "name": "AMAZON.YesIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "no_intent_with_int":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T02:02:29Z",
      "intent": {
        "name": "AMAZON.NoIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "no_intent_without_int":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {},
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T02:02:29Z",
      "intent": {
        "name": "AMAZON.NoIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "repeat_intent":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965",
        "last_last_intent": ""
      },
      "user": {
        "userId": "amzn1.ask.account."
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-21T02:04:37Z",
      "intent": {
        "name": "AMAZON.RepeatIntent",
        "slots": {}
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "read_all":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "publication_date_two": "1985",
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId",
      "timestamp": "2016-04-25T13:28:45Z",
      "intent": {
        "name": "BestMoviesIntentRead",
        "slots": {
          "ReadOrder": {
            "name": "ReadOrder",
            "value": "all"
          },
          "ReadN": {
            "name": "ReadN"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },

  "read_all_error":{
    "session": {
      "sessionId": "SessionId.",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {},
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": "false"
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId.",
      "timestamp": "2016-04-26T03:42:44Z",
      "intent": {
        "name": "BestMoviesIntentRead",
        "slots": {
          "ReadOrder": {
            "name": "ReadOrder",
            "value": "all"
          },
          "ReadN": {
            "name": "ReadN"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },
  "should_end_session_bad_call": {
  "session": {
      "sessionId": "SessionId",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": True
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId",
      "timestamp": "2016-05-10T01:07:43Z",
      "intent": {
        "name": "BestMoviesIntent",
        "slots": {
          "PublicationDateRangeOne": {
            "name": "PublicationDateRangeOne"
          },
          "PublicationDateRangeTwo": {
            "name": "PublicationDateRangeTwo"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },
  "read_all_error_reported": {
  "session": {
    "sessionId": "SessionId",
    "application": {
      "applicationId": "amzn1.echo-sdk-ams.app"
    },
    "user": {
      "userId": "amzn1.ask.account"
    },
    "new": True
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId",
    "timestamp": "2016-05-10T01:42:16Z",
    "intent": {
      "name": "BestMoviesIntentRead",
      "slots": {
        "ReadOrder": {
          "name": "ReadOrder",
          "value": "all"
        },
        "ReadN": {
          "name": "ReadN"
        }
      }
    },
    "locale": "en-US"
  },
  "version": "1.0"
},
  "query_movies_1925": {
  "session": {
    "sessionId": "SessionId",
    "application": {
      "applicationId": "amzn1.echo-sdk-ams.app"
    },
    "attributes": {
      "publication_date_two": "?",
      "last_intent": "BestMoviesIntent",
      "publication_date_one": "1925"
    },
    "user": {
      "userId": "amzn1.ask.account"
    },
    "new": False
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId",
    "timestamp": "2016-05-10T02:05:12Z",
    "intent": {
      "name": "BestMoviesIntentRead",
      "slots": {
        "ReadOrder": {
          "name": "ReadOrder",
          "value": "all"
        },
        "ReadN": {
          "name": "ReadN"
        }
      }
    },
    "locale": "en-US"
  },
  "version": "1.0"
},
  "query_movies_1962": {
    "session": {
      "sessionId": "SessionId",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": True
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId",
      "timestamp": "2016-05-11T01:05:02Z",
      "intent": {
        "name": "BestMoviesIntent",
        "slots": {
          "PublicationDateRangeOne": {
            "name": "PublicationDateRangeOne",
            "value": "1962"
          },
          "PublicationDateRangeTwo": {
            "name": "PublicationDateRangeTwo"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },
  "query_movies_1935": {
    "session": {
      "sessionId": "SessionId",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": True
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId",
      "timestamp": "2016-05-11T01:05:02Z",
      "intent": {
        "name": "BestMoviesIntent",
        "slots": {
          "PublicationDateRangeOne": {
            "name": "PublicationDateRangeOne",
            "value": "1935"
          },
          "PublicationDateRangeTwo": {
            "name": "PublicationDateRangeTwo"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },
  "read_first_1965": {
    "session": {
      "sessionId": "SessionId",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": False
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId",
      "timestamp": "2016-05-12T14:17:19Z",
      "intent": {
        "name": "BestMoviesIntentRead",
        "slots": {
          "ReadOrder": {
            "name": "ReadOrder",
            "value": "1st"
          },
          "ReadN": {
            "name": "ReadN"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  },
  "read_last_1965": {
    "session": {
      "sessionId": "SessionId",
      "application": {
        "applicationId": "amzn1.echo-sdk-ams.app"
      },
      "attributes": {
        "last_intent": "BestMoviesIntent",
        "publication_date_one": "1965"
      },
      "user": {
        "userId": "amzn1.ask.account"
      },
      "new": False
    },
    "request": {
      "type": "IntentRequest",
      "requestId": "EdwRequestId",
      "timestamp": "2016-05-12T14:19:08Z",
      "intent": {
        "name": "BestMoviesIntentRead",
        "slots": {
          "ReadOrder": {
            "name": "ReadOrder",
            "value": "last"
          },
          "ReadN": {
            "name": "ReadN"
          }
        }
      },
      "locale": "en-US"
    },
    "version": "1.0"
  }
}