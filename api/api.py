from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()

# Для запросов от фронтенда
origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Данные с бирж о паре из заголовка, например http://localhost:5438/check/BTC-USDT
from checker.base import check_return
@app.get("/check/{pair}", tags=["/check/{pair}"])
async def read_root(pair: str,  request: Request):
    cryp1 = pair.split('-')[0]
    cryp2 = pair.split('-')[1]
    data = check_return.check_return(cryp1, cryp2)
    return data

'''@app.get("/{item_id}")
def read_root(item_id: str, request: Request):
    client_host = request.client.host
    return {"client_host": client_host, "item_id": item_id}'''