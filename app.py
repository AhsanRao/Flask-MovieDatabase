from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'moviedb',
    'raise_on_warnings': True
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_director', methods=['GET', 'POST'])
def search_director():
    if request.method == 'POST':
        keyword = request.form['keyword']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the search query
        query = """
        SELECT Directors.Name, Directors.DateOfBirth, Movies.Title
        FROM Directors
        LEFT JOIN Movies ON Directors.DirectorID = Movies.DirectorID
        WHERE Directors.Name LIKE %s OR Directors.DateOfBirth LIKE %s OR Movies.Title LIKE %s
        """
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%',))
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        return render_template('results_directors.html', results=results)
    
    return render_template('search_directors.html')



@app.route('/search_producer', methods=['GET', 'POST'])
def search_producer():
    if request.method == 'POST':
        keyword = request.form['keyword']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the search query
        query = """
        SELECT Producers.Name, Producers.DateOfBirth, Movies.Title
        FROM Producers
        LEFT JOIN MovieProducer ON Producers.ProducerID = MovieProducer.ProducerID
        LEFT JOIN Movies ON MovieProducer.MovieID = Movies.MovieID
        WHERE Producers.Name LIKE %s OR Producers.DateOfBirth LIKE %s OR Movies.Title LIKE %s
        """
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%',))
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        return render_template('results_producers.html', results=results)
    
    return render_template('search_producers.html')


@app.route('/search_actor', methods=['GET', 'POST'])
def search_actor():
    if request.method == 'POST':
        keyword = request.form['keyword']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the search query
        query = """
        SELECT Actors.Name, Actors.DateOfBirth, Movies.Title
        FROM Actors
        LEFT JOIN MovieActor ON Actors.ActorID = MovieActor.ActorID
        LEFT JOIN Movies ON MovieActor.MovieID = Movies.MovieID
        WHERE Actors.Name LIKE %s OR Actors.DateOfBirth LIKE %s OR Movies.Title LIKE %s
        """
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%',))
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        return render_template('actors.html', results=results)
    
    return render_template('searchactor.html')



@app.route('/search_studio', methods=['GET', 'POST'])
def search_studio():
    if request.method == 'POST':
        keyword = request.form['keyword']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the search query
        query = """
        SELECT Studios.Name, Studios.Address, Movies.Title
        FROM Studios
        LEFT JOIN Movies ON Studios.StudioID = Movies.StudioID
        WHERE Studios.Name LIKE %s OR Studios.Address LIKE %s OR Movies.Title LIKE %s
        """
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%',))
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        return render_template('studios.html', results=results)
    
    return render_template('searchstudio.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the search query
        query = "SELECT * FROM movies WHERE title LIKE %s OR YearOfRelease LIKE %s OR Price LIKE %s"
        cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%', '%' + keyword + '%',))
        
        # Fetch the results
        results = cursor.fetchall()
        
        # Close the database connection
        cursor.close()
        conn.close()
        
        return render_template('results.html', results=results)
    
    return render_template('search.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        movie_id = request.form['id']
        new_title = request.form.get('title')
        new_year = request.form.get('year')
        new_genre = request.form.get('genre')
        new_price = request.form.get('price')

        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Prepare the SQL update statement dynamically
        query_update = "UPDATE movies SET"
        update_values = []
        if new_title:
            query_update += " Title = %s,"
            update_values.append(new_title)
        if new_year:
            query_update += " YearOfRelease = %s,"
            update_values.append(new_year)
        if new_genre:
            query_update += " Genre = %s,"
            update_values.append(new_genre)
        if new_price:
            query_update += " Price = %s,"
            update_values.append(new_price)
        
        # If no fields to update, return message
        if not update_values:
            return "No fields to update!"

        # Remove the last comma and append the WHERE clause
        query_update = query_update.rstrip(',') + " WHERE MovieId = %s"
        update_values.append(movie_id)

        # Execute the update query
        cursor.execute(query_update, tuple(update_values))

        # Commit the changes and close the database connection
        conn.commit()
        cursor.close()
        conn.close()

        return 'Movie updated successfully!'

    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        movie_id = request.form['id']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the delete query
        query = "DELETE FROM movies WHERE Movieid = %s"
        cursor.execute(query, (movie_id,))
        
        # Commit the changes and close the database connection
        conn.commit()
        cursor.close()
        conn.close()
        
        return 'Movie deleted successfully!'
    
    return render_template('delete.html')


@app.route('/movies')
def view_movies():
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Execute the query to retrieve all movies
    query = "SELECT * FROM movies"
    cursor.execute(query)
    
    # Fetch the results
    results = cursor.fetchall()
    
    # Close the database connection
    cursor.close()
    conn.close()
    
    return render_template('movies.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
