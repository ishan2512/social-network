import random
from os import system, name
from time import sleep

members_name=['Chirag','Anubhav','Rachit','Divyanshu','Subrat','Ishaan','Rishi']
members_username=['chirag','anubhav','rachit','divyanshu','subrat','ishaan','rishi']
members_password=['Chir123@','Anub123@','Rach123@','Divy123@','Subr123@','Isha123@','Rish123@']              #data to be entered

def members(friend):
    friends_circle={'Chirag':['Anubhav','Rachit','Divyanshu','Subrat','Ishaan','Rishi'],
                    'Anubhav':['Rachit','Divyanshu','Subrat','Chirag'],
                    'Rachit':['Chirag','Anubhav','Divyanshu'],
                    'Subrat':['Rachit','Divyanshu','Chirag','Anubhav'],
                    'Ishaan':['Chirag','Rishi'],
                    'Rishi':['Chirag','Ishaan']}
    return friends_circle[friend]   
    
    
def check_if_member(username,password):
    if username in members_username:
        user_id=members_username.index(username)
        if(members_password[user_id]==password):
            return True
        return False
    return False
    # to be completed
    
    
def check_password(password):
    special_characters='!@?£$%&'
    capital='QWERTYUIOPASDFGHJKLZXCVBNM'
    small='qwertyuiopasdfghjklzxcvbnm'
    number='123456789'
    countsc,countc,counts,countn=0,0,0,0
    if(7<len(password)<16):
        for i in range(len(password)):
            if password[i] in special_characters:
                countsc+=1
            elif password[i] in capital:
                countc+=1
            elif password[i] in small:
                counts+=1
            elif password[i] in number:
                countn+=1
        if(countsc>0 and counts>0 and countc>0 and countn>0):
            return True
        else:
            return False
    else:
        return False

def login(if_login):
    detail=[]
    print('Username')
    username=input()
    print('Password')
    password=input()
    
    if(check_if_member(username,password)==True):
        detail.append(username)
        detail.append(password)
        if_login=1
        return detail,if_login;
    else:
        print('Who Are You??')
    
def Signup():
    print('Name')
    name=input()
    print('Username')
    username=input()
    while(1):
        print('Password')
        password=input()
        if(check_password(password)==True):
            print("Password Accepted")
            print("You Are On")
            break
        else:
            print("Password is weak")
            print("Please Enter A Valid Password")

def who_is_online(friends):
    online=[]
    while(1):
        print('\n'*100)
        for i in range(len(friends)-2):
            friend=random.choice(friends)
            if friend not in online:
                online.append(friend)
                print(friend)
        sleep(5)
        online=[]

def Friends(detail):
    friends=[];k=1
    if(len(friends)==0):
        print("YOU HAVE NO FRIENDS..")
    else:
        for i in friends:
            print(i)
        print('Type the name for friends of'+i)
        print("\n")
        print('Press 0 for nothing')
        choice=int(input())
        if(choice==0):
            logged_in(1)
        else:
            members(i)
            
def Chats(member_friend):
    friends_list=members(member_friend)
    who_is_online(friends_list)
        
    # to be completed


def choices_of_logged_in():
    print("Press 1 for Chats")
    print("Press 2 for Friends")
    print("Press 3 for Searching a Friend")

def Search_friend():
    friend=input()
    for i in members_name:
        if(Matcher(i,friend,40999999, 999999937)!=''):
            print(i)
    
def logged_in(detail):
    choices_of_logged_in()
    choice=int(input())
    member_friends=members_name[members_username.index(detail[0])]
    switcher={
        1:Chats(member_friends),
        2:Friends(),
        3:Search_friend()
        }
    # to be completed

def choices():
    print("Press 1 for Signup")
    print("Press 2 for Login")


def Matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1)%q
    p = 0
    t = 0
    result = []
    for i in range(m): # preprocessing
        p = (d*p+ord(pattern[i]))%q
        t = (d*t+ord(text[i]))%q
    for s in range(n-m+1): # note the +1
        if p == t: # check character by character
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = (t-h*ord(text[s]))%q # remove letter s
            t = (t*d+ord(text[s+m]))%q # add letter s+m
            t = (t+q)%q # make sure that t >= 0
    return result



choices()
choice=int(input())
if_login=0                                  #initialise not logged in
if(choice==1):
    Signup()                                #go to signup page
elif(choice==2):
    detail,if_login=login(if_login)         #go to login page
else:
    print("Invalid Input")
print(if_login)
print(detail)
if(if_login==1):
    logged_in(detail)

"""check to be logged  in"""
