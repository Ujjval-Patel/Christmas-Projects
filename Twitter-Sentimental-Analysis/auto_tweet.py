import tweepy 
import twitter_credentials
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

  
# personal information 
  
# authentication 
auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET) 
auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET) 
   
api = tweepy.API(auth) 
tweet ="trying to tweet using python." # toDo 
image_path ="Tuesday.jpg" # toDo 
  
# to attach the media file 
status = api.update_with_media(image_path, tweet)  
api.update_status(status = tweet)