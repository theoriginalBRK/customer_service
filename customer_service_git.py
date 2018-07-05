whaaa = "Sorry, we didn't understand your selection."

def cs_service_bot():
    cs_type = input("""Hello! Welcome to the DNS Cable Company's Service Portal.
Are you a new or existing customer?\n [1] New Customer\n [2] Existing Customer. 
Please enter the number corresponding to your choice:""")
    if cs_type == "1":
        new_customer()
    elif cs_type == "2":
        existing_customer()
    else:
        print(whaaa)
        cs_service_bot()
        
def existing_customer():
    exist = input("What kind of support do you need?\n [1] Television Support\n [2] Internet Support\n [3] Speak to a support representative")
    if exist == "1":
        television_support()
    elif exist == "2":
        internet_support()
    elif exist == "3":
        live_rep("support")
    else:
        print(whaaa)
        existing_customer()

def television_support():
    tv = input("What is the nature of your problem?\n [1] I can't access certain channels.\n [2] My picture is blurry.\n [3] I keep losing service.\n [4] Other issues.")
    if tv == "1":
        print("Please check the channel lists at DefinitelyNotSinister.com. If the channel you cannot access is there, please contact a live representative.")
        did_that_help()
    elif tv == "2":
        print(" Try adjusting the antenna above your television set.")
        did_that_help()
    elif tv == "3":
        print("Is it raining outside? If so, wait until it is not raining and then try again.")
        did_that_help()
    elif tv == "4":
        live_rep("support")
    else:
        print(whaaa)
        television_support()  

def internet_support():
    internet = input("What is the nature of your problem?\n [1] I can't connect to the internet.\n [2] My connection is very slow.\n [3] I can't access certain sites.\n [4] Other issues")
    if internet == "1":
        print("Unplug your router, then plug it back in, then give it a good whack, like the Fonz.")
        did_that_help()
    elif internet == "2":
        print("Make sure that all cell phones and other peoples computers are not connected to the internet, so that you can have all the bandwidth.")
        did_that_help()
    elif internet == "3":
        print("Move to a different region or install a VPN. Some areas block certain sites.")
        did_that_help()
    elif internet == "4":
        live_rep("support")
    else:
        print(whaaa)
        internet_support()
        
def new_customer():
    new = input("We're excited to have you join the DNS family, how can we help you?\n [1] Sign up for service.\n [2] Schedule a home visit.\n [3] Speak to a sales representative.")
    if new == "1":
        sign_up()
    elif new == "2":
        home_visit()
    elif new == "3":
        live_rep("sales")
    else:
        print(whaaa)
        new_customer() 
        

def frustrated():
    boo = input("Sorry about that! Select an option:\n [1] Talk to a live representative\n [2] Schedule a home visit")
    if boo == "1":
        live_rep("support")
    elif boo == "2":
        home_visit("support")
    else: 
        print(whaaa)
        frustrated()

def did_that_help():
    resolved = input("Did that solution solve your problem?\n [1] Yes\n [2] No")
    if resolved == "1": 
        print("Thank you for using DNS Cable Company")
    elif resolved == "2":
        frustrated()
    else: 
        print(whaaa)
        did_that_help() 

def home_visit(purpose="none"):
    if purpose == "none":
        homepurpose = input("What is the purpose of the home visit?\n [1] New service installation\n [2] Existing service repair.\n [3] Location scouting for unserviced region.")
        if homepurpose == "1": 
            home_visit("new install")
        elif homepurpose == "2":
            home_visit("support")
        elif homepurpose == "3":
            home_visit("scout")
        else: 
            print(whaaa)
            home_visit(purpose="none")
    elif purpose == "new install":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and install your new service:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
        return visit_date
    elif purpose == "support":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and inspect the problem:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
        return visit_date
    elif purpose == "scout":
        visit_date = input("Please enter a date below when you are available for a technician to come to your home and scout your unserviced region:")
        print("Wonderful! A technical will come visit you on " + visit_date + ". Please be available between the hours of 1:00 am and 11:00 pm.")
        return visit_date
    else: 
        print(whaaa)
        home_visit(purpose="none")
        
def sign_up():
    package = input("Great choice, friend! We're excited to have you join the DNS family! Please select the package you are interested in signing up for.\n [1] Bundle Deal (Internet + Cable)\n [2] Internet\n [3] Cable")
    if package == "1":
        print("You've selected the Bundle Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif package == "2":
        print("You've selected the Internet Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    elif package == "3":
        print("You've selected the Cable Only Package! Please schedule a home visit and our technician will come and set up your new service.")
        home_visit("new install")
    else:
        print(whaaa)
        sign_up()
        
def live_rep(purpose):
    if purpose == "sales":
        print("Please hold while we connect you with a live sales representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    elif purpose == "support":
        print("Please hold while we connect you with a live support representative. The wait time will be between two minutes and six hours. We thank you for your patience.")
    else:
        print(whaaa)
        live_rep()