from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a la base de datos en AWS RDS
db_config = {
    "host": "database-privada.cfmk6ioegnq6.us-east-1.rds.amazonaws.com",  # Cambia esto por tu endpoint real
    "user": "admin",
    "password": "HexVault4802",
    "database": "sakila"
}

def get_db_connection():
    """Función para obtener la conexión a la base de datos."""
    return mysql.connector.connect(**db_config)

# Página de inicio
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index2():
    return render_template('index.html')

# Listado de películas
@app.route('/movies.html')
def movies():
    return render_template('movies.html')

# Detalles de una película específica
@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    return render_template('movie.html', movie_id=movie_id)

# Busqueda de peliculas
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    filter_type = request.args.get('filter')

    if not query:
        return jsonify({"error": "No query provided"}), 400

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if filter_type == "title":
        sql = "SELECT film_id, title, description FROM film WHERE title LIKE %s LIMIT 10"
        cursor.execute(sql, ('%' + query + '%',))
    elif filter_type == "actor":
        sql = """SELECT film.film_id, film.title, film.description
                 FROM film
                 JOIN film_actor ON film.film_id = film_actor.film_id
                 JOIN actor ON film_actor.actor_id = actor.actor_id
                 WHERE actor.first_name LIKE %s OR actor.last_name LIKE %s LIMIT 10"""
        cursor.execute(sql, ('%' + query + '%', '%' + query + '%'))
    else:
        cursor.close()
        connection.close()
        return jsonify([])

    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(results)

# Autenticación
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

# Gestión de compras
@app.route('/cart.html')
def cart():
    return render_template('cart.html')

@app.route('/cart/add/<int:movie_id>')
def add_to_cart(movie_id):
    return redirect(url_for('cart'))

@app.route('/cart/remove/<int:movie_id>')
def remove_from_cart(movie_id):
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/order/<int:order_id>')
def order_details(order_id):
    return render_template('order.html', order_id=order_id)

# Rutas de administración
@app.route('/admin/movies')
def admin_movies():
    return render_template('admin_movies.html')

@app.route('/admin/movies/add')
def add_movie():
    return render_template('add_movie.html')

@app.route('/admin/movies/edit/<int:movie_id>')
def edit_movie(movie_id):
    return render_template('edit_movie.html', movie_id=movie_id)

@app.route('/admin/movies/delete/<int:movie_id>')
def delete_movie(movie_id):
    return redirect(url_for('admin_movies'))

@app.route('/admin/orders')
def admin_orders():
    return render_template('admin_orders.html')

# Otras rutas
@app.route('/genres.html')
def genres():
    return render_template('genres.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
