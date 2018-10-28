# Natural-Disaster-Chat-Bot
This bot was made in response to IBM call for code with a plethora of ways to save people stuck in the aftermath of a disaster.
ELIZABETH NATURAL DISASTER CHATBOT 
	 	 	 	 	 	1.2.0 
    https://elizabeth.eu-gb.mybluemix.net/ 
 	 	 	 
 	 
1.	Introduction 
2.	Tools and technologies used. 
3.	Advantages and why this? 
4.	Architecture Diagram 
5.	Sample use cases of this chat bot 
6.	Sample Scripts for chatbot 
7.	Roadmap: How to scale and Future work? 
8.	Running the code on a local machine  
9.	Twilio account trial for sending messages to numbers 
10.	Link 
11.	Clarifying ambiguities if any in the Video 
 
 
 
 
 
 
 
 	 
 
 
 
 
 
 
 
	I. 	Introduction 
Natural disasters happen all the time. Although, we can hardly prevent them from happening, we can at least try to mitigate the consequences of the disaster. We saw firsthand how Puerto Rico was affected and how the unpreparedness cost many lives. Now the government is taking so many initiatives to solve and prevent the situation. We believe our solution will be highly beneficial to not only situations like Puerto rice, but to almost any natural disaster solution. Our Solution solves 7 most important challenges faced by people during any disaster. We would like to win the challenge and use the money from the winnings to scale our product and release android and iOS versions. 
 
Note: Our main aim is to save people. 
 
 
  	IIa) Tools, Data Sets and Technologies used at present 
1.	Watson Assistant. 
2.	Watson Knowledge studio. 
3.	Watson Discovery service. 
4.	Watson Tone analyzer. 
5.	IBM DB2 database 6. IBM Cloud Hosting. 
7.	Yahoo weather API (IBM weather API has a pay as you go option.) 
8.	Twilio Messaging Web API 
9.	Google Geolocation HTML  
10.	Geocoder 
11.	Geopy library. 
12.	UN and Latitude longitude datasets for 100 safe locations.  
 
IIb) Additional Tools and Technologies to be used in Future 
1.	Google Maps JavaScript API along with Google geo location API to further improve the accuracy. (Code is already ready for this. This code is also in the submission folder.)  Reason for not using now  There are quotas for each map loading per day that is one map load per day. Need to upgrade the account. 
2.	Watson Language translator (To converse in several local languages) 
3.	Watson Text to Speech and Watson Speech to Text  
4.	IBM Machine Learning to find the probability of a disaster occurring and to find which areas might be affected most if it occurs. 
5.	Personality insights to further assist Tone analyzer 
 
 
 
III. Advantages and the Usefulness in the context of Natural Disasters 
1.Offloading Traffic: Disasters like hurricanes, earth quakes and tornados occur all the time. There are limited personal attending to the calls and taking input from potentially several hundred thousand victims. A chat bot can offload this traffic and effectively help people. Watson Assistant 
2.Resource Management (Matching needs with resources): Supplying resources such as food, clothes, electronics to users is a challenging task as the responders might not exactly know what each person needs. With the chatbot people can ask exactly what they need, and our chat bot automatically matches the needs with the resources.Natalia Rodriguez, his generator ran out of diesel and he died in the aftermath of Puerto Rico. If we could have only supplied and alerted the responders in a timely manner, he would have been alive. (Database and assistant NLC) 
3.Emergency Classification and Alerting Responders: Imagine an Earth quake in the west coast of USA. There will be many calls and 911 centers cannot handle all of them. So, Classifying the situation of emergency into  
1.High 
      2.Medium 
      3.Low  
       Will save lives. (Twilio to send messages) 
 
4)Automatic Location Detection: Imagine a person in a very deadly situation, he might hardly  have a minute or so to speak or talk to a chat bot. In such situations, out chat bot will automatically categorize the emergency, locate the person and send a message to the responders along with what the person has informed the chatbot so that the responder will have enough information to reach and save the person’s life.  Google html geolocation services. We also take location info such as city from user 
 
