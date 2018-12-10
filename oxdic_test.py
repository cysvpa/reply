# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
# TODO: replace with your own app_id and app_key

app_id = '4475d0a4'
app_key = 'f41ff0b6c8e584e4b17b66cfabd818dd'
language = 'en'
word_id = 'ash'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()

#url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
a = json.dumps(r.json())

print(r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])

print(r.text)
