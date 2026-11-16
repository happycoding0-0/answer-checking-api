# FastAPI 엔드포인트를 구현한다.
import logging

from fastapi import FastAPI, HTTPException

from checker import check_answer, VerificationError
from schemas import CheckRequest, CheckResponse

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Answer Checking API",
    description="생성형 AI 답변의 정확성과 맥락적 적절성을 평가하는 API",
    version="0.1.0",
)


@app.post("/check", response_model=CheckResponse)
def check(request: CheckRequest) -> CheckResponse:
    try:
        return check_answer(request)

    except VerificationError:
        logger.exception("Answer checking failed")

        raise HTTPException(
            status_code=502,
            detail="답변 검증 처리에 실패했습니다.",
        )


@app.get("/health")
def health():
    return {"status": "ok"}
