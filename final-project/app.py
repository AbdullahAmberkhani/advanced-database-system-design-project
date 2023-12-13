from bottle import Bottle, template, request, redirect
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = 'sqlite:///database.db'
Base = declarative_base()

class Spacecraft(Base):
    __tablename__ = 'spacecraft'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    manufacturer = Column(String, nullable=False)
    missions = relationship('Mission', back_populates='spacecraft')

class Mission(Base):
    __tablename__ = 'mission'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    spacecraft_id = Column(Integer, ForeignKey('spacecraft.id'))
    spacecraft = relationship('Spacecraft', back_populates='missions')

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

app = Bottle()

@app.route('/')
def index():
    return template('index')

@app.route('/spacecraft')
def spacecraft_list():
    session = Session()
    spacecraft_list = session.query(Spacecraft).all()
    return template('spacecraft_list', spacecraft_list=spacecraft_list)

@app.route('/spacecraft/add', method='GET')
def spacecraft_add_form():
    return template('spacecraft_add')

@app.route('/spacecraft/add', method='POST')
def spacecraft_add():
    name = request.forms.get('name')
    manufacturer = request.forms.get('manufacturer')

    session = Session()
    new_spacecraft = Spacecraft(name=name, manufacturer=manufacturer)
    session.add(new_spacecraft)
    session.commit()

    redirect('/spacecraft')

@app.route('/mission')
def mission_list():
    session = Session()
    mission_list = session.query(Mission).all()
    return template('mission_list', mission_list=mission_list)

@app.route('/mission/add', method='GET')
def mission_add_form():
    session = Session()
    spacecraft_list = session.query(Spacecraft).all()
    return template('mission_add', spacecraft_list=spacecraft_list)

@app.route('/mission/add', method='POST')
def mission_add():
    name = request.forms.get('name')
    destination = request.forms.get('destination')
    spacecraft_id = request.forms.get('spacecraft_id')

    session = Session()
    new_mission = Mission(name=name, destination=destination, spacecraft_id=spacecraft_id)
    session.add(new_mission)
    session.commit()

    redirect('/mission')


# Route to delete spacecraft
@app.route('/spacecraft/delete/<id>', method='GET')
def spacecraft_delete(id):
    with Session() as session:
        spacecraft = session.query(Spacecraft).filter_by(id=id).first()
        if spacecraft:
            session.delete(spacecraft)
            session.commit()

    redirect('/spacecraft')

# Route to delete mission
@app.route('/mission/delete/<id>', method='GET')
def mission_delete(id):
    with Session() as session:
        mission = session.query(Mission).filter_by(id=id).first()
        if mission:
            session.delete(mission)
            session.commit()

    redirect('/mission')

# Route to edit spacecraft
@app.route('/spacecraft/edit/<id>', method='GET')
def spacecraft_edit_form(id):
    with Session() as session:
        spacecraft = session.query(Spacecraft).filter_by(id=id).first()
        return template('spacecraft_edit', spacecraft=spacecraft)

@app.route('/spacecraft/edit/<id>', method='POST')
def spacecraft_edit(id):
    new_name = request.forms.get('name')
    new_manufacturer = request.forms.get('manufacturer')

    with Session() as session:
        spacecraft = session.query(Spacecraft).filter_by(id=id).first()
        if spacecraft:
            spacecraft.name = new_name
            spacecraft.manufacturer = new_manufacturer
            session.commit()

    redirect('/spacecraft')

    # Route to edit mission
@app.route('/mission/edit/<id>', method='GET')
def mission_edit_form(id):
    with Session() as session:
        mission = session.query(Mission).filter_by(id=id).first()
        spacecraft_list = session.query(Spacecraft).all()
        return template('mission_edit', mission=mission, spacecraft_list=spacecraft_list)

@app.route('/mission/edit/<id>', method='POST')
def mission_edit(id):
    new_name = request.forms.get('name')
    new_destination = request.forms.get('destination')
    new_spacecraft_id = request.forms.get('spacecraft_id')

    with Session() as session:
        mission = session.query(Mission).filter_by(id=id).first()
        if mission:
            mission.name = new_name
            mission.destination = new_destination
            mission.spacecraft_id = new_spacecraft_id
            session.commit()

    redirect('/mission')


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
