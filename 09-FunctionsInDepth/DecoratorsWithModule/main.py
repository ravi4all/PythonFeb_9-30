from decorator import login_req

@login_req
def welcome():
    print("Welcome User")

@login_req
def profile():
    print("This is profile")


#welcome()
#profile()
