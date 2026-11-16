# 요청 및 응답 데이터의 형식을 정의한다.

from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


class CheckRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    question: str = Field(min_length=1, max_length=4000)
    answer: str = Field(min_length=1, max_length=12000)


class Evaluation(BaseModel):
    accuracy: Literal[
        "correct",
        "incorrect",
        "partially_correct",
        "unverifiable",
    ]
    relevance: Literal[
        "relevant",
        "partially_relevant",
        "irrelevant",
    ]
    reason: str


class Source(BaseModel):
    title: str
    url: str


class CheckResponse(Evaluation):
    sources: list[Source]
