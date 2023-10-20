import Adafruit_DHT
import datetime
import time
import csv


sensor_pin = 4   

sensor_type = Adafruit_DHT.DHT11

csv_file = open("humidity_sensor_data.csv", "a")
csv_writer = csv.writer(csv_file)


try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, sensor_pin)
        if humidity is not None and temperature is not None:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Timestamp: {timestamp}")
            print(f"Temperature: {temperature:.2f}°C")
            print(f"Humidity: {humidity:.2f}%")
            
            
            csv_writer.writerow([timestamp, temperature, humidity])
            csv_file.flush()

        else:
            print("Failed to retrieve data from the sensor!")

        time.sleep(5)

except KeyboardInterrupt:
    print("Script terminated by user.")
