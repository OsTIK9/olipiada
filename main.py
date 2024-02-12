import time #импортирование библиотеки

import kivy #импортирование библиотеки

from kivy.core.window import Window #импортирование функции из библиотеки
from kivy.uix.image import Image #импортирование функции из библиотеки
from kivy.app import App #импортирование функции из библиотеки
from kivy.uix.button import Button#импортирование функции из библиотеки
from kivy.uix.floatlayout import FloatLayout #импортирование функции из библиотеки
from kivy.uix.boxlayout import BoxLayout #импортирование функции из библиотеки
from kivy.uix.screenmanager import ScreenManager, Screen #импортирование функции из библиотеки
from kivy.uix.togglebutton import ToggleButton #импортирование функции из библиотеки
from kivy.uix.label import Label #импортирование функции из библиотеки
from kivy.clock import Clock #импортирование функции из библиотеки

import asyncio #импортирование библиотеки
import boto3 #импортирование библиотеки

from threading import Thread #импортирование функции из библиотеки
from time import sleep #импортирование функции из библиотеки

k1 = (Window.size[0]/540) #создание коэффициента для изменения разменра интерфейса в зависимости от устройства


details = ['vinty', 'gayki', 'shaibu', 'shpilki', 'valu', 'dvigateli', 'podshipniki', 'lineynue_napravlyaushie', 'datchiki'] #объявление списка

lbl_STATUS_text = '' #создание переменной для изменения статуса

lbl_STATUS_button = '' #создание переменной для изменения кнопки "отменить заказ" на "готово"

info = '' #создание переменной для изменения статуса

lst_len = None #создание переменной для определения длины списка выбранных товаров

def CheckData(): #функция таймера
     global info #объявление переменной глобальной

     info = 'waiting' #изменение значений переменной для вывода "ожидание"

     ctue(info) #вызов функции для изменения статуса

     sleep(4) #таймер

     info = 'assembling' #изменение значений переменной для вывода "сборка заказа"

     ctue(info) #вызов функции для изменения статуса

     sleep(17 * lst_len) #таймер

     info = 'done' #изменение значений переменной для вывода "сборка завершена"

     ctue(info) #вызов функции для изменения статуса


def CheckData2(): #функция таймера
    global info #объявление переменной для статуса глобальной

    info = 'waiting' #изменение значений переменной для вывода "ожидание"

    ctue(info) #вызов функции для изменения статуса

    sleep(4) #таймер

    info = 'assembling' #изменение значений переменной для вывода "сборка заказа"

    ctue(info) #вызов функции для изменения статуса

    sleep(9999) #таймер



def ctue(obj): #функция для изменения статуса
    info = obj #объявление локальной переменной для изменения статуса

    global lbl_STATUS_text #объявление переменной глобальной

    global lbl_STATUS_button #объявление переменной глобальной

    if info == 'waiting':
        lbl_STATUS_text = 'Ожидание...' #присваивание переменной для изменения статуса нового значения

    if info == 'assembling':
        lbl_STATUS_text = 'Сборка заказа' #присваивание переменной для изменения статуса нового значения

    if info == 'done':
        lbl_STATUS_text = 'Сборка завершена' #присваивание переменной для изменения статуса нового значения
        lbl_STATUS_button = 'done' #присваивание переменной для изменения статуса нового значения



def status(): #функция для обнуления статуса
    global lbl_STATUS_text #объявление переменной глобальной
    lbl_STATUS_text = '' #присваивание переменной для изменения статуса пустого значения


class MyApp(App): #класс запуска программы
    def build(self):
        sm.add_widget(MainScreen()) #добавление в ScreenManager первого экрана
        sm.add_widget(ThirdScreen()) #добавление в ScreenManager второго экрана
        sm.add_widget(SecondScreen()) #добавление в ScreenManager третьего экрана
        return sm #возврат значения sm (объявлено в конце программы)



class MainScreen(Screen): #класс первого экрана
    def __init__(self): #метод, который запускается с вызовом класса
        super().__init__()

        self.name = 'Main' #присваивание экрану уникального имени для переключения между экранами


        layout3 = FloatLayout() #объявление лайаута
        layout = FloatLayout() #объявление лайаута
        layout2 = FloatLayout() #объявление лайаута
        img = Image(source='Resources/стартовый экран.png') #объявление фона экрана
        btn = Button(border=(0, 0, 0, 0), #объявление кнопки "сделать заказ"
                     background_normal='Resources/Кнопка для сбора заказов.png',
                     background_down='Resources/Нажатая кнопка для сбора заказов.png',
                     size_hint=(None, None),
                     size=(318.75*k1, 120*k1),
                     pos=(111*k1, 115*k1))
        btn.bind(on_release=self.to_second_scrn) #вызов функции для перехода на второй экран по нажатию на кнопку btn

        layout2.add_widget(btn) #добавление в лайаут btn
        layout.add_widget(img) #добавление в лайаут img

        layout3.add_widget(layout) #объединение лайаутов
        layout3.add_widget(layout2) #объединение лайаутов

        self.add_widget(layout3) #вывод на экран

    def to_second_scrn(self, *args): #функция для перехода на второй экран
        self.manager.transition.direction = 'left' #анимация перехода
        self.manager.current = 'Second' #переход на второй экран (в __init__ второго экрана self.name = 'second')




