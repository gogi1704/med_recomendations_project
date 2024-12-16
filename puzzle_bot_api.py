from dotenv import load_dotenv
import os
import asyncio
import aiohttp

load_dotenv()

puzzle_token = os.environ.get('PUZZLE_TOKEN')
var_name_neuro_recs = 'neuro_recs'

command_name_neuro_recs = "/neuro_var"
command_name_error = "/neuro_error"

async def change_var_puzzle(user_id , var_value):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(sock_connect=30, sock_read=30)) as session:
            payload = {
                'variable': var_name_neuro_recs,
                'expression': f"\"{var_value}\"",
                'user_id': user_id
               
               }
            async with session.post(f'https://api.puzzlebot.top/?token={puzzle_token}&method=variableChange', json=payload) as resp:         
                text_json = await resp.json()
            
                print(f"Изменение переменной - {text_json}")

                return text_json
            
async def send_command_neuro_recs(user_id):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(sock_connect=30, sock_read=30)) as session:
            payload = {
                'command_name': command_name_neuro_recs,
                'tg_chat_id': user_id
               
               }
            async with session.post(f'https://api.puzzlebot.top/?token={puzzle_token}&method=sendCommand', json=payload) as resp:         
                text_json = await resp.json()
            
                print(f"Отправка команды рекомендации - {text_json}")

                return text_json
            
async def send_command_error(user_id):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(sock_connect=30, sock_read=30)) as session:
            payload = {
                'command_name': command_name_error,
                'tg_chat_id': user_id
               
               }
            async with session.post(f'https://api.puzzlebot.top/?token={puzzle_token}&method=sendCommand', json=payload) as resp:         
                text_json = await resp.json()
            
                print(f"Отправка команды ошибка рекомендаций - {text_json}")

                return text_json
            