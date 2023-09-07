from typing import Union
from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pywebpush import webpush, WebPushException
from uuid import uuid4
import ujson
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from os import getenv
import multiprocessing
from custom_types import Push, Keys, Subscription, Register
from contextlib import asynccontextmanager

tags_metadata = [
    {
        "name": "client",
        "description": "Operations for clients.",
    },
    {
        "name": "server",
        "description": "Operations for the server.",
    },
]

# pool = None


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global pool
#     pool = multiprocessing.Pool(
#         multiprocessing.cpu_count()
#     )  # create a pool of processesm
#     yield
#     pool.close()
#     pool.join()
#     pool.terminate()


app = FastAPI(
    title="WebPush",
    openapi_tags=tags_metadata,
    #    lifespan=lifespan
)

app.mount("/server", StaticFiles(directory="static/server", html=True), name="server")
app.mount("/client", StaticFiles(directory="static/client", html=True), name="client")


origins = [
    "http://localhost",
    "http://127.0.0.1:5501",
    "http://localhost:8000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
    "http://127.0.0.1:8000",
    "https://web-push-client.mehdiabdi.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# read keys
with open("./public_key.pem") as file:
    public_key = file.read()

with open("./private_key.pem") as file:
    private_key = file.read()


subscriptions_in_db = {}


def send_webpush(subscription_info, message, private_key, vapid_claims):
    webpush(
        subscription_info=subscription_info,
        data=message,
        vapid_private_key=private_key,
        vapid_claims=vapid_claims,
    )


@app.post("/push", tags=["server"])
async def push(data: Push, background_tasks: BackgroundTasks):
    if data.user_id:
        webpush(
            subscription_info=subscriptions_in_db.get(data.user_id),
            data=data.message,
            vapid_private_key=private_key,
            vapid_claims={
                "sub": f"mailto: {getenv('SUBJECT', 'mailto: <example@gmail.com>')}",
            },
        )
        return "done"
    else:
        for subs in subscriptions_in_db.values():
            try:
                background_tasks.add_task(
                    send_webpush,
                    subs,
                    data.message,
                    private_key,
                    {
                        "sub": f"mailto: {getenv('SUBJECT', 'mailto: <example@gmail.com>')}",
                    },
                )
            except Exception as exc:
                print(exc.args)
                continue

        return "done"


@app.post("/register", status_code=201, tags=["client"])
def read_item(data: Register):
    subscriptions_in_db[
        data.user_id if data.user_id else uuid4().hex
    ] = data.subscription.model_dump()
    return "ok"


@app.get("/vapidPublicKey", tags=["client"])
async def read_item():
    return public_key


@app.get("/")
def home_page():
    return RedirectResponse("/server")


@app.get("/client")
def home_page():
    return RedirectResponse("/client")
