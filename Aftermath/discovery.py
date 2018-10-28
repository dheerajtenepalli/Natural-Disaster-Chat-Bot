import json
import watson_developer_cloud
from watson_developer_cloud import DiscoveryV1
import config as cg

"""Instantiating the discovery instance """
collection_id = "6d41201d-4792-460e-bbdc-b787c8815b78"
Environment_id = "bb85dee6-60fc-4664-ade8-894a0c2a5e22"


"""Instantiating Discovery service"""
discovery = DiscoveryV1(
      username="3aafa454-0f24-4247-a392-4d9287c505a3",
      password="0CO8Se6r7ltb",
      version="2017-10-16"
    )


def search_discovery(query):
	natural_language_query = query
	search_response = discovery.query(Environment_id,collection_id,natural_language_query =natural_language_query,count = 50,passages_count = 100)	
	try:
		discovery_output = str(search_response.result["passages"][0]["passage_text"]).replace("<b>","").replace("\n","").replace("</li>","").replace("<li>","").replace("<p>","").replace("</p>","")
	except Exception as e:
		discovery_output = "No Relevant info found"	
	return discovery_output


						
	
#print(search_discovery("how to prepare for wildfire")) 


