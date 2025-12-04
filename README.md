Very basic inventory management application.

There is a single inventory. Only a single warehouse.

Containing lots of products.

Products are sold to some clients. Products are replenished by purchasing them from suppliers.

Two types of users will use the application. Admin user and manager.

Admin user will manage the list of products. And he will also approve orders.

Manager will place orders and update order status. Orders can be of two types, incoming and outgoing. Incoming orders are for when purchasing from suppliers. Outgoing orders are for when selling to clients.

Incoming order: Pending (Update inventory here), picked and delivered.
Outgoing order.: Pending and then delivered (Update inventory here).

Admin also has access to a summary statistics about products. We will show him a list of key performance indicators.

===

frontend
backend

backend/requirements.txt
flask
backend/app.py
backend/models.py

cd backend
python -m venv .venv
pip install -r requirements.txt
