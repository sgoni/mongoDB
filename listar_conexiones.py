from pymongo import MongoClient

# Conexion 
conexion_local = "mongodb://phantom:pu4lfruy59AxE@localhost"
conexion_atlas = "mongodb+srv://phantom:5MP7nIC6rB0wczMl@development.jyqjkpa.mongodb.net/?retryWrites=true&w=majority&appName=development"

# MongoClient para conectarnos

cliente = MongoClient(conexion_atlas)

# Crear la BD de pruebas
dbname = cliente['test']
#print(dbname)

#filter = {"name": {"$regex": r"^(?!system\.)"}}
#collections = dbname.list_collection_names(filter=filter)

collections = dbname.list_collection_names()
print(collections)

for collection in collections:
    print(collection)