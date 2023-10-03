import requests
import sys
import re

url_to_fetch = "https://leghe.fantacalcio.it/" + sys.argv[1] + "/classifica"
response_classifica = requests.get(url_to_fetch)

encodedJsons = re.findall(r"'(ey.*)'", response_classifica.text)
competition = re.findall(r"currentCompetition: ({.+}),", response_classifica.text)[0]

response_lega = requests.get("https://leghe.fantacalcio.it/" + sys.argv[1])
countdown = re.findall(r"countdown: Number\(\"(.+)\"\)", response_lega.text)[0]

import base64
import json

calendario = json.loads(base64.b64decode(encodedJsons[0]))['data']
squadre = json.loads(base64.b64decode(encodedJsons[1]))['data']
competition_info = json.loads(competition)
countdown_seconds = int(countdown)

def get_squadra_name(squadra_id):
    for squadra in squadre:
        if squadra['id'] == squadra_id:
            return squadra['n']
    return None

def to_countdown_string(seconds):
    days = seconds // (24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return str(days) + "d " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s"

print ("NOME COMPETIZIONE:")
print (competition_info['nome'])

print ("\n\nSQUADRE:")
for squadra in squadre:
    print(squadra['n'])

print ("\n\nCALENDARIO:")
for giornata in calendario["cale"]["cinc"]:
    print ("\nGiornata " + str(giornata['gl']))
    for inc in giornata['inc']:
        print (get_squadra_name(inc['ida']) + " - " + get_squadra_name(inc['idb']) + ": " + inc['res'])

print ("\n\nCLASSIFICA:")
for squadra_info in competition_info['squadre']:
    print(str(squadra_info['pos']) + ". " + get_squadra_name(squadra_info['id']) + " (" + str(squadra_info['p']) + " pt)") 

print ("\n\nCOUNTDOWN:")
print (to_countdown_string(countdown_seconds))

