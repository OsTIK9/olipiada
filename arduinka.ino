#include <Servo.h> // Подключение библиотеки для работы с сервоприводами
#include <Wire.h> // Подключение библиотеки для работы с шиной I2C

Servo UP; // Объявление сервопривода UP
Servo FORWARD; // Объявление сервопривода FORWARD
Servo SIDE; // Объявление сервопривода SIDE
Servo GRAB; // Объявление сервопривода GRIP


#define I2C_SLAVE_ADDRESS 0x08 // Определение I2C-адреса подчиненного Arduino
#define MAX_ARRAY_SIZE 10 // Определение максимального размера массивов
#define MAX_STRING_LENGTH 32 // Определение максимальной длины каждой строки

String details[MAX_ARRAY_SIZE]; // Массив для хранения расположения товаров с стеллаже
String a[MAX_ARRAY_SIZE]; // Массив для хранения товаров из заказа


bool arraysReceived = false; // Флаг для указания того, получены ли массивы

// Функция для обработки события получения данных по шине I2C
void receiveEvent(int howMany) {
  static int arrayIndex = 0;
  static int stringIndex = 0;
  static String currentString = "";

  while (Wire.available()) {
    char c = Wire.read();
    if (c == '\0') {
// Символ '0' указывает на конец строки
      if (stringIndex < MAX_ARRAY_SIZE) {
        if (arrayIndex == 0) {
          a[stringIndex] = currentString;
        } else if (arrayIndex == 1) {
          details[stringIndex] = currentString;
        }
        currentString = ""; // Сброс текущей строки
        stringIndex++;
      }
    } else if (c == '|') {
      // Символ вертикальной черты указывает на конец массива
      arrayIndex++;
      stringIndex = 0;
    } else if (c == '!') {
      // Восклицательный знак указывает на конец всех массивов
      arraysReceived = true;
      break;
    } else {
      // Добавление символа к текущей строке
      if (currentString.length() < MAX_STRING_LENGTH) {
        currentString += c;
      }
    }
  }
}


int *b = nullptr; // Указатель на динамически выделенный массив
int bSize = 0; // Фактический размер массива b

void setup() 
{

Wire.begin(I2C_SLAVE_ADDRESS); // Присоединение к шине I2C в качестве подчиненного
Wire.onReceive(receiveEvent); // Регистрация события получения

  UP.attach(13); // Присоединение сервопривода к пину 13
  FORWARD.attach(12); // Присоединение сервопривода к пину 12
  SIDE.attach(11); // Присоединение сервопривода к пину 11
  GRAB.attach(10); // Присоединение сервопривода к пину 10

  UP.write(0); // Установка начального положения сервопривода UP
  FORWARD.write(0); // Установка начального положения сервопривода FORWARD
  SIDE.write(0); // Установка начального положения сервопривода SIDE
  GRAB.write(46); // Установка начального положения сервопривода GRAB
  delay(5000); // Пауза 5 секунд

  Serial.begin(9600); // Подключение монитора порта

  // Определение размера массива b
  for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++) {
    for (int j = 0; j < sizeof(details) / sizeof(details[0]); j++) {
      if (a[i] == details[j]) {
        bSize++;
        break;
      }
    }
  }

  // Выделение памяти для массива b
  b = new int[bSize];

  // Инициализация b значениями -1 для обозначения отсутствия элементов
  for (int i = 0; i < bSize; i++) {
    b[i] = -1;
  }

  int bIndex = 0;
  for (int i = 0; i < sizeof(a) / sizeof(a[0]); i++) {
    for (int j = 0; j < sizeof(details) / sizeof(details[0]); j++) {
      if (a[i] == details[j]) {
        b[bIndex] = j; // Сохранение индекса дубликата из массива details
        bIndex++;
        break;
      }
    }
  }
}


