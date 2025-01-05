from sqlalchemy import Column, BigInteger, String, Date, Integer, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    duration = Column(Integer, nullable=False) # minutes
    released_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    rating = Column(String, nullable=True)

    def __repr__(self):
        return f"<Movie {self.title}: description {self.description} >"
