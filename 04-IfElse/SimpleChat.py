import random

print("Welcome User".center(60))

hello_intent = ['hi','hello','hey','hie','wass up']
bye_intent = ['bye','bie','see you','take care','good bye']

##if user_msg == "hello":
##    print("Hello")
##
##elif user_msg == "bye":
##    print("Bye")

while True:
    user_msg = input("Enter your message : ")

    user_msg = user_msg.lower()

    cpu_helloMessage = random.choice(hello_intent)
    cpu_byeMessage = random.choice(bye_intent)
    
    if user_msg in hello_intent:
        print("CPU :",cpu_helloMessage)

    elif user_msg in bye_intent:
        print("CPU :",cpu_byeMessage)

    else:
        print("I don't Understand...")
