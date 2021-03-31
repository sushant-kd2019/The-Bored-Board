# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from config import AUTH, SID

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = SID
auth_token = AUTH
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16787122995',
                     to='+917428035953'
                 )

print(message.sid)
