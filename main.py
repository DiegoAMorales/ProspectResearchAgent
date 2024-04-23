from fastapi import FastAPI
from pydantic import BaseModel
import agent
import json

class Item(BaseModel):
    email: str

app = FastAPI()

@app.post("/research-agent/")
async def create_item(item: Item):
    item_dict = json.loads(item.model_dump_json())
    email = item_dict["email"]
    company_info = agent.main(email)
    return company_info