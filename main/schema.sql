CREATE TABLE IF NOT EXISTS CarDetails (
    car_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_year INTEGER,
    car_make TEXT,
    car_model TEXT
);

CREATE TABLE IF NOT EXISTS MaintenanceTasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    car_id INTEGER,
    FOREIGN KEY (car_id) REFERENCES CarDetails (car_id)
);
