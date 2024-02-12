# Импорт необходимых библиотек
import time
import libcamera
from picamera2 import Picamera2, Preview


# Инициализация камеры
picam = Picamera2()

# Создание и настройка конфигурации камеры
config = picam.create_preview_configuration(main={"size": (1500, 900)})
config["transform"] = libcamera.Transform(hflip=0, vflip=0)
picam.configure(config)

# Запуск предварительного просмотра и камеры
picam.start_preview(Preview.QTGL)
picam.start()
time.sleep(2)

# Создание фотографии
picam.capture_file("test-python.png")

# Закрытие камеры
picam.close()

# Разделение фотографии на 9 равных частей
from PIL import Image

# Открытие изображения
input_image = Image.open('test-python.png')

# Размер каждого куска (в пикселях)
tile_width = 500
tile_height = 300

# Получение размеров исходного изображения
image_width, image_height = input_image.size
i = 0

# Цикл по изображению и разделение его на куски
for x in range(0, image_width, tile_width):
    for y in range(0, image_height, tile_height):
        left = x
        upper = y
        right = x + tile_width
        lower = y + tile_height

        # Вырезание куска из исходного изображения
        tile = input_image.crop((left, upper, right, lower))

        # Сохранение куска как отдельное изображение
        tile.save(f'fz{i}.png')
        i += 1

# Закрытие исходного изображения
input_image.close()



# Распознавание QR-кодов
from pyzbar.pyzbar import decode
from PIL import Image

details = []


# Цикл по файлам с изображениями
for i in range(0, 9):
    NameFile = "fz" + str(i) + ".png"
    image = Image.open(NameFile)
    print(NameFile)
    decoded_objects = decode(image)

    # Цикл по распознанным объектам
    for obj in decoded_objects:
        print(f"Тип: {obj.type}, данные: {obj.data.decode('utf-8')}")
        value = obj.data.decode('utf-8')
        if value == "":
            details.append("no")
        else:
            details.append(value)

print(details)

# Асинхронное получение данных из облачного хранилища
# Импорт необходимых библиотек
import asyncio
import boto3
import time


# Асинхронная функция для работы с облачным хранилищем
async def s3_demo():
    try:
        # Инициализация клиента для работы с облачным хранилищем
        s3_client = boto3.client(
            's3',
            aws_access_key_id='YCAJE6zihcw_TTy6H00_juYTt',
            aws_secret_access_key='YCP_iPjDq4IHO-1mHOODn8luCpB_rNEfZRpqQJhV',
            region_name='ru-central1',
            endpoint_url='https://storage.yandexcloud.net'
        )

        send = 'waiting'

        # Цикл для получения данных из облачного хранилища
        while True:
            response = s3_client.get_object(Bucket='mobileprogram2', Key='status2.txt')
            get = response['Body'].read().decode('utf-8')
            a = eval(get)
            print(a)
            time.sleep(1)


    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Асинхронная функция для запуска s3_demo()
async def main():
    await s3_demo()

# Запуск асинхронной функции main()
if __name__ == "__main__":
    asyncio.run(main())


# Передача данных на Arduino
# Импорт необходимых библиотек
import smbus2
import time

# Инициализация шины I2C
bus = smbus2.SMBus(1)

# Установка адреса устройства на шине I2C
address = 0x08

# Функция для отправки массива по шине I2C
def send_array(arr):
    for string in arr:  # Цикл по каждой строке в массиве
        for char in string:  # Цикл по каждому символу в строке
            bus.write_byte(address, ord(char))  # Отправка байта (ASCII код символа) по шине I2C
        bus.write_byte(address, 0)  # Отправка нулевого байта
    bus.write_byte(address, ord('|'))  # Отправка символа "|" по шине I2C

# Отправка массива "a" по шине I2C
send_array(a)
# Отправка массива "details" по шине I2C
send_array(details)
# Приостановка выполнения программы на 1 секунду
time.sleep(1)