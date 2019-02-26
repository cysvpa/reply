# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import  requests
import json
# TODO: replace with your own app_id and app_key

app_id = ''
app_key = ''
language = 'en'
word_id = 'ash'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word_id.lower()

#url Normalized frequency
urlFR = 'https://od-api.oxforddictionaries.com:443/api/v1/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()

r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
a = json.dumps(r.json())

print(r.json()['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'])

print(r.text)
