# Import library controller dari Webots
from controller import Robot

# Inisialisasi robot e-puck
robot = Robot()

# Mendapatkan timestep dari simulator (biasanya 64ms)
timestep = int(robot.getBasicTimeStep())

# Mendapatkan perangkat motor dari robot
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Mengatur mode motor ke posisi infinity agar motor terus berputar
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Mengaktifkan dan mendapatkan sensor proximity
proximity_sensors = []
sensor_names = ['ps0', 'ps1', 'ps2', 'ps3', 'ps4', 'ps5', 'ps6', 'ps7']
for sensor_name in sensor_names:
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    proximity_sensors.append(sensor)

# Mengatur kecepatan awal motor
left_motor.setVelocity(6.28)  # Kecepatan maksimal
right_motor.setVelocity(6.28) # Kecepatan maksimal

# Ambang batas deteksi objek (nilai ini bisa disesuaikan berdasarkan hasil simulasi)
detection_threshold = 80.0

# Loop simulasi
while robot.step(timestep) != -1:
    # Membaca nilai sensor proximity
    sensor_values = [sensor.getValue() for sensor in proximity_sensors]

    # Debug: print nilai sensor untuk mengetahui nilai yang terbaca
    print("Proximity sensor values:", sensor_values)
    
    # Mengecek apakah ada objek di depan (sensor PS0 atau PS7 terdeteksi)
    if sensor_values[0] > detection_threshold or sensor_values[7] > detection_threshold:
        # Menghentikan robot
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        print("Object detected! Stopping the robot.")
    else:
        # Terus bergerak maju jika tidak ada objek
        left_motor.setVelocity(6.28)
        right_motor.setVelocity(6.28)
