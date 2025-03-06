from flask import (
    jsonify
)

from app.backend.db.base import (
    Session
)

from app.backend.db.models import (
    Anime
)

def add_anime(title, description, rating, image):
    with Session() as session:
        anime = Anime(
            title=title,
            description=description,
            rating=rating,
            image=image
        )

        session.add(anime)
        session.commit()

        return jsonify({'message': 'Anime added successfully!'}), 200