# Intro
Hola 馃憢 mi nombre es Felix Wong, y estoy cursando el bootcamp Henry - Data Science.

En este proyecto (PI01) vamos a desarrollar un proceso de ETL desde el IDE de visual studio code, usando Pandas(python), luego desarrollaremos la construcci贸n de APIs con el framework FastAPI (python) y expondremos la salida de datos en un entorno cloud llamado Deta.

## Arquitectura de soluci贸n

En la siguiente imagen, se puede visualizar todos los componentes a desarrollar, as铆 como la comunicaci贸n entre ellos y los frameworks a utilizar.
![Presentaci贸n1](https://user-images.githubusercontent.com/97036778/213478667-f26f0ea9-9648-45f5-aa5a-2abd87f70f73.jpg)

Iniciamos con la lecutura de los CSVs usando Pandas, seguidamente estos pasan por un proceso de limpieza de datos (ver c贸digo en repositorio) para finalmente tener un archivo limpio y centralizado, el cual subiremos a Data Drive.

A continuaci贸n, realizamos ciertas querys de interes usando Pandas ser谩n usadas para las APIs.

Las APIs las vamos a desarrollar usando FastAPI (ver c贸digo en repositorio), y las expondremos usando Deta Micros. Los valores output de salida estan con formato json/int para asegurar la comunicaci贸n efectiva con el cliente que las requiera.

El c贸digo y archivos de carga los mantendremos en el repositorio de github para tener en cuenta versiones del mismo.

Link youtube: https://www.youtube.com/watch?v=tDRfW947ga4
