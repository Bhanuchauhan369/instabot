import requests
# access token
ACCESS_TOKEN = "4520134249.a092bc7.455118f824224145bd0b49d913df6338"
print("___________It is Access token for using app______  "+ACCESS_TOKEN)

base_url = 'https://api.instagram.com/v1/'
######################################################################################################################

# -----owner information in the form of json------------------------
def self_info():
    url = base_url + 'users/self/?access_token=' +ACCESS_TOKEN
    my_info = requests.get(url).json()
    print("Owner info in the form of json:")
    print(my_info)
#self_info()


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


#complete_self_info()
# *********************************************************************************************************************


# -----user information in the form of json-------------
def user_info(insta_user):
    url = base_url + 'users/search?q=' + insta_user + '&access_token=' + ACCESS_TOKEN
    insta_user_info = requests.get(url).json()
    print("info of user  in the form of json")
    #print(insta_user_info)
    return insta_user_info['data'][0]['id']


#user_info("ananya_thakur333")



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


#detail_user_info("ananya_thakur333")
###########################################################################################################

# ----- get user id----------
def get_user_id(insta_user):
    user_id = user_info(insta_user)
    print("user_id is:")
    print(user_id)
    return user_id



#get_user_id("ananya_thakur333")
# ************************************************************************************************************
#----Get the Total no. of user Post-------
def get_post_id(user_name):
    insta_user_id = get_user_id(user_name)
    url = base_url + 'users/' + insta_user_id + '/media/recent/?access_token=' + ACCESS_TOKEN
    recent_post = requests.get(url).json()
    print("it is the link of a recent post of user " +recent_post['data'][0]['link'])
    #print(recent_post)
    for number in range(0, len(recent_post["data"]), 1):  #traversingh all post id of userpass


        print("-------------Total Number Of posts-------- " + str(number))
    return recent_post['data'][0]['id']


####################################################################################################################
# - ---get user post-----------------
def get_user_post(insta_username):
    insta_user_id = user_info(insta_username)
    request_url = base_url + 'users/' + str(insta_user_id) + '/media/recent/?access_token=' + ACCESS_TOKEN
    recent_post = requests.get(request_url).json()
    print("user's recent post is:" + str(recent_post['data'][0]['link']))
    print(recent_post)
    return recent_post['data'][0]['id']


#get_user_post("ananya_thakur333")

# ---------------------------------------------------------------------------------------------------------------


# -----------fuction to like the user post-------------
def like_post(insta_user):
    id = get_user_post(insta_user)
    payload = {"access_token": ACCESS_TOKEN}
    req_url = base_url + "media/" + id + "/likes"
    like_response = requests.post(req_url, payload).json()
    print("-----Successfully Liked---------------")
    print(like_response)


#like_post("ananya_thakur333")

################################################################################################################

# ------------- comment on user post-------------
def comment_on_user_post(insta_user):
    id = get_user_post(insta_user)
    comment_choice = input("Enter Your comment-----   ")
    request_url = base_url + 'media/' + id + '/comments?access_token=' + ACCESS_TOKEN
    payload = {"access_token": ACCESS_TOKEN, 'text': comment_choice}
    comment_response = requests.post(request_url, payload).json()
    print("ouput of the post comment")
    print(comment_response)
#comment_on_user_post("ananya_thakur333")

#################################################################################################################


# -----------------to see  comment on user post------------
def see_comments_on_user_post(insta_user):
    id = get_user_post(insta_user)
    req_url = base_url + 'media/' + id + '/comments?access_token=' + ACCESS_TOKEN
    response = requests.get(req_url).json()
    print("reteriving comments....")
    print(response)
    return response['data'][0]['id']


#see_comments_on_user_post("ananya_thakur333")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#cmt id
def return_comment_id(user_name,post_id):

    comment = input("-----Please enter the comment you want to delete--------   ")
    recent_comments = base_url + "media/" + str(post_id) + "/comments?access_token=" + ACCESS_TOKEN
    recent_comments = requests.get(recent_comments).json()#get to see the comment
    for i in range(0, len(recent_comments['data']), 1): #one by one each
        if comment in recent_comments['data'][i]['text']:
            print("=======Comment Is Found========")
            return recent_comments['data'][i]['id']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ----------Function to delete the comment done by owner---------
