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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        keyword = request.form['keyword']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the search query
        query = "SELECT * FROM movies WHERE title LIKE %s"
        cursor.execute(query, ('%' + keyword + '%',))
        
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
        new_title = request.form['title']
        
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        # Execute the update query
        query = "UPDATE movies SET title = %s WHERE MovieId = %s"
        cursor.execute(query, (new_title, movie_id))
        
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

if __name__ == '__main__':
    app.run(debug=True)
