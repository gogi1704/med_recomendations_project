from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import main
# import db.user_history_db as sql_db
# import baza.doctors_baza as doctors_baza
import os


# создаем объект приложения
app = FastAPI()
# sql_db.init_db()
# doctors_baza.load_doctors_baza()
# настройки для работы запросов
app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class AnswerRequest(BaseModel):
    topic:str
    text_answer:str


class AnswerRecomendationRequest(BaseModel):
    telegram_user_id:str
    user_anketa:str
    user_zhaloba:str  

class AnswerIsZhalobaValidRequest(BaseModel):
    telegram_user_id:str
    zhaloba_text:str

# @app.post("/api/get_recomendations")
# async def get_recomendations(request: AnswerRequest):
#     try:
#         text = await main.get_recomendations(request.topic , request.text_answer)
#         print(text)
#         return {"message": text}
    
#     except Exception as e:
#          print(e)
#          return {"message": "Error "+ str(e)}
    



@app.post("/api/get_recs")
async def get_recs(request: AnswerRecomendationRequest):
    try:
        await main.get_recs(request.telegram_user_id , request.user_anketa , request.user_zhaloba)
    
    except Exception as e:
         print(e)
        #  return {"message": "Error "+ str(e)}


# @app.post("/api/is_zhaloba_valid")
# async def is_zhaloba_valid(request: AnswerIsZhalobaValidRequest):
#     try:
#         await main.is_zhaloba_valid(request.telegram_user_id , request.zhaloba_text)
    
#     except Exception as e:
#          print(e)
        #  return {"message": "Error "+ str(e)}

        
