from werkzeug.security import generate_password_hash
from models import db, User, Product
from csv import DictReader


def populate_db():
  db.session.add(User(
      name="Admin",
      email="admin@example.com",
      password=generate_password_hash("12345"),
      role="admin"
  ))

  db.session.add(User(
      name="Manager",
      email="manager@example.com",
      password=generate_password_hash("12345"),
      role="manager"
  ))

  with open("./sample_data/products.csv") as f:
    for product in DictReader(f):
      db.session.add(Product(
          name=f"{product["name"]}",
          cost_price=product["cost_price"],
          selling_price=product["selling_price"],
          qty=product["qty"],
      ))

  db.session.commit()
