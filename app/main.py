from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session

app = FastAPI(title="Конференции.РФ")

@app.get(
    path="/"
)
async def test_endpoint(
    session: AsyncSession = Depends(get_session)
):

    return {"Message": "OK"}