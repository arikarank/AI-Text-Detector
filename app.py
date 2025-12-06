from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# --- Config ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # change this in real deployment

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# --- Load LSTM model and tokenizer ---
# Make sure these files exist in the project root on Render as well
model = load_model('ai_detection_lstm_model.h5')
with open('tokenizer.pkl', 'rb') as file:
    tokenizer = pickle.load(file)

MAXLEN = 100  # Same as training


# --- User model ---
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# 👇 IMPORTANT: create tables on import (so it works with gunicorn on Render)
with app.app_context():
    db.create_all()


# --- Routes ---
@app.route('/')
def home():
    # If you want to redirect logged-in users:
    # if current_user.is_authenticated:
    #     return redirect(url_for('predict_page'))
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        raw_password = request.form['password']

        if not username or not raw_password:
            flash("Username and password are required.", "error")
            return redirect(url_for('register'))

        password = bcrypt.generate_password_hash(raw_password).decode('utf-8')

        # Check if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Try another one.", "error")
            return redirect(url_for('register'))

        # Create new user
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))  # Redirect to login after registration

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for('predict_page'))  # Redirect to predict.html after login
        else:
            flash("Invalid username or password. Try again.", "error")
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('login'))


@app.route('/predict_page')
@login_required
def predict_page():
    return render_template('predict.html')


@app.route('/predict', methods=['POST'])
@login_required
def predict():
    # Support both JSON and form submissions
    text = request.json.get('text') if request.is_json else request.form.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    sequences = tokenizer.texts_to_sequences([text])
    data = pad_sequences(sequences, maxlen=MAXLEN)

    prediction = model.predict(data)
    probability = float(prediction[0][0])

    result = "AI-generated" if probability >= 0.5 else "Human-generated"

    return jsonify({'prediction': result, 'probability': probability})


# Local dev entrypoint (Render uses gunicorn instead)
if __name__ == '__main__':
    # db.create_all() is already called above on import
    app.run(debug=True)
