from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "751657421177622528-Jp46Gn0Z3J9T5nq4oP1bifAk0X1I1qn"
access_token_secret = "qmWzbhnHVfm7wqvftUrVGe2UB4aBwpZwmcvFrmMzIZCIm"
consumer_key = "lq9WJsV4SgzvhyOnUTA6J57jR"
consumer_secret = "nWDh2BRLJa08wF9t0oqmTmJ1FYJMOr2fqjT941T4T5Mk2ZeuPB"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['google pixel'])