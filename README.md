# Intro
Hola 👋 mi nombre es Felix Wong, y estoy cursando el bootcamp Henry - Data Science.

En este proyecto (PI01) vamos a desarrollar un proceso de ETL desde el IDE de visual studio code, usando Pandas(python), luego desarrollaremos la construcción de APIs con el framework FastAPI (python) y expondremos la salida de datos en un entorno cloud llamado Deta.

## Arquitectura de solución

En la siguiente imagen, se puede visualizar todos los componentes a desarrollar, así como la comunicación entre ellos y los frameworks a utilizar.
![Presentación1](https://user-images.githubusercontent.com/97036778/213478667-f26f0ea9-9648-45f5-aa5a-2abd87f70f73.jpg)

Iniciarmos con la lecutura de los CSVs usando Pandas, seguidamente estos pasan por un proceso de limpieza de datos (ver código en repositorio) para finalmente tener un archivo limpio y centralizado, el cual subiremos a Data Drive. A continuación, realizamos ciertas querys de interes para el ejercicio usando Pandas, las mismas que serán usadas para el desarrollo de las APIs.

Las APIs las vamos a desarrollar usando FastAPI (ver código en repositorio), y las expondremos usando Deta Micros. Los valores output de salida estan con formato json/int para asegurar la comunicación efectiva con el cliente que las requiera.

El código y archivos de carga los mantendremos en el repositorio de github para tener en cuenta versiones del mismo.
