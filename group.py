from pymongo import MongoClient
import pprint
  # conexion
CONEXION_LOCAL="mongodb://admin:lepanto@localhost"
CONEXION_ATLAS = "mongodb+srv://admin:lepanto@cluster0.1jkwhhs.mongodb.net/?retryWrites=true&w=majority"
 
   # Usamos MongoClient para conectarnos
cliente = MongoClient(CONEXION_ATLAS)
 
# Accedemos a la base de datos
dbname=cliente['sample_airbnb']

# Coleccion a usar
propiedades=dbname['listingsAndReviews']

# Vamos a agrupar por tipo de Propiedad y averiguar el precio medio
grupo={"$group": {"_id": "$property_type","precio_medio": {"$avg":"$price"}}}

# Crear la tuberia
tuberia=[grupo]

# Lanzar el aggregate
resultados=propiedades.aggregate(tuberia)

# Visualizar el resultado
for elemento in resultados:
   # pprint.pprint(elemento)
    print(elemento['_id']+"  "+str(elemento['precio_medio']))