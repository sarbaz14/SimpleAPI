# In the name of Allah

import datetime
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/factorial/{num}")
def showFactorial(num:int):
    return {"number": num, "factorial": factorial(num)}

def factorial(num:int):
    if num < 0:
        return -1
    
    fact = 1
    for i in range(1,num + 1):
        fact *= i
    return fact


@app.get("/whoami")
def client_ip_time(request: Request):
    ip = request.client.host
    time = datetime.datetime.now()
    return {"client": ip, "time": time}

