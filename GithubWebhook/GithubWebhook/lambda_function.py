import json
import os
import tweepy

# importing the environment variables - is this safe? We'll see ...
consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

# setup authentication with twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def lambda_handler(event, context):
    mytweet = f"Hi, {event['body']['commit'][0]['committer']['name']} just commited with message {event['body']['commit'][0]['message']}!"
    status = api.update_status(status=mytweet)
    
    response_body =  { "message": "Your tweet has been posted!"}
    
    return {
      "isBase64Encoded": "false",
      "statusCode": 200,
      "headers": {},
      "body": json.dumps(response_body)
    }