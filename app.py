from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

@app.route('/payments', methods=['POST'])
def create_payment():
    data = request.get_json()
    new_payment = Payment(
        user_id=data['user_id'],
        amount=data['amount'],
        status=data['status']
    )
    db.session.add(new_payment)
    db.session.commit()
    return jsonify({"message": "Payment created"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5003)

