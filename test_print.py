import requests

print('test working')

# Function to get most favortied tweets of user
def get_favorites(username):
    url = 'https://api.twitter.com/1.1/favorites/list.json'
    params = {'screen_name': username, 'count': 5}  
    response = requests.get(url, params=params)
    return response.json()

# print the most favorited tweets of user
for tweet in get_favorites('stujmar'):
    print(tweet)

print(get_favorites('stujmar'))