# Evaluación 2 Telepresencia y entornos innovadores de colaboración humana_004D 
## Autores intelectuales
  -Martin Contreras
  
  -José Parra
##

Proyecto realizado para la evaluacion n°2 de Telepresencia. Consiste en un script que recopila informacion con la API de graphhopper, que permite al usuario ingresar una ubicacion de origen y de destino para mostrar: la distancia, instrucciones paso a paso en español y tiempo estimado del recorrido.

A Continuacion se explicara todo lo necesario para ejecutar el script.
##
===========================================================================
## Requisitos del Sistema Operativo
-Conexión a internet

-Tener Python 3

-Una API key obtenida gratis desde la url (https://graphhopper.com/)
##
===========================================================================

## Instalación previa de las dependencias
Como primer requisito se necesita tener el modulo "requests" en python el cual puedes instalar desde la consola : pip install requests.

pip install requests
##
## Como ejecutar el script 
1. Abre tu terminal 
2. Ve hasta la carpeta "Prueba2-Martin-José" .
3. Ejecuta el script con el siguiente comando:

python3 Prueba2-Martin-José.py
##
## Instrucciones 

-El programa te solicitara que ingreses: *Tipo de Vehiculo* ('car', 'bike', 'foot').

-Luego ingresa la **ubicacion de origen** y la  **ubicacion de destino**.

-El script te mostrara :
  - Las **Instrucciones paso a paso en español**
  - Las coordenadas geograficas obtenidas por el geocodificador.
  - La distancia total del recorrido (en km y millas).
  - La duracion del viaje.
    
Para salir del programa escribe 's' o 'salir'.

---
