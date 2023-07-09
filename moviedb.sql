-- Create table queries
CREATE TABLE Directors (
    DirectorID INTEGER PRIMARY KEY,
    Name TEXT,
    DateOfBirth DATE
);

CREATE TABLE Studios (
    StudioID INTEGER PRIMARY KEY,
    Name TEXT,
    Address TEXT
);

CREATE TABLE Producers (
    ProducerID INTEGER PRIMARY KEY,
    Name TEXT,
    DateOfBirth DATE
);

CREATE TABLE Actors (
    ActorID INTEGER PRIMARY KEY,
    Name TEXT,
    DateOfBirth DATE
);

CREATE TABLE Movies (
    MovieID INTEGER AUTO_INCREMENT PRIMARY KEY,
    Title TEXT,
    YearOfRelease INTEGER,
    Genre TEXT,
    RunningTime INTEGER,
    DirectorID INTEGER,
    StudioID INTEGER,
    Price DECIMAL(5,2),
    FOREIGN KEY (DirectorID) REFERENCES Directors(DirectorID),
    FOREIGN KEY (StudioID) REFERENCES Studios(StudioID)
);

CREATE TABLE MovieActor (
    MovieID INTEGER,
    ActorID INTEGER,
    Role TEXT,
    IsLead BOOLEAN,
    PRIMARY KEY (MovieID, ActorID),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
);

CREATE TABLE MovieProducer (
    MovieID INTEGER,
    ProducerID INTEGER,
    PRIMARY KEY (MovieID, ProducerID),
    FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
    FOREIGN KEY (ProducerID) REFERENCES Producers(ProducerID)
);

