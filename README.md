# Movie Database Management: A Flask Web Application

## Introduction
The world of cinema is vast and ever-expanding. With hundreds of thousands of movies produced over the years, managing this enormous collection of information is a challenging task. This project focuses on the development of a web application using Flask, a popular micro web framework in Python, to efficiently manage a movie database. By offering functionalities such as viewing, creating, deleting, and updating movie records, our application serves as a comprehensive tool for movie data management.

## Project Description
Our Flask web application aims to manage a complex movie database comprising various entities such as movies, directors, producers, actors, and movie studios. It hosts a variety of functionalities, meeting the following functional requirements:

1. Movie Information: Each movie record consists of title, year of release, genre, running time, director, producers, actors and actresses, movie studios, and price.

2. Viewing Records: Users can view the entire database, accessing comprehensive information about all the movies.

3. Creating Movies: The application allows users to add new movies to the database.

4. Deleting Movies: Users can delete existing movies from the database.

5. Updating Information: The application provides the capability to search for a specific movie and update its information.

6. Search Functionality: Users can search for movies using various parameters such as title, year of release, genre, director, producers, movie studios, actors and actresses.

7. Extended Search: The application allows users to search for actors, producers, and directors by their names, dates of birth or movies.

8. Studio Search: Users can search movie studios by their names, addresses, or movies.

The back-end database handling these operations is built on MariaDB, providing robustness and efficiency.

## Getting Started

Clone the repository to your local machine:

```bash
    git clone <repo-url>

Install the necessary dependencies:
  pip install -r requirements.txt
Run the Flask application:
  flask run

