# <img width="32" height="32" alt="min" src="https://github.com/user-attachments/assets/1cb45186-3186-47de-ac11-b003bf92dcda" /> min Tool
Доведи количество ***мусора*** на СВОЁМ телефоне до ***минимума***

С 1 сентября 2025 года на все телефоны официально ввозимые в Россию для последующей продажи начали предустанавливать мессенджер MAX, но не со всех его можно удалить - на многих устройствах MAX устанавливается как системное приложение, и просто так удалить его не получится

Для этого был создан Min - инструмент для удаления мессенджера там, где его обычно не получится удалить

## Инструкция по использованию
1) Откройте настройки разработчика на телефоне (как это сделать именно на своём устройстве можно узнать в интернете)
<img width="217" height="38" alt="image" src="https://github.com/user-attachments/assets/b500aadf-8e5f-4021-8bdd-0fb3561e1865" />

2) Включите отладку по USB (если есть дополнительный параметр, например "настройки безопасности" его тоже нужно включить)
<img width="195" height="58" alt="image" src="https://github.com/user-attachments/assets/d8dc135b-55d8-4e04-9033-81d00e21e150" />

3) Скачайте, ***распакуйте*** и откройте Min на своём ПК
<img width="256" height="293" alt="image" src="https://github.com/user-attachments/assets/06263778-8e50-4382-b4b9-c9676f25abdf" />

4) Подключите телефон к ПК используя кабель с поддержкой передачи данных (скорее всего такой есть на вашей заводской зарядке)
<img width="256" height="256" alt="image" src="https://github.com/user-attachments/assets/47243768-9020-4a36-8e4e-f8cf10f5cce5" />

5) Запустите Min, если на телефоне появится потдверждение/запрос ADB то разрешите подключение
<img width="222" height="200" alt="image" src="https://github.com/user-attachments/assets/6a472aad-6df6-4714-add6-1468172ed08e" />

6) Нажмите большую красную кнопку, вы точно не перепутаете
<img width="391" height="37" alt="image" src="https://github.com/user-attachments/assets/d3117d59-a960-4de9-ab46-1961fa8d99a9" />

## Сборка
Для клонирования репозитория нужен Git (но можно и просто скачать репозиторий с сайта), для сборки нужен Python
### Клонирование репозитория:
```
git clone https://github.com/Forbirdden/min-max-uninstaller.git
cd min
```
### Установка QT и pyinstaller:
```
pip install PySide6 pyinstaller
```
### Запаковка:
Windows:
```
python -m PyInstaller --onefile --windowed --name "min" --add-data "adb.exe;." min.py
```
Linux/MacOS:
```
python -m PyInstaller --onefile --windowed --name "min" --add-data "adb:." min.py
```
Также для работы нужен файл adb(или adb.exe) в той же самой папке, что и запакованный min, скачать adb можно с сайта Google:

[Windows](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)

[MacOS](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)

[Linux](https://dl.google.com/android/repository/platform-tools-latest-linux.zip)
