from bottle import Bottle, run, template, request, redirect
import sqlite3

app = Bottle()

conn = sqlite3.connect('vehicle_companion.db')
cursor = conn.cursor()

@app.route('/')
def index():
    search_term = request.query.get('search', '')
    query = '''
    SELECT vehicles.id, vehicles.title, vehicles.release_year, companions.name
    FROM vehicles
    JOIN companions ON vehicles.companion_id = companions.id
    WHERE vehicles.title LIKE ? OR companions.name LIKE ?
    '''
    cursor.execute(query, (f'%{search_term}%', f'%{search_term}%'))
    result = cursor.fetchall()
    return template('index', vehicles=result)

@app.route('/add')
def add_form():
    cursor.execute('SELECT * FROM companions')
    companions = cursor.fetchall()
    return template('insert', companions=companions)

@app.route('/add', method='POST')
def add():
    title = request.forms.get('title')
    release_year = request.forms.get('release_year')
    companion_id = request.forms.get('companion_id')
    cursor.execute("INSERT INTO vehicles (title, release_year, companion_id) VALUES (?, ?, ?)",
                   (title, release_year, companion_id))
    conn.commit()
    redirect('/')

@app.route('/edit/<vehicle_id>')
def edit_form(vehicle_id):
    cursor.execute("SELECT * FROM vehicles WHERE id=?", (vehicle_id,))
    vehicle = cursor.fetchone()
    cursor.execute('SELECT * FROM companions')
    companions = cursor.fetchall()
    return template('edit', vehicle=vehicle, companions=companions)

@app.route('/edit/<vehicle_id>', method='POST')
def edit(vehicle_id):
    title = request.forms.get('title')
    release_year = request.forms.get('release_year')
    companion_id = request.forms.get('companion_id')
    cursor.execute("UPDATE vehicles SET title=?, release_year=?, companion_id=? WHERE id=?",
                   (title, release_year, companion_id, vehicle_id))
    conn.commit()
    redirect('/')

@app.route('/delete/<vehicle_id>')
def delete(vehicle_id):
    cursor.execute("DELETE FROM vehicles WHERE id=?", (vehicle_id,))
    conn.commit()
    redirect('/')

if __name__ == '__main__':
    run(app, host='localhost', port=8090)
