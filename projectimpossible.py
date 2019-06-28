import random
from os import system, name
from time import sleep

members_name=['Chirag','Anubhav','Rachit','Divyanshu','Ishaan','Rishi']
members_username=['chirag','anubhav','rachit','divyanshu','ishaan','rishi']
members_password=['Chir123@','Anub123@','Rach123@','Divy123@','Isha123@','Rish123@']              #data to be entered

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
    print("You have uccessfully signed up.")

def who_is_online(friends):
    online=[]
    while(1):
        print('\n'*100)
        no_of_friends_online=random.randint(1,len(friends)-2)
        for i in range(no_of_friends_online):
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
        if(Matcher(i,friend,101)!=''):
            print(i)
    
def logged_in(detail):
    choices_of_logged_in()
    choice=int(input())
    member_friends=members_name[members_username.index(detail[0])]
    if(choice==1):
        Chats(member_friends)
    elif(choice==2):
        Friends()
    elif(choice==3):
        Search_friend()
    # to be completed

def choices():
    print("Press 1 for Signup")
    print("Press 2 for Login")


d = 256
def Matcher(pat, txt, q):               # string matching using rabin-karp algorithm
	M = len(pat) 
	N = len(txt) 
	i = 0
	j = 0
	p = 0
	t = 0 
	h = 1
	for i in range(M-1): 
		h = (h * d)% q 
	for i in range(M): 
		p = (d * p + ord(pat[i]))% q 
		t = (d * t + ord(txt[i]))% q
	for i in range(N-M + 1):  
		if p == t:  
			for j in range(M): 
				if txt[i + j] != pat[j]: 
					break
			j+= 1 
			if j == M: 
				print("Pattern found at index " + str(i) )
		if i < N-M: 
			t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
			if t < 0: 
				t = t + q 



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
