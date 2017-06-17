import json

with open("sound.json") as f:
    json_string = f.read()

    

parsed_json = json.loads(json_string)
results = parsed_json["results"]

alternatives = [result["alternatives"] for result in results]
all_alternatives = [item for sublist in alternatives for item in sublist]
transcripts = [alternative["transcript"] for alternative in all_alternatives]



import json

def get_transcripts(json_string):
    parsed_json = json.loads(json_string)
    results = parsed_json["results"]

    alternatives = [result["alternatives"] for result in results]
    all_alternatives = [item for sublist in alternatives for item in sublist]
    return [alternative["transcript"] for alternative in all_alternatives]
    

    


    