5)Analyzing the Person’s Mental health (Should not be taken lightly) : Depression alone is a billion-dollar problem in America.  Disasters can add onto that and feed of people’s mind. Disasters can be tough on people, some might need mental therapy. Our Chat bot will help identifying those people and update their information in a database so that they can receive help to recover from the effects of a natural disaster. Tone analyzer and Personality insights can help in this area. 
 
6)Help Identifying Safe Places: The solution will automatically identify the three nearest safe locations identified by the responders, government as well as people from safe locations. This Works similarly to Facebook Mark Me Safe API but it provides more value in that the database can be updated by government officials, responders also so that more safe locations can be identified. In future, We plan to use IBM Watson Machine learning to identity safe locations from the data we collect. Geocoder, Geopy. 
 
7)	Disaster Preparation :  
 People might want to know how to react in certain situations. They will not have much time to search the internet and get an accurate answer as google returns some “million docs”. A chat bot can use AI services such as Watson Discovery to get exact answers the users are looking for using Cognitive capabilities of discovery service. Providing exact information is key in such dramatic and lifethreatening situations. On top of Watson discovery we use Watson knowledge studio to teach Watson and improve the exactness of returned answers.Watson discovery and Knowledge studio. 
 
8)	Weather Forecasting : This simple idea can add so much value in that people can make safe decision based on  the forecasts . Also, it will give them enough info so that for example they will stay at home/bunker during a hurricane. Yahoo weather API. 
 	  
IV. Architecture 
 
  
 See the technical documentation pdf and watch the video to understand how this works.
 Also you can check out the deployed application in IBM cloud.
 
 

V. Sample Use Cases 
 
Earthquake: When an earth quake strikes people lose lives, might get stuck under debris. Emergency classifier along with geolocator and automatic message and ticket uploader will help responders save lives. It will also help identifying the safe places using machine learning and our app. Earthquake preparation tips and cautions. 
 
Floods, Hurricanes: Take Kerala floods in 2018, India.  People get stuck after the floods. They need food, clothes and many other daily resources. More than 50 Million dollars worth resources were donated to Kerala from all over the world. Our resource management system will help here. It will also help in identifying safe places as well as emergency classification. 
 
These are only a sample of endless possible uses of our chat bot. 
 
 
VI: Sample Scripts 
 
1. Please watch the video for all the possible options and scripts. 
 
VII : Scalability and Future Work  
Let’s get real for a moment. We didn’t make this huge effort just to win a competition. We want to deploy this bot  and scale it. 
ROADMAP: 
1.	Scaling the Watson discovery service to at least 100,000 documents to get the most relevant answers than Google. 
2.	Using Google’s Geolocation and Map API to build in a real time map(Costly). 
3.	Release an android version so that the GPS can improve the accuracy further.   
4.	Release iOS version 
5.	Collect data and use IBM Watson Machine Learning and analytics service to further the support during disasters. 
6.	Introduce Multilingual support to translate languages. 
7.	Introduce TTS and STT. 
 
We are not stopping with a bot. We are already on course to use  state of the art custom neural networks automated using Auto ML (Bayesian Optimization and Reinforcement Learning) to predict the occurrence of a natural disasters based on past data. 
 
8)To run the code on a local Machine: 
   Create a virtual environment. 
   Run pip install -r requirements.txt to install dependencies. 
   Then run python app.py in command window. 
 
9)
   To Send messages to your own telephone number, you must register your mobile phone number using Twilio and enable SMS also you need to subscribe to a Twilio phone number. The cost of each SMS is 0.00075 cents. But, it is certainly worth it when it comes to saving lives. 
 
10)
   https://elizabeth.eu-gb.mybluemix.net/ 
 
11)	Ambiguities in Video : 
    When I say script in video, it just means that the way of using a chat bot. Not the python script. 
    I have just shown the potential advantages of the bot using several scripts. 
 
 
 
  
 
 
 
 
 	 
 
 
 
 
 .    
 
