import requests
API_URL = "https://api-inference.huggingface.co/models/Moatasem22/bart_CNN_NLP"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def summarize_text(text):
    output = query(
	    {
		    "inputs": text,
		    'parameters': {'truncation': 'only_first'}
	    }
    )
    return output[0]["generated_text"]




	