void loop() {
  if (arraysReceived) {
  // Вывод массивов в Serial Monitor
    Serial.print("a: ");
    for (int i = 1; i < MAX_ARRAY_SIZE; i++) {
      if (a[i] != "") {
        Serial.print(a[i]);
        if (i < MAX_ARRAY_SIZE - 1) {
          Serial.print(", ");
        }
      }
    }
    Serial.println();

    Serial.print("details: ");
    for (int i = 1; i < MAX_ARRAY_SIZE; i++) {
      if (details[i] != "") {
        Serial.print(details[i]);
        if (i < MAX_ARRAY_SIZE - 1) {
          Serial.print(", ");
        }
      }
    }
    Serial.println();

    arraysReceived = false; // Сброс флага
  }
 bool flag = false; // Флаг для указания того, обработаны ли указанное количество случаев
  int count = 0; // Счетчик для отслеживания количества обработанных случаев

  for (int i = 0; i < bSize; i++) {
    if (b[i] != -1) { // Если элемент массива b не равен -1, то выполняем действия внутри switch-case
      switch (b[i]) {
        case 0: // Действия для случая, когда b[i] равен 0
          Serial.println("Found 0");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(112.2);
          delay(2000);
          UP.write(58);
          delay(2000);
          FORWARD.write(84);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          delay(2000);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(50);
          delay(2000);
          break;
        case 1:  // Действия для случая, когда b[i] равен 1
          Serial.println("Found 1");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(109);
          delay(2000);
          UP.write(37);
          delay(2000);
          FORWARD.write(96);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(46);
          delay(2000);
          break;
        case 2:  // Действия для случая, когда b[i] равен 2
          Serial.println("Found 2");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(105);
          delay(2000);
          UP.write(14);
          delay(2000);
          FORWARD.write(140);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(40);
          delay(2000);
          break;
        case 3:  // Действия для случая, когда b[i] равен 3
          Serial.println("Found 3");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(138.6);
          delay(2000);
          UP.write(59.5);
          delay(2000);
          FORWARD.write(79);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          delay(2000);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(40);
          delay(2000);
          break;
        case 4:  // Действия для случая, когда b[i] равен 4
          Serial.println("Found 4");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(138.9);
          delay(2000);
          UP.write(30);
          delay(2000);
          FORWARD.write(84);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          delay(2000);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(50);
          delay(2000);
          break;
        case 5:  // Действия для случая, когда b[i] равен 5
          Serial.println("Found 5");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(138);
          delay(2000);
          UP.write(12);
          delay(2000);
          FORWARD.write(140);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(40);
          delay(2000);
          break;
        case 6:  // Действия для случая, когда b[i] равен 6
          Serial.println("Found 6");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(174);
          delay(2000);
          UP.write(58);
          delay(2000);
          FORWARD.write(130);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(40);
          delay(2000);
          break;
        case 7:  // Действия для случая, когда b[i] равен 7
          Serial.println("Found 7");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(174);
          delay(2000);
          UP.write(38);
          delay(2000);
          FORWARD.write(160);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(40);
          delay(2000);
          break;
        case 8:  // Действия для случая, когда b[i] равен 8
          Serial.println("Found 8");
          b[i] = -1; // Помечаем этот случай как обработанный
          SIDE.write(176);
          delay(2000);
          UP.write(12);
          delay(2000);
          FORWARD.write(140);
          delay(3000);
          GRAB.write(180);
          delay(2000);
          
          FORWARD.write(0);
          UP.write(0);
          delay(2000);
          SIDE.write(0);
          delay(2000);
          GRAB.write(40);
          delay(2000);
          break;
      default: // Действия по умолчанию, если b[i] не соответствует ни одному из описанных случаев
        UP.write(0);
        FORWARD.write(0);
        SIDE.write(0);
        GRAB.write(46);
          break;
      }
      count++; // Увеличиваем счетчик после каждого случая
     b[i] = -1; // Помечаем случай как обработанный
    if (count == bSize) { // Если обработано всего bSize случаев, то устанавливаем флаг в true и выходим из цикла
        flag = true; 
        break; // Завершение цикла
      }
    }
  }
  if (flag) { // Если флаг true, то выводим сообщение "Done"
    Serial.println("Done");
    
  }

  bool allFound = true;
  for (int i = 0; i < bSize; i++) {
    if (b[i] != -1) { // Если элемент массива b не равен -1, то устанавливаем флаг allFound в false и выходим из цикла
      allFound = false;
      break;
    }
  }

  if (allFound) {
    while (true) {
    }
  }
}