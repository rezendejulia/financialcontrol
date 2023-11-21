# def home() -> str:
#     presentation = 'Welcome to your personal financial control!\nPlease choose one of the options below:\n\n[ 1 ] - Login\n[ 2 ] - Register\n[ 3 ] - Exit\n'
#     print(presentation)

#     answer = input('Enter your answer: ')

#     return answer

# def connector(x: str):
#     if x == '1':
#         print('\nYou chose to log in.')
#         login()
#     elif x == '2':
#         register()
#     elif x == '3':
#         print('\nAre you sure you want to leave?')
#         leaving()
#     else:
#         print('\nOps! Chosen option is not valid... Please try again!!')
#         main()

# def login():
#     log = input('Please insert your email/username: ')
#     pw = input('Please insert you password: ')
#     # Add feature to verify if inserted data is correct

# def register():
#     print('\nTo register, we need some information:')
#     username = input('Please insert username/email: ')
#     # Add feature to verify if inserted data already exists.
#     password = input('Please insert password: ')
#     rppassword = input('Please insert password again: ')

#     options = '\n[ 1 ] - Cancel\n[ 2 ] - Ok!'
#     print(options)
#     answer = input('\nEnter your answer: ')
#     if answer == '1':
#         main()
#     elif answer == '2':
#         if password != rppassword:
#             print("Ops! Passwords doesn't match!")
#             register()
#         else:
#             print('Successfully registered!')


# def leaving():
#     options = '\n[ 1 ] - Yes\n[ 2 ] - No'
#     print(options)
#     answer = input('\nEnter your answer: ')
#     if answer == '1':
#         print('\nExiting... Thanks for using our software! See you! :)')
#     elif answer == '2':
#         main()
#     else:
#         print('\nOps! Chosen option is not valid... Please try again!!')
#         leaving()


# def main():
#     answer = home() # -> [1, 2, 3]

#     connector(x = answer)


# main()

def summary() -> str:
    begin = 'Hello! Where do you want to go?\n\n[ 1 ] - Dashboard\n[ 2 ] - Bills\n[ 3 ] - Cards\n[ 4 ] - Export'
    print(begin)
    
    answer = 'Enter your answer: '
    
    return answer

def connector(answer: str):
    if answer == '1':
        dashboard()
    elif answer == '2':
        bills()
    elif answer == '3':
        cards()
    elif answer == '4':
        export()
    else:
       print('\nOps! Chosen option is not valid... Please try again!!')
       main()

def dashboard():
    pass

def bills():
    pass

def cards():
    pass

def export():
    pass

def main():
    answer = summary() # -> [1, 2, 3]

    connector(answer = answer)