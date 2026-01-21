CREATE TABLE labours_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    role VARCHAR(255) NOT NULL,
    wages INT NOT NULL
);


-- Insert labours
INSERT INTO labours_table (name, role, wages) VALUES
('Mahesh', 'labour', 500),
('Ramesh', 'labour', 400),
('Mithilesh', 'labour', 400),
('Sumesh', 'labour', 300);

-- Insert mistris
INSERT INTO labours_table (name, role, wages) VALUES
('Jagmohan', 'mistri', 1000),
('Rampyare', 'mistri', 800);



CREATE TABLE attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    labours_id INT,
    start_time TIME,
    end_time TIME,
    date DATE,
    FOREIGN KEY (labours_id) REFERENCES labours_table(id)
);


INSERT INTO attendance (labours_id, start_time, end_time, date) VALUES
(1, '08:00:00', '17:00:00', '2024-05-14'),
(2, '08:30:00', '17:30:00', '2024-05-14'),
(3, '09:00:00', '18:00:00', '2024-05-14'),
(4, '09:00:00', '18:00:00', '2024-05-14'),
(5, '07:00:00', '16:00:00', '2024-05-14'),
(6, '07:30:00', '16:30:00', '2024-05-14');


insert_query = "INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)"
cursor.execute(insert_query, ('New Labour', 'labour', 600))
Finally close all the connection
connection.commit()
cursor.close()
connection.close()
