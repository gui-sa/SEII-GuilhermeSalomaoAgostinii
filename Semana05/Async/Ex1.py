import asyncio 
import time

async def funcao():
    print(f"Iniciou: {time.strftime('%X')}")
    task1 = asyncio.create_task(outrafuncao1()) 
    task2 = asyncio.create_task(outrafuncao2())
    print(f"Terminou: {time.strftime('%X')}")
    
    await task1
    await task2


async def outrafuncao1():
    print(f"Iniciou Outrafuncao1: {time.strftime('%X')}")
    await asyncio.sleep(1)
    print("Minhas mensagem 1")

async def outrafuncao2():
    await asyncio.sleep(1)
    print("Minhas mensagem 2")


asyncio.run(funcao())