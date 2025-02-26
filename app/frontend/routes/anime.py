from flask import (
    render_template,
    request
)

from app.frontend.forms import (
    AddAnime
)

from app import app

@app.route('/add_anime', methods=['GET', 'POST'])
def add_anime():
    form = AddAnime()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.title.data
            description = form.description.data
            rating = form.rating.data
            image = form.image.data

            return render_template('add_anime.html', form=form)
    return render_template('add_anime.html', form=form)