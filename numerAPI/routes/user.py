from fastapi import APIRouter
from config.db import conn

user = APIRouter()

@user.get("/api/bisection")
def getBisecData(request):
    return conn.local.user.find()