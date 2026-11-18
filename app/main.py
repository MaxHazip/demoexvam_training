from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.core.database import get_session

app = FastAPI(title="Конференции.РФ")

@app.get(
    path="/"
)
async def test_endpoint(
    session: AsyncSession = Depends(get_session)
):

    result = (await session.execute(text("SELECT 1"))).scalar_one()

    if result == 1:
        return {"Message": "OK"}