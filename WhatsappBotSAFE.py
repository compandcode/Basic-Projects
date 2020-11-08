# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client #Import Twilio module. Works on a client server basis.
import time


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

#ID's from Twilio console. You will need to generate these yourself!!!
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token) #Defines the client/

message = client.messages.create( #Method to create the message.
    from_='whatsapp:', #From Address.
    body='Whatsapp message through Twilio', #The message itself, what it will contain.
    to='whatsapp:' #The phone number which will recieve the message.
    )
print(message.sid) #String printed to indicate the message was successfully sent.

'''
Requires installing the Twilio API.
You can only message numbers that were added to the sandbox.
Use at your own risk.
This is only for educational purposes.
'''