class SecondScreen(Screen): #класс второго экрана

    k = 0 #счётчик

    def __init__(self): #метод, который запускается с вызовом класса
        super().__init__()
        self.name = 'Second' #присваивание экрану уникального имени для переключения между экранами
        layout5 = FloatLayout() #объявление лайаута
        layout3 = FloatLayout() #объявление лайаута
        layout = BoxLayout(size=(540 * k1, 960 * k1)) #объявление лайаута
        layout2 = FloatLayout() #объявление лайаута
        layout4 = FloatLayout() #объявление лайаута
        img = Image(source='Resources/экран сборки.png') #объявление фона экрана
        btn = Button(border=(0, 0, 0, 0), #объявление кнопки "отмена"
                      background_normal='Resources/Отмена.png',
                      background_down='Resources/Отмена инверт.png',
                      size_hint=(None, None),
                      size=(318.75 * k1, 120 * k1),
                      pos=(110.5 * k1, 36 * k1))
        btn2 = Button(border=(0, 0, 0, 0), #объявление кнопки "начать сборку"
                      background_normal='Resources/Начать сборку.png',
                     background_down='Resources/Начать сборку инверт.png',
                      size_hint=(None, None),
                      size=(318.75*k1, 120*k1),
                      pos=(111 * k1, 165.5 * k1),
                      on_release=self.check_state) #вызов функции для проверки каждой кнопки флага по нажатию на кнопку btn2

        layout2.add_widget(btn) #добавление в лайаут btn
        layout.add_widget(img) #добавление в лайаут img
        layout4.add_widget(btn2) #добавление в лайаут btn2

        layout3.add_widget(layout) #объединение лайаутов
        layout3.add_widget(layout2) #объединение лайаутов
        layout3.add_widget(layout4) #объединение лайаутов

        self.btn_chc1 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "винты"
                                     pos_hint={'center_x': 0.1895, 'center_y': 0.887},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Винты.png',
                                     background_down='Resources/Винты инверт.png')

        self.btn_chc2 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "гайки"
                                     pos_hint={'center_x': 0.5, 'center_y': 0.887},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Гайки.png',
                                     background_down='Resources/Гайки инверт.png')

        self.btn_chc3 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "шайбы"
                                    pos_hint={'center_x': 0.809, 'center_y': 0.887},
                                    size_hint=(None, None),
                                    size=(150.75 * k1, 150.75 * k1),
                                    background_normal='Resources/Шайбы.png',
                                    background_down='Resources/Шайбы инверт.png')

        self.btn_chc4 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "шпильки"
                                     pos_hint={'center_x': 0.191, 'center_y': 0.6878},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Шпильки.png',
                                     background_down='Resources/Шпильки инверт.png')

        self.btn_chc5 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "валы"
                                     pos_hint={'center_x': 0.502, 'center_y': 0.6875},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Валы.png',
                                     background_down='Resources/Валы инверт.png')

        self.btn_chc6 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "двигатели"
                                     pos_hint={'center_x': 0.81, 'center_y': 0.6875},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Двигатели.png',
                                     background_down='Resources/Двигатели инверт.png')

        self.btn_chc7 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "подшибники"
                                     pos_hint={'center_x': 0.189, 'center_y': 0.488},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Подшибники.png',
                                     background_down='Resources/Подшибники инверт.png')

        self.btn_chc8 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "направляющие линейные"
                                     pos_hint={'center_x': 0.5, 'center_y': 0.4875},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Линейные направляющие.png',
                                     background_down='Resources/Линейные направляющие инверт.png')

        self.btn_chc9 = ToggleButton(border=(0, 0, 0, 0), #объявление кнопки с флагом "датчики"
                                     pos_hint={'center_x': 0.81, 'center_y': 0.4875},
                                     size_hint=(None, None),
                                     size=(150.75 * k1, 150.75 * k1),
                                     background_normal='Resources/Датчики.png',
                                     background_down='Resources/Датчики инверт.png')

        layout5.add_widget(self.btn_chc1) #добавление добавление в лайаут кнопки btn_chc1
        layout5.add_widget(self.btn_chc2) #добавление добавление в лайаут кнопки btn_chc2
        layout5.add_widget(self.btn_chc3) #добавление добавление в лайаут кнопки btn_chc3
        layout5.add_widget(self.btn_chc4) #добавление добавление в лайаут кнопки btn_chc4
        layout5.add_widget(self.btn_chc5) #добавление добавление в лайаут кнопки btn_chc5
        layout5.add_widget(self.btn_chc6) #добавление добавление в лайаут кнопки btn_chc6
        layout5.add_widget(self.btn_chc7) #добавление добавление в лайаут кнопки btn_chc7
        layout5.add_widget(self.btn_chc8) #добавление добавление в лайаут кнопки btn_chc8
        layout5.add_widget(self.btn_chc9) #добавление добавление в лайаут кнопки btn_chc9

        self.add_widget(layout3) #вывод на экран
        self.add_widget(layout5) #вывод на экран


        btn.bind(on_release=self.to_main_scrn) #вызов функции для перехода на первый экран по нажатию на кнопку btn
        btn2.bind(on_release=self.to_third_scrn) #вызов функции для перехода на третий экран по нажатию на кнопку btn


    def to_main_scrn(self, *args): #функция для перехода на второй экран
        self.manager.transition.direction = 'right' #анимация перехода
        self.manager.current = 'Main' #переход на первый экран (в __init__ второго экрана self.name = 'main')

    def to_third_scrn(self, *args): #функция для перехода на второй экран
        self.manager.transition.direction = 'left' #анимация перехода
        self.manager.current = 'Third' #переход на третий экран (в __init__ второго экрана self.name = 'third')


    def check_state(self, obj): #фукцичя для проверки каждой кнопки флага

        self.k += 1 #работа счётчика

        global lst_len #объявление переменной глобальной

        lst = [] #объявление списка выбранных продуктов

        self.b1 = self.btn_chc1.state #проверка кнопки флага на значение "down" или "normal"
        self.b2 = self.btn_chc2.state #проверка кнопки флага на значение "down" или "normal"
        self.b3 = self.btn_chc3.state #проверка кнопки флага на значение "down" или "normal"
        self.b4 = self.btn_chc4.state #проверка кнопки флага на значение "down" или "normal"
        self.b5 = self.btn_chc5.state #проверка кнопки флага на значение "down" или "normal"
        self.b6 = self.btn_chc6.state #проверка кнопки флага на значение "down" или "normal"
        self.b7 = self.btn_chc7.state #проверка кнопки флага на значение "down" или "normal"
        self.b8 = self.btn_chc8.state #проверка кнопки флага на значение "down" или "normal"
        self.b9 = self.btn_chc9.state #проверка кнопки флага на значение "down" или "normal"

        if self.b1 == 'down':
            lst.append('vinty') #добавление винтов в список выбранных продуктов

        if self.b2 == 'down':
            lst.append('gayki') #добавление гаек в список выбранных продуктов

        if self.b3 == 'down':
            lst.append('shaibu') #добавление шаеб в список выбранных продуктов

        if self.b4 == 'down':
            lst.append('shpilki') #добавление шпилек в список выбранных продуктов

        if self.b5 == 'down':
            lst.append('valu') #добавление валов в список выбранных продуктов

        if self.b6 == 'down':
            lst.append('dvigateli') #добавление двигателей в список выбранных продуктов

        if self.b7 == 'down':
            lst.append('podshipniki') #добавление подшибников в список выбранных продуктов

        if self.b8 == 'down':
            lst.append('lineynue_napravlyaushie') #добавление линейных направляющих в список выбранных продуктов

        if self.b9 == 'down':
            lst.append('datchiki') #добавление датчиков в список выбранных продуктов

        async def s3_demo(): #функция для отправки данных

            s3_client = boto3.client( #объявление клиента
                's3',
                aws_access_key_id='YCAJE6zihcw_TTy6H00_juYTt',
                aws_secret_access_key='YCP_iPjDq4IHO-1mHOODn8luCpB_rNEfZRpqQJhV',
                region_name='ru-central1',
                endpoint_url='https://storage.yandexcloud.net'
            )

            send = "["
            for i in range(len(lst)):
                send = send + "'" + lst[i] + "'" + ', '
            send = send[0:-2] + "]" #образование списка в str для отправки



            s3_client.put_object(Body=send, Bucket='mobileprogram2', Key='status2.txt') #создание файла "status2.txt", погрузка в него данных из переменной send, загрузка данных в облако


        async def main(): #запуск отправки
            await s3_demo() #вызов функции для отправки данных

        asyncio.run(main()) #запуск отправки

        lst_len = len(lst) #присваивание переменной числа, обозначающего длину списка с выбранными товарами


        if self.k != 3:
            Thread(target=CheckData).start() #запуск потока с таймером
        if self.k == 3:
            Thread(target=CheckData2).start() #запуск потока с таймером



