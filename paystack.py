import sys
sys.path.append("./")
import os
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI,Request
from pprint import pprint





access_token = os.getenv("PAYSTACK_TOKEN")


def temp():
    try:
        pass
    except Exception as e:
        print(e.args)
        return {"code":500,"message":"internal server error","success":False}
    

app = FastAPI()


@app.post("/funding/completed")
async def USSDWebhooks(request: Request):

    output = await request.json()
    pprint(output)
    

