#This is the main file the runs all the other files.

import os
from flask import Flask, render_template, request,Response
import json
import storage_ibm_db2
import pandas as pd
import chatbot 
import tone_analyzer as ta
#Default location for displaying functionality, if any issues occur due to browser
user_lat = 40.7128
user_long = 74.0060

#General initializations for flask app
app = Flask(__name__)
app.secret_key = '#savethepeople'
ports = int(os.getenv('PORT', 8000)) 

#All the global variables to maintain the chatbot conversation.
city_or_area = ""
context = {}
output = ""
response ={}

# General Flask methods to render a template
@app.route("/")
def home():
	global user_lat
	global user_long
	user_lat = 40.7128
	user_long = 74.0060
	global city_or_area
	city_or_area = ""	
	global context
	context = {}
	return render_template("index.html")
@app.route("/maploc")
def get_location():
	global user_lat
	global user_long
	user_lat = request.args.get('lat')
	user_long = request.args.get('long')
	print(user_lat,user_long)
	return "done"	
 	
@app.route("/get")
def response():
	flag= False
	global user_lat
	global user_long

	global context
	global city_or_area
	global output
	global response
	global count
	bot_input = request.args.get('msg')
	print("This is input:",bot_input)
	string = storage_ibm_db2.string	
	if string.lower() in bot_input.lower():
		list_string_to_be_attached = []
		flag = True
		tone = ta.get_tone(bot_input)
		list_string_to_be_attached.append(storage_ibm_db2.pre_string+tone+storage_ibm_db2.post_string)
		 
		
	#handling exceptions
	try:
		if not flag:		
			response,output,context,string_to_be_attached_in_bot_output,flag_for_string_to_be_attached = chatbot.analyze_message(context,bot_input,city_or_area,float(user_lat),float(user_long))	
			#print(response)
			if storage_ibm_db2.response_string_to_get_city_input in output:
				city_or_area = bot_input
				print("This is my city or area:",city_or_area)
				print("Found you two.")
			if flag_for_string_to_be_attached:
				output.extend(string_to_be_attached_in_bot_output) 
			
			print("output",output)     
	except Exception as exception:
		print(exception)              
		return ("<span> Watson Error. Refresh Page and retry</span>")		
	if flag:
		output = []
		output.extend(list_string_to_be_attached)
		flag = False 
		
	output_string = ""    
	for string in output:        
		output_string += "<span>"+ str(string) + "</span>" + "<br>"	
	return output_string
	

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=ports, debug=True)
    app.run()
