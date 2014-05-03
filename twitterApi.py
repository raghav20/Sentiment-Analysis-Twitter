
import twitter
#Setting up Twitter API
api = twitter.Api(
 consumer_key='NGdmaaaCs26N1RLzVGFvjfU2E',
 consumer_secret='MCBDZZif8Mkf7xgHRIUluYqgZZsJtR6bzkrKblih56m0a5Arnm',
 access_token_key='2329691352-qRVgASW79U6YanobJEQWFYN0Avhf8u3W3WTi15e',
 access_token_secret='JPkhFKhD090dtsGZtKvRpoEhzanjVKnitBZEvJNZtnmJP'
 )
search = api.GetSearch(term='Captain America', lang='en', result_type='recent', count=100, max_id='')
for t in search:
 print(t.user.screen_name + ' (' + t.created_at + ')')
 #Add the .encode to force encoding
 print(t.text.encode('utf-8'))