def delete_the_comment_on_user_post(insta_user):
    user_id = get_post_id(insta_user)
    cmt_id = return_comment_id(insta_user,user_id)
    if cmt_id==None:
        print("=======Sorry,Please Try Again later=====")
    else:
        request_url = base_url + 'media/' + str(user_id) + '/comments/' + str(cmt_id) + '?access_token=' + ACCESS_TOKEN
        response = requests.delete(request_url).json()
        print("----Response of Delete------")
        print(response)
        if response['meta']['code']==200:
            print("===Your Comment is Successfully Deleted===")

#delete_the_comment_on_user_post("ananya_thakur333")


#######################################################################################################################

#to enter in the while loop to repeat this task again and again
count = 'y'
while count=='y':


    print("***************WELCOME TO INSTABOT***********")
    print("........To Choose One  Number From 1 to 8............................")
    print("--------Enter 1 for Owner Information--------------------------------")
    print("--------Enter 2 for User Information---------------------------------")
    print("--------Enter 3 for see user post------------------------------------")
    print("--------Enter 4 to do like on user post------------------------------")
    print("--------Enter 5 to see the recent comments on post-------------------")
    print("--------Enter 6 to do comment on the instagram user post-------------")
    print("--------Enter 7 to delete the particular comment by comment_id-------")
    print("--------Enter 8 to print the average number of words per comment-----")
    print("--------Enter 9 to delete the comment by word-----------------------")

    choice = input(".......PLEASE ENTER The Choice From 1 TO 9.................")
    if choice=='1':
        complete_self_info()

    elif choice=='2':
        insta_user_name = input("Please Enter Valid User Name Either ananya_thakur333 or Kaurl19  ")
        if insta_user_name=='ananya_thakur333':
            detail_user_info(insta_user_name)
        elif insta_user_name=='kaurl19':
            detail_user_info(insta_user_name)
        else:
            print("PLEASE ENTER A VALID NAME FROM OPTION PROVIDED TO YOU")

    elif choice=='3':
        insta_user_name = input("Please Enter Valid User Name Either ananya_thakur333 or Kaurl19 ")
        if insta_user_name == 'ananya_thakur333':
            get_user_post(insta_user_name)
        elif insta_user_name == 'kaurl19':
            get_user_post(insta_user_name)
        else:
            print("PLEASE ENTER A VALID NAME FROM OPTION PROVIDED TO YOU")

    elif choice=='4':
        insta_user_name = input("Please Enter Valid User Name Either ananya_thakur333 or Kaurl19 ")
        if insta_user_name == 'ananya_thakur333':
            like_post(insta_user_name)
        elif insta_user_name == 'kaurl19':
            like_post(insta_user_name)
        else:
            print("PLEASE ENTER A VALID NAME FROM OPTION PROVIDED TO YOU")

    elif choice=='5':
        insta_user_name = input("Please Enter Valid User Name Either ananya_thakur333 or Kaurl19 ")
        if insta_user_name == 'ananya_thakur333':
            see_comments_on_user_post(insta_user_name)
        elif insta_user_name == 'kaurl19':
            see_comments_on_user_post(insta_user_name)
        else:
            print("PLEASE ENTER A VALID NAME FROM OPTION PROVIDED TO YOU")

    elif choice=='6':
        insta_user_name = input("Please Enter Valid User Name Either ananya_thakur333 or Kaurl19 ")
        if insta_user_name == 'ananya_thakur333':
            comment_on_user_post(insta_user_name)
        elif insta_user_name == 'kaurl19':
            comment_on_user_post(insta_user_name)
        else:
            print("PLEASE ENTER A VALID NAME FROM OPTION PROVIDED TO YOU")


    elif choice=='7':
        insta_user_name = input("Please Enter Valid User Name Either ananya_thakur333 or Kaurl19 ")
        if insta_user_name == 'ananya_thakur333':
            delete_the_comment_on_user_post(insta_user_name)
        elif insta_user_name == 'kaurl19':
            delete_the_comment_on_user_post(insta_user_name)
        else:
            print("PLEASE ENTER A VALID NAME FROM OPTION PROVIDED TO YOU")
    else:
        print("........wrong choice entered.....thank you.....")

    print("*************.........Do You want to use this app again........***********")
    count = input("... #####  Enter 'y' if you want to use this app again #### .....")
