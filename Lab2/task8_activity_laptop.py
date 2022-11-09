from libdw import pyrebase

"""
TODO 8.0 Fill in the same authentication details as your partner
""" 

dburl = "fill in"
email = "fill in"
password = "fill in" 
apikey = "fill in"
authdomain = dburl.replace("https://","")


config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken']) 

"""
TODO 8.1 With your partner decide what key your node should have
""" 

key = pass 


while True: 

    """
    TODO 8.2 Decide with your partner what values should represent the LED being on or off
    Then prompt the user with a message to ask for the desired action
    """

    """ 
    TODO 8.3 if the value entered by the user is valid, upload the data to firebase to your node
    else, tell the user that an invalid value was entered 
    """









###my_stream.close()