class ThirdScreen(Screen): #класс третьего экрана
    def __init__(self): #метод, который запускается с вызовом класса
        super().__init__()

        self.name = 'Third' #присваивание экрану уникального имени для переключения между экранами

        Thread(target=self.updater).start() #запуск потока с обновлением статуса


        layout3 = FloatLayout() #объявление лайаута
        layout = BoxLayout(size=(540 * k1, 960 * k1)) #объявление лайаута
        layout2 = FloatLayout() #объявление лайаута
        layout4 = FloatLayout() #объявление лайаута


        img = Image(source='Resources/Экран статуса.png') #объявление фона экрана
        self.btn = Button(border=(0, 0, 0, 0), #объявление кнопки "отменить сборку и кнопки "готово" (кнопка зависит от значений lbl_STATUS_btn)
                     background_normal='Resources/Отменить сборку.png',
                     background_down='Resources/Отменить сборку инверт.png',
                     size_hint=(None, None),
                     size=(318.75 * k1, 120 * k1),
                     pos=(110.5 * k1, 86 * k1),
                     on_release=self.to_second_scrn2) #вызов функции для перехода на второй экран по нажатию на кнопку btn

        self.lbl = Label(text='', #объявление текста статуса
                    size_hint = (None, None),
                    font_size = 50*k1,
                    pos = (220*k1, 650*k1),
                    color = 'black')

        layout4.add_widget(self.lbl) #добавление в лайаут lbl


        layout2.add_widget(self.btn) #добавление в лайаут btn


        layout.add_widget(img) #добавление в лайаут img


        layout3.add_widget(layout) #объединение лайаутов
        layout3.add_widget(layout2) #объединение лайаутов
        layout3.add_widget(layout4) #объединение лайаутов


        self.add_widget(layout3) #вывод на экран
        self.btn.bind(on_release=self.cancel) #вызов функции отмены сборки

    def updater(self): #функция для обновления статуса сборки
        Clock.schedule_interval(self.done, 1) #запуск цикла while, реализованного при помощи библиотеки kivy

    def done(self, arg):
        self.lbl.text = lbl_STATUS_text #изменение текста статуса сборки на актуальный статус (изменение происходит раз в секунду при помощи функции updater)

        if lbl_STATUS_button == 'done':
            self.btn.background_normal = 'Resources/готово.png' #изменение кнопки "отменить сборку" на кнопку "готово"
            self.btn.background_down = 'Resources/готово инверт.png' #изменение кнопки "отменить сборку" на кнопку "готово"
        if lbl_STATUS_button != 'done':
            self.btn.background_normal = 'Resources/Отменить сборку.png' #изменение кнопки "готово" на кнопку "отменить сборку"
            self.btn.background_down = 'Resources/Отменить сборку инверт.png' #изменение кнопки "готово" на кнопку "отменить сборку"



    def to_second_scrn2(self, *args): #функция для переключения на второй экран
        self.manager.transition.direction = 'right' #анимация перехода
        self.manager.current = 'Second' #переход на второй экран (в __init__ второго экрана self.name = 'second')

    def cancel(self, obj): #функция для отмены сборки

        global  lbl_STATUS_button #объявление переменной глобальной

        async def s3_demo(): #функция для отправки данных
            s3_client = boto3.client( #объявление клиента
                's3',
                aws_access_key_id='YCAJE6zihcw_TTy6H00_juYTt',
                aws_secret_access_key='YCP_iPjDq4IHO-1mHOODn8luCpB_rNEfZRpqQJhV',
                region_name='ru-central1',
                endpoint_url='https://storage.yandexcloud.net'
            )

            send = "['stop']" #отправка слова "stop" в списке в str формате

            s3_client.put_object(Body=send, Bucket='mobileprogram2', Key='status2.txt') #создание файла "status2.txt", погрузка в него данных из переменной send, загрузка данных в облако

        async def main(): #запуск отправки
            await s3_demo() #вызов функции для отправки данных

        asyncio.run(main()) #запуск отправки

        lbl_STATUS_button = '' #присваивание переменной пустого значения для изменения кнопки "готово" на "отменить сборку"




sm = ScreenManager() #присваивание, необходимое для работы ScreenManager


try: #исключение вывода ошибок при остановке приложения
    if __name__ == '__main__':
            MyApp().run() #запуск приложения
except: #исключение вывода ошибок при остановке приложения
    pass #исключение вывода ошибок при остановке приложения
