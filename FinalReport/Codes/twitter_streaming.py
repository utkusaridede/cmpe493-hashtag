#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "***********************"
access_token_secret = "****************"
consumer_key = "***********************"
consumer_secret = "********************"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track = ["bir","bu","ne","ve","ben","de","evet","var","ama","da",
        "sen","daha","bana","kadar","seni","beni","iyi","tamam","onu","bunu","gibi",
        "yok","benim","her","sana","ki","sadece","neden","burada","senin","ya","zaman",
        "sonra","en","mu","misin","hadi","biraz","musun","ona","bak","oldu","hey","istiyorum",
        "geri","onun","bile","kim","bay","yani","bilmiyorum","buraya","belki","peki","olarak",
        "tek","efendim","biri","haydi","olur","et","olacak","olan","adam","merhaba","orada",
        "herhalde","biz","demek","bilmiyorum","gece","ederim","olmak","o","yapmak","almak",
        "kendi","gelmek","ile","vermek","sonra","insan","iki","el","istemek","ara","son","ilk",
        "veya","bunlar","ancak","yemek","su","girmek","orta","yan","durum","gerekmek","bulunmak",
        "ise","diye","ev"], languages=["tr"])
    #stream.filter(locations=[25.40,44.48,35.51,42.06])