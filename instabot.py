import requests

# access token
ACCESS_TOKEN = "4520134249.a092bc7.455118f824224145bd0b49d913df6338"
print("___________It is Access token for using app______  " + ACCESS_TOKEN)

base_url = 'https://api.instagram.com/v1/'


######################################################################################################################

# -----owner information in the form of json------------------------
def self_info():
    url = base_url + 'users/self/?access_token=' + ACCESS_TOKEN
    my_info = requests.get(url).json()
    print("Owner info in the form of json:")
    print(my_info)


# self_info()


####################################################################################################################


# -------owner information field by field------------
def complete_self_info():
    url = base_url + 'users/self/?access_token=' + ACCESS_TOKEN
    my_info = requests.get(url).json()
    print("---------The Owner information is:----------------")
    # print (my_info)
    print("Owner id is :" + my_info['data']['id'])
    print("Owner name is :" + my_info['data']['username'])
    print("Owner full name is :" + my_info['data']['full_name'])
    print("Owner media is :" + str(my_info['data']['counts']['media']))
    print("Owner following is :" + str(my_info['data']['counts']['follows']))
    print("Owner followers is :" + str(my_info['data']['counts']['followed_by']))
    if my_info['data']['website'] != '':
        print("Owner web is:" + str(my_info['data']['bio']))
    else:
        print("Owner web is: " + "Owner has not website")
    if my_info['data']['bio'] != '':
        print('Owner bio is: ' + str(my_info['data']['bio']))
    else:
        print('Owner bio is: ' + "Owner has not Bio ")


# complete_self_info()

# *********************************************************************************************************************


# -----user information in the form of json-------------
def user_info(insta_user):
    url = base_url + 'users/search?q=' + insta_user + '&access_token=' + ACCESS_TOKEN
    insta_user_info = requests.get(url).json()
    print("info of user  in the form of json")
    print(insta_user_info)


# user_info("ananya_thakur333")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# -------- user information field by field--------
def detail_user_info(insta_user):
    url = base_url + 'users/search?q=' + insta_user + '&access_token=' + ACCESS_TOKEN
    insta_user_info = requests.get(url).json()
    print(insta_user_info)
    print("----------The User Information is-------")
    print("The name of user is  =" + insta_user_info['data'][0]['username'])
    print("The Full  name of user is  =" + insta_user_info['data'][0]['full_name'])
    print("user id is  =" + insta_user_info['data'][0]['id'])
    print("Profile of user is  =" + insta_user_info['data'][0]['profile_picture'])
    if insta_user_info['data'][0]['website'] != '':
        print("User web is:" + str(insta_user_info['data'][0]['bio']))
    else:
        print("User web is: " + "User has not website")
    if insta_user_info['data'][0]['bio'] != '':
        print('User bio is: ' + str(insta_user_info['data'][0]['bio']))
    else:
        print('User bio is: ' + "User has not Bio ")


# detail_user_info("ananya_thakur333")


###########################################################################################################

# ----- get user id----------
def get_user_id(insta_user):
    user_id = user_info(insta_user)
    print("user_id is:")
    print(user_id)


# get_user_id("ananya_thakur333")


# ************************************************************************************************************

# - ---get user post----
def get_user_post(insta_username):
    insta_user_id = user_info(insta_username)
    request_url = base_url + 'users/' + str(insta_user_id) + '/media/recent/?access_token=' + ACCESS_TOKEN
    recent_post = requests.get(request_url).json()
    print("user's recent post is:" + str(recent_post['data'][0]['link']))
    print(recent_post)
    return recent_post['data'][0]['id']


# get_user_post("ananya_thakur333")


# ---------------------------------------------------------------------------------------------------------------


# -----------fuction to like the user post-------------
def like_post(insta_user):
    id = get_user_post(insta_user)
    payload = {"access_token": ACCESS_TOKEN}
    req_url = base_url + "media/" + id + "/likes"
    like_response = requests.post(req_url, payload).json()
    print("-----like detail of an user---------------")
    print(like_response)


# like_post("ananya_thakur333")

################################################################################################################

# ------------- comment on user post-------------
def comment_on_user_post(insta_user):
    id = get_user_post(insta_user)
    request_url = base_url + 'media/' + id + '/comments?access_token=' + ACCESS_TOKEN
    payload = {"access_token": ACCESS_TOKEN, 'text': 'hello you'}
    comment_response = requests.post(request_url, payload).json()
    print("ouput of the post comment")
    print(comment_response)


#################################################################################################################


# -----------------to see  comment on user post------------
def see_comments_on_user_post(insta_user):
    id = get_user_post(insta_user)
    req_url = base_url + 'media/' + id + '/comments?access_token=' + ACCESS_TOKEN
    response = requests.get(req_url).json()
    print("reteriving comments....")
    print(response)
    return response['data'][0]['id']


# see_comments_on_user_post("ananya_thakur333")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----------Function to delete the comment done by owner---------
def delete_the_comment_on_user_post(insta_user):
    user_id = get_user_post(insta_user)
    cmt_id = see_comments_on_user_post(insta_user)
    request_url = base_url + 'media/' + user_id + '/comments/' + cmt_id + '?access_token=' + ACCESS_TOKEN
    response = requests.delete(request_url).json()
    print("----Response of Delete------")
    print(response)

# delete_the_comment_on_user_post("ananya_thakur333")
