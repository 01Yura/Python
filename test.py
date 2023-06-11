import subprocess
import time

# Определение имени сетевого интерфейса
interface_name = "wifi"  # Замените на имя своего сетевого интерфейса

# Отключение сетевого интерфейса
subprocess.run(["netsh", "interface", "set", "interface", interface_name, "admin=disable"], capture_output=True)

# Подождать 5 секунд
time.sleep(5)

# Включение сетевого интерфейса
subprocess.run(["netsh", "interface", "set", "interface", interface_name, "admin=enable"], capture_output=True)

print("Сетевой интерфейс был выключен и снова включен.")
