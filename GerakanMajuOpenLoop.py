# Import library controller dari Webots
from controller import Robot

# Inisialisasi robot
robot = Robot()

# Mendapatkan timestep dari simulator
timestep = int(robot.getBasicTimeStep())

# Mendapatkan perangkat motor dari robot
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')

# Mengatur mode motor ke posisi infinity agar motor terus berputar
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Memastikan motor sudah di-reset sebelum pengaturan kecepatan
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Mengatur kecepatan motor untuk gerakan melingkar
# Kecepatan roda kiri lebih lambat dari roda kanan
left_motor.setVelocity(3.14)  # Setengah dari kecepatan maksimal
right_motor.setVelocity(6.28)  # Kecepatan maksimal

# Loop simulasi
while robot.step(timestep) != -1:
    # Robot akan terus bergerak melingkar
    pass
