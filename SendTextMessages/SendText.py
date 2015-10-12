# https://www.twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Start IDLE from a VirtualEnv:
# (virtualenv)$ python -c "from idlelib.PyShell import main; main()"

 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "<account_sid>"
auth_token  = "<auth_token>"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi. My name is unknown.",
    to="+<your phone number>",    # Replace with your phone number
    from_="+<your twilio number>") # Replace with your Twilio number
print message.sid
