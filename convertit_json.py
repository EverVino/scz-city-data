import json

with open("transporte.json") as file:
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
            "distrito": element["distrito"],
            "barrio": element["barrio"],
            "direccion": element["direccion"],
            "google_map": element["google_map"],
            "adm": element["adm"],
            "codigo": element["codigo"],
            #"infraestructura": element["infraestru"],
        }
    }

    features.append(feature_element)

geojson = {
    "type": "FeatureCollection",
    "features": features
}

with open("datos_deportes_scz.geojson", "w") as f:
    json.dump(geojson, f, indent=4, ensure_ascii=False)


"""
Ejemplo una feature dentro de un archivo geojson
 "features": [
        {
            "type": "Feature",
            "id": "museos.21",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    -68.13328259,
                    -16.49520314
                ]
            },
            "geometry_name": "geom",
            "properties": {
                "Nombre": "Academia Boliviana de Historia Militar",
                "Direccion": "Pza. Murillo, Lado Cine Plaza",
                "Zona": "Casco Viejo",
                "distrito": 1
            }
        },
    ]
"""