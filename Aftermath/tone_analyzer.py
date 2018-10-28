from watson_developer_cloud import ToneAnalyzerV3
import json
tone_analyzer = ToneAnalyzerV3(
    version='2017-09-21',
    username='d6ff8e93-ef0b-4bcb-b33f-810a5f0d1f9a',
    password='GhDizfv5b1oW',
    url='https://gateway.watsonplatform.net/tone-analyzer/api'
)

def get_tone(text):
	tone_analysis = tone_analyzer.tone(
	    {'text': text},
    	'application/json').get_result()
	print(tone_analysis)
	try:
		overall_tone = tone_analysis["document_tone"]["tones"][0]["tone_name"]
	except Exception as e:
		print(e)	
		overall_tone = "Not found" 	
	return  overall_tone

#print(get_tone("Iam sad"))
