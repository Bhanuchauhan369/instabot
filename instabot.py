import requests

# access token
ACCESS_TOKEN = "4520134249.a092bc7.455118f824224145bd0b49d913df6338"
print("___________It is Access token for using app______  "+ACCESS_TOKEN)

base_url='https://api.instagram.com/v1/'
# owner information display function
def self_info():
    url =base_url +'users/self/?access_token=' +ACCESS_TOKEN
    my_info = requests.get(url).json()
    print (my_info)
self_info()


# user information display function
def user_info(insta_user):
    url= base_url+'users/search?q='+insta_user +'&access_token='+ACCESS_TOKEN
    user_info = requests.get(url).json()
    print (user_info)
    print(user_info['data'][0]['username'])
    print(user_info['meta']['code'])
user_info("ananya_thakur333")