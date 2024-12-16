from openai import OpenAI
from dotenv import load_dotenv
import openai
import os


load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI()

system = """
Ты лучший терапевт.Ты строго выполняешь поставленную задачу. 
Тебе будут передана анкета пациента а также его жалоба на здоровье
с несколькими вопросами и ответами на них.
Твоя задача проанализироввать полученную информацию и предоставить информацию о 
возможных заболеваниях . Рекомендации предоставлять не нужно.
"""



async def get_zhaloba_result(user_anketa , zhaloba):
    user =f"""
Анкетта пациента: {user_anketa}
Вопросы по здоровью и ответы пациента: {zhaloba}

Во время анализа и обязательно обращай внимание на анкету пациента . 
В частности на его вес , возраст и другое. 
Если у пациента есть проблемы с весом то обязательно укажи на это и посчитай индекс массы тела пациента.
Ответ дай в таком формате : 

Проблемы исходя из анкеты : ...
Возможные заболевания : ...
"""
    messages =[
                {"role": "system", "content": system},
                {"role": "user", "content": f"{user}" }
                ]
    print("openai start")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    return completion.choices[0].message.content

