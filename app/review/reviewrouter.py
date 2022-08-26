from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from models.usermodels import User
from dto.reviewschema import ReviewCreate
from config.token import get_currentUser
from .reviewservice import ReviewService

router = APIRouter(prefix="/review", tags=["Review"])


@router.get("/")
def getAllReview(db: Session = Depends(get_db)):
    return ReviewService.get_all(db=db)


@router.post("/create/{productid}")
def createReview(
    productid: int,
    request: ReviewCreate,
    db: Session = Depends(get_db)):
    return ReviewService.create_review(
        request=request, productId=productid, db=db
    )


@router.post("/coba")
def cobaReview(request: ReviewCreate):
    return request

