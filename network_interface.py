import subprocess
import time


def disable_enable_network_interface(interface_name):
    # Отключение сетевого интерфейса
    disable_cmd = f'netsh interface set interface "{interface_name}" admin=disable'
    subprocess.run(disable_cmd, shell=True, check=True)

    # Подождать 5 секунд
    time.sleep(5)

    # Включение сетевого интерфейса
    enable_cmd = f'netsh interface set interface "{interface_name}" admin=enable'
    subprocess.run(enable_cmd, shell=True, check=True)


# Пример использования
interface_name = "wifi"  # Укажите имя сетевого интерфейса, который нужно отключить и включить
disable_enable_network_interface(interface_name)
