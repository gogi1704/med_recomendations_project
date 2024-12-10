from openai import OpenAI
from dotenv import load_dotenv
import openai
import os


load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()

system = """
Ты опытный терапевт.Ты работаешь в компании ООО ,,Человек,, Ты всегда ответственно подходишь к своей работе. 
Тебе будет передана жалоба на здоровье от пациента а так же небольшой диалог с пациентом.Твоя задача на основе 
полученныч данных выдать рекомендации по улучшению здоровья пациента.
"""



def get_recomendations(topic , user_info):
    user =f"""
Жалоба пациента: {topic}
Диалог с пациентом:
{user_info}

"""
    messages =[
                {"role": "system", "content": system},
                {"role": "user", "content": f"{user}" }
                ]
    
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    return completion.choices[0].message.content

