# <img width="32" height="32" alt="min" src="assets/icon.png" /> min Tool
Доведи количество ***мусора*** на ТВОЁМ телефоне до ***минимума***

С 1 сентября 2025 года на все телефоны официально ввозимые в Россию для последующей продажи начали предустанавливать мессенджер MAX, но не со всех его можно удалить - на многих устройствах MAX устанавливается как системное приложение, и просто так удалить его не получится

Для этого был создан min - инструмент для удаления мессенджера там, где его обычно не получится удалить

<a href="https://github.com/Forbirdden/min-max-uninstaller/releases/latest/download/windows.zip"><img alt="Скачать для Windows" src="https://img.shields.io/github/downloads/Forbirdden/min-max-uninstaller/latest/windows.zip?displayAssetName=false&style=for-the-badge&logo=Wine&label=%D0%A1%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C%20%D0%B4%D0%BB%D1%8F%20Windows&labelColor=%230390fc&color=%23f0f0f0"></a>

<a href="https://github.com/Forbirdden/min-max-uninstaller/releases/latest/download/linux.zip"><img alt="Скачать для Linux" src="https://img.shields.io/github/downloads/Forbirdden/min-max-uninstaller/latest/linux.zip?displayAssetName=false&style=for-the-badge&logo=Linux&logoColor=fff&label=%D0%A1%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C%20%D0%B4%D0%BB%D1%8F%20GNU%2FLinux&labelColor=%230390fc&color=%23f0f0f0"></a>

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
Для сборки и работы нужна папка assets из репозитория
Windows:
```
build.cmd
```
Linux:
```
make
```
