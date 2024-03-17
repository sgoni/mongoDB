# mongoDB
Proyecto de aprendizaje integracion de Mongo. Python, Linux

Configurar entorno virtual e instalacion del driver pymongo

// Instalar componente
sudo apt install python3.10-venv

// crear entorno virtual
python3 -m venv mongo   

// Opcional: Crear alias en Linux
alias python=python3

// Activar el entorno virtual
source mongo/bin/activate  or .  mongo/bin/activate

// Instalar pymongo
python -m pip install pymongo o, python -m pip install pymongo[srv]

// Validar instalacion del driver de Python
from pymongo import MongoClient
