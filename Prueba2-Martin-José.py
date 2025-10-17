import requests
import urllib.parse
##Martin Contreras
##Jose Parra 
route_url = "https://graphhopper.com/api/1/route?"
key = "e91d197b-d985-4941-836f-1e1223b2c7ff"

def geocoding(location, key):
    while location == "":
        location = input("Porfavor, ingrese la ubicacion nuevamente: ")

    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q": location, "limit": "1", "key": key})

    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code

    if json_status == 200 and len(json_data["hits"]) != 0:
        lat = json_data["hits"][0]["point"]["lat"]
        lng = json_data["hits"][0]["point"]["lng"]
        name = json_data["hits"][0]["name"]

        country = json_data["hits"][0].get("country", "")
        state = json_data["hits"][0].get("state", "")

        if state and country:
            new_loc = f"{name}, {state}, {country}"
        elif country:
            new_loc = f"{name}, {country}"
        else:
            new_loc = name

        print(f"URL de geocodificacion para {new_loc}\n{url}")
    else:
        lat = 'null'
        lng = 'null'
        new_loc = location
        if json_status != 200:
            print("Estado de la API de geocodificacion: " + str(json_status) + "\nError message: " + json_data.get('message', 'sin message'))

    return json_status, lat, lng, new_loc

while True:
    print("========================================")
    print("Perfiles de vehiculo disponibles en Graphhopper")
    print("========================================")
    print("car(coche), bike(bicicleta), foot(a pie)")
    print("========================================")
    profile=["car", "bike", "foot"]
    vehicle = input("Ingrese una de las opciones anteriores, si desea salir escriba s o salir: ")
    if vehicle == "salir" or vehicle == "s":
        break
    if vehicle in profile:
        vehicle = vehicle
    else:
        vehicle = "car"
        print("No se ingreso un perfil valido. Se usara el perfil por defecto:coche ")
    
    loc1 = input("Origen: ")
    if loc1 == "salir" or loc1 == "s":
        break
    orig = geocoding(loc1, key)
    print(orig)
    loc2 = input("Destino: ")
    if loc2 == "salir" or loc2 == "s":
        break
    dest= geocoding(loc2, key)
    print("========================================")
    if orig[0] ==200 and dest[0] == 200:
            op="&point="+str(orig[1])+"%2C"+str(orig[2])
            dp="&point="+str(dest[1])+"%2C"+str(dest[2])
            paths_url = route_url + urllib.parse.urlencode({"key":key, "vehicle":vehicle, "locale": "es" }) + op + dp
            paths_status = requests.get(paths_url).status_code
            paths_data = requests.get(paths_url).json()
            print("Estado de la API de rutas: " + str(paths_status) + "\nURL de la API de rutas:\n" + paths_url)
            print("========================================")
            print("Direcciones desde " + orig[3] + " hasta " + dest[3] + " perfil usado: " + vehicle)
            print("========================================")
            if paths_status == 200:
                miles = (paths_data["paths"][0]["distance"])/1000/1.61
                km = (paths_data["paths"][0]["distance"])/1000
                sec = int(paths_data["paths"][0]["time"]/1000%60)
                min = int(paths_data["paths"][0]["time"]/1000/60%60)
                hr = int(paths_data["paths"][0]["time"]/1000/60/60)

                print("Distancia total: {0:.1f} miles / {1:.1f} km".format(miles, km))

                print("Duracion del viaje: {0:02d}:{1:02d}:{2:02d}".format(hr, min, sec))
                print("========================================")
                for each in range(len(paths_data["paths"][0]["instructions"])):
                    path = paths_data["paths"][0]["instructions"][each]["text"]
                    distance = paths_data["paths"][0]["instructions"][each]["distance"]
                    print("{0} ( {1:.1f} km / {2:.1f} miles )".format(path, distance/1000, distance/1000/1.61))
                print("========================================")
            else:
                print("Mensaje de error: " + paths_data["message", "Sin mensaje disponible."])
                print("*************************************************")
