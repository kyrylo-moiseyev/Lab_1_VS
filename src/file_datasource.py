from csv import reader
import csv
from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.aggregated_data import AggregatedData
import config


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
    ) -> None:
        pass

    def read(self, accelerometer_filename, gps_filename, parking_filename) -> AggregatedData:
        """Метод повертає дані отримані з датчиків"""
        x_values = []
        y_values = []
        z_values = []
        X_values = []
        Y_values = []
        p = []
        
        with open(accelerometer_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                x_values.append(float(row['x']))
                y_values.append(float(row['y']))
                z_values.append(float(row['z']))

        # Зчитування даних з файлу "gpc.csv"
        with open(gps_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                X_values.append(float(row['longitude']))
                Y_values.append(float(row['latitude']))

        with open(parking_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                p.append(float(row['x']))
                
        
        return x_values, y_values, z_values, X_values, Y_values, p

    def startReading(self, *args, **kwargs):
        """Метод повинен викликатись перед початком читання даних"""

    def stopReading(self, *args, **kwargs):
        """Метод повинен викликатись для закінчення читання даних"""
