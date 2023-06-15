import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
import sqlite3


class CarMaintenanceScheduler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vehicle Task Manager")
        self.setGeometry(200, 200, 600, 400)
        self.init_ui()
        self.connect_database()
        self.load_car_details()
        self.load_task_details()

    def init_ui(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.car_table = QTableWidget(self)
        self.car_table.setColumnCount(4)
        self.car_table.setHorizontalHeaderLabels(["Car ID", "Year", "Make", "Model"])
        self.car_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.car_id_label = QLabel("Car ID:")
        self.car_id_input = QLineEdit()

        self.car_year_label = QLabel("Year:")
        self.car_year_input = QLineEdit()

        self.car_make_label = QLabel("Make:")
        self.car_make_input = QLineEdit()

        self.car_model_label = QLabel("Model:")
        self.car_model_input = QLineEdit()

        self.add_car_button = QPushButton("Add Car")
        self.add_car_button.clicked.connect(self.save_car_details)

        self.remove_car_button = QPushButton("Remove Car")
        self.remove_car_button.clicked.connect(self.remove_car_details)

        self.task_table = QTableWidget(self)
        self.task_table.setColumnCount(2)
        self.task_table.setHorizontalHeaderLabels(["Task Name", "Car ID"])
        self.task_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.task_name_label = QLabel("Task Name:")
        self.task_name_input = QLineEdit()

        self.task_car_id_label = QLabel("Car ID:")
        self.task_car_id_input = QLineEdit()

        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.save_task_details)

        self.remove_task_button = QPushButton("Remove Task")
        self.remove_task_button.clicked.connect(self.remove_task_details)

        main_layout = QVBoxLayout()
        car_layout = QHBoxLayout()
        car_layout.addWidget(self.car_id_label)
        car_layout.addWidget(self.car_id_input)
        car_layout.addWidget(self.car_year_label)
        car_layout.addWidget(self.car_year_input)
        car_layout.addWidget(self.car_make_label)
        car_layout.addWidget(self.car_make_input)
        car_layout.addWidget(self.car_model_label)
        car_layout.addWidget(self.car_model_input)
        car_layout.addWidget(self.add_car_button)
        car_layout.addWidget(self.remove_car_button)
        main_layout.addLayout(car_layout)
        main_layout.addWidget(self.car_table)
        task_layout = QHBoxLayout()
        task_layout.addWidget(self.task_name_label)
        task_layout.addWidget(self.task_name_input)
        task_layout.addWidget(self.task_car_id_label)
        task_layout.addWidget(self.task_car_id_input)
        task_layout.addWidget(self.add_task_button)
        task_layout.addWidget(self.remove_task_button)
        main_layout.addLayout(task_layout)
        main_layout.addWidget(self.task_table)
        self.centralWidget.setLayout(main_layout)

    def connect_database(self):
        self.db = sqlite3.connect("vehicle_maintenance.db")
        self.cursor = self.db.cursor()

        with open("schema.sql", "r") as schema_file:
            schema_script = schema_file.read()
            self.cursor.executescript(schema_script)
            self.db.commit()

    def load_car_details(self):
        self.cursor.execute("SELECT car_id, car_year, car_make, car_model FROM CarDetails")
        car_details = self.cursor.fetchall()

        self.car_table.setRowCount(0)
        for row_num, row_data in enumerate(car_details):
            self.car_table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.car_table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def save_car_details(self):
        car_id = self.car_id_input.text()
        car_year = self.car_year_input.text()
        car_make = self.car_make_input.text()
        car_model = self.car_model_input.text()

        if car_year and car_make and car_model:
            self.cursor.execute(
                "INSERT INTO CarDetails (car_id, car_year, car_make, car_model) VALUES (?, ?, ?, ?)",
                (car_id, car_year, car_make, car_model),
            )
            self.db.commit()
            self.load_car_details()

            self.car_id_input.clear()
            self.car_year_input.clear()
            self.car_make_input.clear()
            self.car_model_input.clear()

    def remove_car_details(self):
        selected_rows = self.car_table.selectionModel().selectedRows()
        if selected_rows:
            for index in sorted(selected_rows, reverse=True):
                car_id = self.car_table.item(index.row(), 0).text()
                self.cursor.execute("DELETE FROM CarDetails WHERE car_id=?", (car_id,))
                self.cursor.execute("DELETE FROM MaintenanceTasks WHERE car_id=?", (car_id,))
                self.db.commit()
                self.car_table.removeRow(index.row())
                self.load_task_details()  # Update the task table

    def load_task_details(self):
        self.cursor.execute("SELECT task_name, car_id FROM MaintenanceTasks")
        task_details = self.cursor.fetchall()

        self.task_table.setRowCount(0)
        for row_num, row_data in enumerate(task_details):
            self.task_table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.task_table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    def save_task_details(self):
        task_name = self.task_name_input.text()
        car_id = self.task_car_id_input.text()

        if task_name and car_id:
            self.cursor.execute(
                "INSERT INTO MaintenanceTasks (task_name, car_id) VALUES (?, ?)", (task_name, car_id)
            )
            self.db.commit()
            self.load_task_details()

            self.task_name_input.clear()
            self.task_car_id_input.clear()

    def remove_task_details(self):
        selected_rows = self.task_table.selectionModel().selectedRows()
        if selected_rows:
            for index in sorted(selected_rows, reverse=True):
                task_name = self.task_table.item(index.row(), 0).text()
                car_id = self.task_table.item(index.row(), 1).text()
                self.cursor.execute("DELETE FROM MaintenanceTasks WHERE task_name=? AND car_id=?", (task_name, car_id))
                self.db.commit()
                self.task_table.removeRow(index.row())

    def closeEvent(self, event):
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CarMaintenanceScheduler()
    window.show()
    sys.exit(app.exec_())
