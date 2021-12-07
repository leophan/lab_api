from api.models.sqla import db


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String(255))
    product_id = db.Column(db.Integer())
    units_sold = db.Column(db.Integer())


    def __init__(self, date, product_id, units_sold) -> None:
        self.date = date
        self.product_id = product_id
        self.units_sold = units_sold


    def __repr__(self):
        return "['{}', {}, {}]".format(self.date, self.product_id, self.units_sold)
