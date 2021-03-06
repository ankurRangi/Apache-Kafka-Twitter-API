# -*- coding: utf-8 -*-
"""BDA_Assignment_04_v2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gfYg_0pK4fVIOxYRi9ybLD3ySsqR2cg2

# Streaming Twitter Data Using Kafka

Importing the libraries:
"""

!pip install kafka-python
!pip install python-twitter
!pip install tweepy

"""# Now Start the Apache Kafka with the following commands in their respective directory in a cmd prompt.

zkServer (To start Zookeeper)

kafka-server-start.bat config\server.properties (To connect Kafka)
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import KafkaProducer
import json
import kafka

"""Using the developer.twitter.com (developer account) access your necessary API keys and tokens. 
(Every Key is unique and limited)
"""

twitterApiKey = 'xKH*******************ubqS'
twitterApiSecret = 'VYO5A******************************tw1r19'
twitterApiAccessToken = '1661**************************************DK40xr'
twitterApiAccessTokenSecret = 'hGKDl***************************************qS7FYfV'

class StdOutListener(StreamListener):
    def on_data(self, data):
        json_ = json.loads(data) 
        producer.send("test", json_["text"].encode('utf-8'))
        return True
    def on_error(self, status):
        print (status)

query = ['COVID19', "CORONA VACCINE"]

producer = KafkaProducer(bootstrap_servers='localhost:9092', api_version= (0, 10, 0),value_serializer=lambda v: json.dumps(v).encode('utf-8'))
listener = StdOutListener()
auth = OAuthHandler(twitterApiKey, twitterApiSecret)
auth.set_access_token(twitterApiAccessToken, twitterApiAccessTokenSecret)
stream = Stream(auth, listener)
stream.filter(track = query)

#kafka = KafkaClient(bootstrap_servers= "localhost:9092")
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
              api_version=(0,11,5),
              value_serializer=lambda x: dumps(x).encode('utf-8'))
listener = StdOutListener()
auth = OAuthHandler(twitterApiKey, twitterApiSecret)
auth.set_access_token(twitterApiAccessToken, twitterApiAccessTokenSecret)
stream = Stream(auth, listener)
stream.filter(track=query)
#KafkaTimeoutError: Failed to update metadata after 60.0 secs.
