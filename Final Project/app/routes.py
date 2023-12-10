from flask import Flask, render_template, request, redirect, url_for
from .models import db, Planet, Spacecraft

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.route('/')
def index():
    planets = Planet.query.all()
    spacecrafts = Spacecraft.query.all()
    return render_template('index.html', planets=planets, spacecrafts=spacecrafts)

@app.route('/create_planet', methods=['GET', 'POST'])
def create_planet():
    if request.method == 'POST':
        planet = Planet(
            name=request.form['planet_name'],
            description=request.form['planet_description']
        )
        db.session.add(planet)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_planet.html')

@app.route('/create_spacecraft', methods=['GET', 'POST'])
def create_spacecraft():
    if request.method == 'POST':
        spacecraft = Spacecraft(
            name=request.form['spacecraft_name'],
            mission_description=request.form['spacecraft_mission'],
            planet_id=request.form['planet_id']
        )
        db.session.add(spacecraft)
        db.session.commit()
        return redirect(url_for('index'))
    planets = Planet.query.all()
    return render_template('create_spacecraft.html', planets=planets)

@app.route('/update_spacecraft/<int:spacecraft_id>', methods=['GET', 'POST'])
def update_spacecraft(spacecraft_id):
    spacecraft = Spacecraft.query.get_or_404(spacecraft_id)
    if request.method == 'POST':
        spacecraft.name = request.form['spacecraft_name']
        spacecraft.mission_description = request.form['spacecraft_mission']
        spacecraft.planet_id = request.form['planet_id']
        db.session.commit()
        return redirect(url_for('index'))
    planets = Planet.query.all()
    return render_template('update_spacecraft.html', spacecraft=spacecraft, planets=planets)

@app.route('/delete_spacecraft/<int:spacecraft_id>')
def delete_spacecraft(spacecraft_id):
    spacecraft = Spacecraft.query.get_or_404(spacecraft_id)
    db.session.delete(spacecraft)
    db.session.commit()
    return redirect(url_for('index'))
