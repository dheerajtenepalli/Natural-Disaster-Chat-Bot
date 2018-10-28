#This code covers all the IBM watson assistant tasks
import Location as loc
import numpy as np
import weather
import urgent_message
import storage_ibm_db2 as database
from watson_developer_cloud import ConversationV1
import discovery as dc
import tone_analyzer as ta

username = "dfc65285-dd45-48db-a8a4-5ed95a1a79e4"
password = "MsjxmYro1nxw"
workspace_id = "ce187483-1725-447c-8bd0-002c8239ac88"

#Instantiating the assistant service
conversation = ConversationV1(username = username, 
                              password=password, 
                              version='2017-05-26')

def find_n_least_elements_in_a_list(a,N):
    return np.argsort(a)[:N][::-1]

def analyze_response(response,city_or_area,ulat,ulong):
	if response["intents"]:	
		print(response)
		list_string_to_be_attached = []	 
		try:
			print("Are you safe",response["context"]["Safe"])
			if response["context"]["Safe"] and response["intents"][0]["intent"]=='Yes' and not response["context"]["Track"]:
				print("Value is true")
				print("Updating_value_database")
				lati = ulat
				longi = ulong
				query = """INSERT INTO DASH14124.SAFE("latitude", "longitude","city")VALUES (""" + str(lati) +""","""+ str(longi)+""","""+ "'" +city_or_area+"'"+""");""" 
				database.data_query_multiple_arguments(query)
	
		except Exception as e:
			print(e)
			print("Safe variable not set yet")	 
		if response["intents"][0]["intent"] == "weather":
			try:
				woeid = loc.get_woeid(city_or_area)
				print(woeid)
				Now,Forecast,Wind,Atmosphere,Astronomy = weather.predictWeather(woeid)
				length_of_forecast = len(Forecast)
				print(length_of_forecast)
				if length_of_forecast >= 3:
					list_string_to_be_attached.append("Date : "+Forecast[0]["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Forecast[0]["text"])
					list_string_to_be_attached.append("Date : "+Forecast[1]["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Forecast[1]["text"])
					list_string_to_be_attached.append("Date : "+Forecast[2]["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Forecast[2]["text"])
			
				else:
					list_string_to_be_attached.append("Date : "+Now["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Now["text"])

				return list_string_to_be_attached,True

			except:
				#output = loc.get_lat_long()
				city,address,woeid= loc.get_address_for_lat_long(ulat,ulong)
				Now,Forecast,Wind,Atmosphere,Astronomy = weather.predictWeather(woeid)
				length_of_forecast = len(Forecast)
				print(length_of_forecast)
				if length_of_forecast >= 3:
					list_string_to_be_attached.append("Date : "+Forecast[0]["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Forecast[0]["text"])
					list_string_to_be_attached.append("Date : "+Forecast[1]["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Forecast[1]["text"])
					list_string_to_be_attached.append("Date : "+Forecast[2]["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Forecast[2]["text"])
			
				else:
					list_string_to_be_attached.append("Date : "+Now["date"])
					list_string_to_be_attached.append("Probable Weather Condition Today : "+Now["text"])

				return list_string_to_be_attached,True


		if response["intents"][0]["intent"] == "help":
			urgent_message.sms_to_responders(ulat,ulong,city_or_area,"","")
			#Update in database
		if response["intents"][0]["intent"] == "highhigh":
			urgent_message.sms_to_responders(ulat,ulong,city_or_area,response["input"]["text"],"high")
			#Update in database
		if response["intents"][0]["intent"] == "medium":
			urgent_message.sms_to_responders(ulat,ulong,city_or_area,response["input"]["text"],"medium")
		if response["intents"][0]["intent"] == "low":
			urgent_message.sms_to_responders(ulat,ulong,city_or_area,response["input"]["text"],"low")
		
		if response["intents"][0]["intent"] == "faq":
			passage = dc.search_discovery(response["input"]["text"])
			list_string_to_be_attached.append(passage)				
			return list_string_to_be_attached,True			

		if response["intents"][0]["intent"] == "feel":
			tone = ta.get_tone(response["input"]["text"])
			list_string_to_be_attached.append("We understand that you are filled with "+tone+" feelings. Ups and downs are common in life. If you would like to talk to someone. Please Call us at +1800(256)8990")				
			return list_string_to_be_attached,True
			
		if response["intents"][0]["intent"] == "safe_places":
			#output = loc.get_lat_long()
			#city,address,woeid= loc.get_address_for_lat_long(ulat,ulong)
			database_query = """SELECT * FROM DASH14124.SAFE"""
			data_framed_returned_from_data_base = database.data_query(database_query)
#			print(data_framed_returned_from_data_base)
			list_of_distances_of_safe_places_from_my_place = []

			latitude_list = data_framed_returned_from_data_base["latitude"]
#			print(latitude_list)

			longitude_list = data_framed_returned_from_data_base["longitude"]
#			print(longitude_list)		

			Telephone_list = data_framed_returned_from_data_base["city"]
#			print(Telephone_list)		
		
			parsing = range(len(latitude_list))

			for index in parsing :
				print(latitude_list[index],longitude_list[index],Telephone_list[index])	
				list_of_distances_of_safe_places_from_my_place.append( loc.distance(ulat,latitude_list[index],ulong,longitude_list[index]) )	
		
#			print(list_of_distances_of_safe_places_from_my_place)
#			print("index",find_n_least_elements_in_a_list(list_of_distances_of_safe_places_from_my_place,3))
			indexes = find_n_least_elements_in_a_list(list_of_distances_of_safe_places_from_my_place,3)
			lat1 = latitude_list[indexes[0]]	
			long1 = longitude_list[indexes[0]]	
			lat2 = latitude_list[indexes[1]]	
			long2 = longitude_list[indexes[1]]	
			lat3 = latitude_list[indexes[2]]	
			long3 = longitude_list[indexes[2]]	


			list_string_to_be_attached.append("Cordinates: "+str(lat1)+" "+str(long1)+ "  Area : "+Telephone_list[indexes[0]])
			list_string_to_be_attached.append("Cordinates: "+str(lat2)+" "+str(long2) + " Area : "+Telephone_list[indexes[1]])
			list_string_to_be_attached.append("Cordinates: "+str(lat3)+" "+str(long3)+ " Area : "+Telephone_list[indexes[2]])
			

			return list_string_to_be_attached,True

		




	return "",False 

def analyze_message(context,bot_input,city_or_area,ulat,ulong):
	try:    
		response = conversation.message(
				workspace_id = workspace_id,
					input = {'text': bot_input},
					context = context)
		string_to_be_attached,flag_for_string_to_be_attached = analyze_response(response.result,city_or_area,ulat,ulong)
		

		return response.result,response.result['output']['text'] , response.result['context'],string_to_be_attached,flag_for_string_to_be_attached


			
			
	except Exception as exception:
		print(exception)
