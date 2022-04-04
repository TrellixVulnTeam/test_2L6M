from turtle import title
from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI(
    title="テストAPI",
    description="テスト用のAPIです。",
    version="1.0.0"
)

class TestRequest(BaseModel):
    param1: str = Field("", title="パラメータ１", description="これはテスト用のパラメータ１です。", example="aaass")
    param2: Optional[str] = Field("", title="パラメータ２", description="これはテスト用のパラメータ２です。", example="bbbb")

class TestResponse(BaseModel):
    param3: Optional[list[str]] = None
    param4: Optional[str] = None

@app.post("/test", response_model=TestResponse, summary="サマリです", description="テストです。")
async def test(req: TestRequest = Body(None, title="req", description="これはテスト用のリクエストデータです。")):
    print(req)
    res: TestResponse = TestResponse()
    res.param3 = ["a", "b", "c"]
    res.param4 = "ddd"
    return res
