from sqlalchemy import (
    Integer,
    String,
    LargeBinary
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from app.backend.db.base import (
    Base
)

class Anime(Base):
    __tablename__ = 'anime'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    rating: Mapped[int] = mapped_column(Integer)
    image: Mapped[bytes] = mapped_column(LargeBinary)

    def __repr__(self):
        return f"<Anime(id={self.id}, title='{self.title}', decription='{self.decription}', rating={self.rating})>"

