import requests
import json


lista = ["salud", "educacion", "seguridad", "infraestructuraIntegral", "cultura", "deportes",
         "institucional", "abastecimiento", "transporte"]

base_url = "https://guiaurbana.gmsantacruz.gob.bo/guiaurbana/public/api/"

for datos in lista:
    api_url = base_url+datos
    response = requests.get(api_url, verify=False)
    if response.status_code == 200:
        
        try:
            data = response.json()
            with open(f'{datos}.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except:
            print("---------Revisar url--", datos)
        
    else:
        print("revisar url", datos)
    """
    https://guiaurbana.gmsantacruz.gob.bo/guiaurbana/public/api/distrito/15
    """