# CRUD - Create Read Update Delete
# Searching Sorting

from datetime import datetime
import DataIO

users = []
userdata = {}

posts = []
postdata = {}

def post_something(username):
    post = input("Post Here : ")
    date = datetime.now().date()
    postdata['post'] = post
    postdata['username'] = username
    postdata['date'] = date.strftime('%D')

    posts.append(postdata.copy())

    login_success(username)

def view_profile(username):
    pass

def update_profile(username):
    pass

def delete_profile(username):
    pass

def logout(x):
    pass

def login_success(username):
    print("Welcome",username)

    for p in posts:
        print("Post :",p['post'])
        print("Post By :",p['username'])
        print("Post On :",p['date'])

    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    choice = input("What do you want to do : ")
    todo = {
        "1" : post_something,
        "2" : view_profile,
        "3" : update_profile,
        "4" : delete_profile,
        "5" : logout
    }

    todo.get(choice)(username)

def login():
    emailID = input("Enter your EmailID : ")
    pwd = input("Enter your Password : ")

    # for user in users:
    #     if user['MailId'] == emailID and user['Password'] == pwd:
    #         print("Login Success")
    #         login_success(user['Name'])
    #     else:
    #         print("Login Failed")

    data = DataIO.readData()
    for user in data:
        # print(user)
        if emailID in user and pwd in user:
            print("Login Success")
            login_success(user[0])

def registration():
    username = input("Enter your Name : ")
    usermail = input("Enter your Mail : ")
    userpwd = input("Enter your Password : ")
    # confirmpwd = input("Confirm Password : ")
    userdata['Name'] = username
    userdata['MailId'] = usermail
    userdata['Password'] = userpwd

    users.append(userdata.copy())
    print("Registered Successfully")

    for data in users:
        print(data)

    saveData()

def saveData():
    DataIO.saveData(users)

def errHandler():
    print("Wrong Choice...")

while True:
    print("""
    1. Login
    2. Registration
    """)

    userChoice = input("Enter your choice : ")

    todo = {
        '1' : login,
        '2' : registration
    }

    todo.get(userChoice, errHandler)()