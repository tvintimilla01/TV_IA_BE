from cook_api import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    ingredients = db.Column(db.String(100), nullable=False)
    steps = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    favorite = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Event %r>' % self.name

    def __init__(self, name, ingredients, steps, rating, favorite):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        if rating > 0 and rating < 6:
            self.rating = rating
        else:
            self.rating = 1
        self.favorite = favorite
