# we import the Twilio client from the dependency we just installed
import twilio
from twilio.rest import Client
# the following line needs your Twilio Account SID and Auth Token
client = Client("AC461edc1978ae7c355bc3d5d7cb48eb51", "b6dbfcb3fa4c5076e520f9ae5a6ebb0e")


def sms_to_responders(latitude,longitude,city,user_response,tag):
	# change the "from_" number to your Twilio number and the "to" number	
	# to the phone number you signed up for Twilio with, or upgrade your
	# account to send SMS to any phone number
	body = "Emergency Message : "+user_response +" Category : "+tag+". Please reach" + str(latitude) +","+ str(longitude)+". City: "+ city + " to help the person."	
	client.messages.create(to="+918374879990",from_="+13144622398",body=body)
