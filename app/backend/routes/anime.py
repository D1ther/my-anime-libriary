from flask import (
    request
)

from app.backend.db.requests import (
    add_anime
)

from app import (
    app
)

import base64

@app.post('/api/add_anime')
def add_anime_request():
    data = request.get_json()

    title = data['title']
    description = data['description']
    rating = data['rating']
    image = base64.b64decode(data['image'])

    return add_anime(title, description, rating, image)