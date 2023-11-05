import json

with open("salud.json") as file:
    json_object = json.load(file)

features=[]
feature_element = dict()

for element in json_object:
    feature_element = {
        "type": "Feature",
        "id": element["objectid"],
        "geometry": {
            "type": "Point",
            "coordinates": [
                element["x"],
                element["y"]
            ]
        },
        "geometry_name": "geom",
        "properties": {
            "nombre": element["nombre"],
            "sistema": element["sistema"],
            "sub_sistema": element["sub_sistem"],
            "nivel": element["nivel"],
            "uv": element["uv"],
            "mz": element["mz"],
            "distrito": element["distrito"],
            "barrio": element["barrio"],
            "direccion": element["direccion"],
            "google_map": element["google_map"],
            "adm": element["adm"],
            "codigo": element["codigo"],
            "fecha_modificacion": element["last_edi_1"],
            "infraestructura": element["infraestru"],
            "adm_infraestructura": element["adm_infrae"]
        }
    }

    features.append(feature_element)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open("datos_salud_scz.geojson", "w") as f:
    json.dump(geojson, f, indent=4, ensure_ascii=False)

