from pydantic import BaseModel


class Push(BaseModel):
    user_id: str | None = None
    message: str


class Keys(BaseModel):
    auth: str
    p256dh: str


class Subscription(BaseModel):
    endpoint: str
    expirationTime: str | None = None
    keys: Keys


class Register(BaseModel):
    user_id: str | None = None
    subscription: Subscription
