-- Student table for database

DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- student id
    firstName NVARCHAR(40) NULL, -- first name
    lastName NVARCHAR(40) NULL -- last name
);