-- Insert data queries
INSERT INTO Directors (DirectorID, Name, DateOfBirth) VALUES (1, 'Steven Spielberg', '1946-12-18');
INSERT INTO Studios (StudioID, Name, Address) VALUES (1, 'Warner Bros', '3400 W Riverside Dr, Burbank, CA 91505, United States');
INSERT INTO Producers (ProducerID, Name, DateOfBirth) VALUES (1, 'George Lucas', '1944-05-14');
INSERT INTO Actors (ActorID, Name, DateOfBirth) VALUES (1, 'Tom Hanks', '1956-07-09');
INSERT INTO Movies (MovieID, Title, YearOfRelease, Genre, RunningTime, DirectorID, StudioID, Price) VALUES (1, 'Saving Private Ryan', 1998, 'Drama', 169, 1, 1, 19.99);
INSERT INTO MovieActor (MovieID, ActorID, Role, IsLead) VALUES (1, 1, 'Captain John H. Miller', TRUE);
INSERT INTO MovieProducer (MovieID, ProducerID) VALUES (1, 1);
INSERT INTO Directors (DirectorID, Name, DateOfBirth) VALUES (2, 'Christopher Nolan', '1970-07-30');
INSERT INTO Directors (DirectorID, Name, DateOfBirth) VALUES (3, 'James Cameron', '1954-08-16');
INSERT INTO Studios (StudioID, Name, Address) VALUES (2, 'Paramount Pictures', '5555 Melrose Ave, Los Angeles, CA 90038, United States');
INSERT INTO Studios (StudioID, Name, Address) VALUES (3, '20th Century Studios', '10201 W Pico Blvd, Los Angeles, CA 90064, United States');
INSERT INTO Producers (ProducerID, Name, DateOfBirth) VALUES (2, 'JJ Abrams', '1966-06-27');
INSERT INTO Producers (ProducerID, Name, DateOfBirth) VALUES (3, 'Kathleen Kennedy', '1953-06-05');
INSERT INTO Actors (ActorID, Name, DateOfBirth) VALUES (2, 'Leonardo DiCaprio', '1974-11-11');
INSERT INTO Actors (ActorID, Name, DateOfBirth) VALUES (3, 'Scarlett Johansson', '1984-11-22');
INSERT INTO Movies (MovieID, Title, YearOfRelease, Genre, RunningTime, DirectorID, StudioID, Price) VALUES (2, 'Interstellar', 2014, 'Sci-Fi', 169, 2, 2, 19.99);
INSERT INTO MovieActor (MovieID, ActorID, Role, IsLead) VALUES (2, 2, 'Joseph Cooper', TRUE);
INSERT INTO Directors (DirectorID, Name, DateOfBirth) VALUES
(4, 'Peter Jackson', '1961-10-31'),
(5, 'Quentin Tarantino', '1963-03-27'),
(6, 'Martin Scorsese', '1942-11-17'),
(7, 'Alfred Hitchcock', '1899-08-13'),
(8, 'Stanley Kubrick', '1928-07-26'),
(9, 'David Fincher', '1962-08-28'),
(10, 'Francis Ford Coppola', '1939-04-07');
INSERT INTO Studios (StudioID, Name, Address) VALUES
(4, 'Universal Pictures', '100 Universal City Plaza, Universal City, CA 91608, United States'),
(5, 'Columbia Pictures', '10202 W Washington Blvd, Culver City, CA 90232, United States'),
(6, 'MGM Studios', '245 N Beverly Dr, Beverly Hills, CA 90210, United States'),
(7, 'Lionsgate Films', '2700 Colorado Ave, Santa Monica, CA 90404, United States'),
(8, 'Disney Studios', '500 S Buena Vista St, Burbank, CA 91521, United States'),
(9, 'DreamWorks Animation', '1000 Flower St, Glendale, CA 91201, United States'),
(10, 'Pixar Animation Studios', '1200 Park Ave, Emeryville, CA 94608, United States');
INSERT INTO Producers (ProducerID, Name, DateOfBirth) VALUES
(4, 'Steven Spielberg', '1946-12-18'),
(5, 'James Cameron', '1954-08-16'),
(6, 'Christopher Nolan', '1970-07-30'),
(7, 'J.J. Abrams', '1966-06-27'),
(8, 'Ridley Scott', '1937-11-30'),
(9, 'Tim Burton', '1958-08-25'),
(10, 'George Lucas', '1944-05-14');
INSERT INTO Actors (ActorID, Name, DateOfBirth) VALUES
(4, 'Robert De Niro', '1943-08-17'),
(5, 'Morgan Freeman', '1937-06-01'),
(6, 'Brad Pitt', '1963-12-18'),
(7, 'Meryl Streep', '1949-06-22'),
(8, 'Jennifer Lawrence', '1990-08-15'),
(9, 'Johnny Depp', '1963-06-09'),
(10, 'Natalie Portman', '1981-06-09');
INSERT INTO Movies (MovieID, Title, YearOfRelease, Genre, RunningTime, DirectorID, StudioID, Price) VALUES
(3, 'The Shawshank Redemption', 1994, 'Drama', 142, 6, 4, 19.99),
(4, 'The Godfather', 1972, 'Crime', 175, 10, 6, 19.99),
(5, 'Pulp Fiction', 1994, 'Crime', 154, 5, 7, 19.99),
(6, 'Fight Club', 1999, 'Drama', 139, 9, 5, 19.99),
(7, 'Forrest Gump', 1994, 'Drama', 142, 1, 4, 19.99),
(8, 'Inception', 2010, 'Sci-Fi', 148, 2, 2, 19.99),
(9, 'The Dark Knight', 2008, 'Action', 152, 2, 1, 19.99),
(10, 'The Lord of the Rings: The Return of the King', 2003, 'Adventure', 201, 4, 5, 19.99);
INSERT INTO MovieActor (MovieID, ActorID, Role, IsLead) VALUES
(3, 5, 'Ellis Boyd \'Red\' Redding', TRUE),
(4, 4, 'Vito Corleone', TRUE),
(5, 6, 'Jules Winnfield', TRUE),
(6, 6, 'Tyler Durden', TRUE),
(7, 1, 'Forrest Gump', TRUE),
(8, 2, 'Dom Cobb', TRUE),
(9, 2, 'Bruce Wayne', TRUE),
(10, 1, 'Samwise Gamgee', FALSE);
INSERT INTO MovieProducer (MovieID, ProducerID) VALUES
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 2),
(10, 3),
(2, 4),
(1, 5);
