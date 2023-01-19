from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from deta import Deta
import pandas as pd
import numpy as np




################## inicio: lineas de codigo para poder usar Deta Drive###############

app = FastAPI()
deta = Deta("e0di40mo_7WonBA1mRSu16ZZX9VyyFxnk4Cw79ME2")  # configure your Deta project 
drive = deta.Drive("Archivos")


@app.get("/", response_class=HTMLResponse)
def render():
    return """
    <form action="/upload" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>
    """

@app.post("/upload")
def upload_img(file: UploadFile = File(...)):
    name = file.filename
    f = file.file
    res = drive.put(name, f)
    return res

@app.get("/download/{name}")
def download_file(name: str):
    res = drive.get(name)
    return StreamingResponse(res.iter_chunks(1024), media_type="text/csv")

################## fin: lineas de codigo para poder usar Deta Drive###############

################## inicio: desarrollo de APIs ######################
#obtener información de los datos 
movie_db = pd.read_csv(drive.get("movie_db.csv"))

#api n°1
@app.get("/get_word_count/{plataforma}/{keyword}")
def get_word_count(plataforma, keyword):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}

    df_temp = movie_db[(movie_db.show_id.str[0] == dicc[plataforma])&(movie_db['title'].str.contains(keyword, na=False))]
    data = df_temp.groupby(df_temp.show_id.str[0]).count().iloc[:,0]
    data = data.rename_axis("Cantidad").rename({v: k for k, v in dicc.items()})
     
    return data.to_dict()


#prueba unitaria: get_word_count("netflix","love")

#api n°2
@app.get("/get_score_count/{plataforma}/{puntaje}/{anio}")
def get_score_count(plataforma:str,puntaje:int,anio:int):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}

    df_temp = movie_db[(movie_db["score"]>puntaje)&(movie_db["release_year"]==anio)&(movie_db.show_id.str[0] == dicc[plataforma])&(movie_db["type"] == "movie")]
    data = df_temp.groupby(df_temp.show_id.str[0]).count().iloc[:,0]
    data = data.rename_axis("Cantidad").rename({v: k for k, v in dicc.items()})
    return data.to_dict()

#prueba unitaria: get_score_count("netflix",85,2010)

#api n°3
@app.get("/get_second_score/{plataforma}")
def get_second_score(plataforma:str):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}

    df_temp = movie_db[(movie_db.show_id.str[0] == dicc[plataforma])&(movie_db.type == "movie")].sort_values(["score","title"],ascending=[False,True]).reset_index(drop=True)
    df_temp = df_temp[["title","score"]].iloc[1,:]
    return df_temp.to_dict()

#prueba unitaria: get_second_score("amazon")


#api n°4
@app.get("/get_longest/{plataforma}/{tipo_duracion}/{anio}")
def get_longest(plataforma:str,tipo_duracion:str,anio:int):
    dicc = {"netflix":"n","amazon":"a","hulu":"h","disney_plus":"d"}

    temp = movie_db[(movie_db.show_id.str[0] == dicc[plataforma])&(movie_db.release_year == anio)&(movie_db.duration_type == tipo_duracion)&(movie_db.type == "movie")].sort_values(["duration_int"],ascending=False).reset_index(drop=True)[["title","duration_int","duration_type"]].iloc[0,:]
    return temp.to_dict()

#prueba unitaria: get_longest('netflix','min',2016)


#api n°5
@app.get("/get_rating_count/{rating_cat}")
def get_rating_count(rating_cat:str):
    return len(movie_db[movie_db["rating"]==rating_cat])

@app.get("/prueba/")
def prueba(palabra:str,numero:int):
    return print(palabra,numero)
#prueba unitaria: get_rating_count('18+')
################## fin: desarrollo de APIs ######################