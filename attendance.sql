-- Attendance table for database

DROP TABLE IF EXISTS attendance;

CREATE TABLE attendance (
    id INTEGER, -- foreign key referencing students table
    checkInTime DATETIME DEFAULT CURRENT_TIMESTAMP, -- timestamp of check-in
    PRIMARY KEY (id, checkInTime) -- allows for multiple timestamps for each student to account for different days
);
