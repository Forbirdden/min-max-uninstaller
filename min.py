import sys
import os
import subprocess
import platform
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QPushButton, QTextEdit, QLabel, 
                               QProgressBar, QMessageBox, QGroupBox)
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QFont, QPalette, QColor

class ADBWorker(QThread):
    log_signal = Signal(str)
    progress_signal = Signal(int)
    finished_signal = Signal(bool, str)

    def __init__(self, adb_path, max_id="ru.oneme.app"):
        super().__init__()
        self.adb_path = adb_path
        self.max_id = max_id
        self.is_running = True

    def run(self):
        try:
            self.log_signal.emit("Проверяем подключение устройства...")
            self.progress_signal.emit(10)

            # Проверяем наличие подключенных устройств
            result = self.run_adb_command("devices")
            devices = [line for line in result.split('\n') if '\tdevice' in line]
            
            if not devices:
                self.finished_signal.emit(False, "Устройство не найдено, убедитесь что оно подключено к ПК кабелем с поддержкой передачи данных, а на самом телефоне включён ADB")
                return

            self.log_signal.emit(f"Найдено устройств: {len(devices)}")
            self.progress_signal.emit(30)

            # Проверяем установлен ли MAX
            self.log_signal.emit("Проверяем наличие мессенджера MAX...")
            packages = self.run_adb_command("shell pm list packages")
            
            if self.max_id not in packages:
                self.finished_signal.emit(False, "Приложение MAX не найдено на устройстве")
                return

            self.log_signal.emit("MAX обнаружен, запускаем противотанковый гранатомёт...")
            self.progress_signal.emit(50)

            # Пытаемся удалить приложение
            result = self.run_adb_command(f"shell pm uninstall -k --user 0 {self.max_id}")
            
            if "Success" in result:
                self.log_signal.emit("ЦЕЛЬ ЛИКВИДИРОВАНА")
                self.progress_signal.emit(100)
                self.finished_signal.emit(True, "Удаление завершено успешно")
            else:
                    self.finished_signal.emit(False, "Не удалось удалить мессенджер MAX")

        except Exception as e:
            self.finished_signal.emit(False, f"Ошибка: {str(e)}")

    def run_adb_command(self, command):
        try:
            full_command = f'"{self.adb_path}" {command}'
            result = subprocess.run(full_command, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout + result.stderr
        except subprocess.TimeoutExpired:
            return "Timeout error"
        except Exception as e:
            return f"Command error: {str(e)}"

    def stop(self):
        self.is_running = False

class MaxRemoverApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("min Tool")
        self.setGeometry(50, 50, 400, 400)
        self.setup_ui()
        
        self.adb_path = self.find_adb()
        if not self.adb_path:
            self.show_error("ADB не найден в папке с программой")

    def find_adb(self):
        if getattr(sys, 'frozen', False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).parent
        
        current_platform = platform.system()
        
        if current_platform == "Windows":
            adb_exe = base_dir / "adb.exe"
            if adb_exe.exists():
                return str(adb_exe)
            for path in base_dir.rglob("adb.exe"):
                return str(path)
        else:
            adb_bin = base_dir / "adb"
            if adb_bin.exists():
                try:
                    os.chmod(str(adb_bin), 0o755)
                except:
                    pass
                return str(adb_bin)
            try:
                result = subprocess.run(["which", "adb"], capture_output=True, text=True)
                if result.returncode == 0:
                    return result.stdout.strip()
            except:
                pass
        
        return None

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        title_label = QLabel("min: удаление MAX")
        title_label.setAlignment(Qt.AlignCenter)
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        layout.addWidget(title_label)

        desc_label = QLabel('<a href="https://github.com/Forbirdden/min-max-uninstaller">Инструкция</a>')
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setOpenExternalLinks(True)
        layout.addWidget(desc_label)

        status_group = QGroupBox("Статус")
        status_layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        status_layout.addWidget(self.progress_bar)
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(200)
        status_layout.addWidget(QLabel("Лог выполнения:"))
        status_layout.addWidget(self.log_text)
        status_group.setLayout(status_layout)
        layout.addWidget(status_group)

        self.remove_button = QPushButton("Удалить MAX")
        self.remove_button.clicked.connect(self.start_removal)
        self.remove_button.setStyleSheet("QPushButton { background-color: #dc3545; color: white; font-weight: bold; }")
        layout.addWidget(self.remove_button)

        self.worker = None

    def log_message(self, message):
        self.log_text.append(message)

    def clear_log(self):
        self.log_text.clear()
        self.progress_bar.setValue(0)

    def start_removal(self):
        if not self.adb_path:
            self.show_error("ADB не найден в папке с программой")
            return

        reply = QMessageBox.question(self, "Подтверждение", "\"Спрашиваешь ещё конечно да\"", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.remove_button.setEnabled(False)
            self.clear_log()
            self.worker = ADBWorker(self.adb_path)
            self.worker.log_signal.connect(self.log_message)
            self.worker.progress_signal.connect(self.progress_bar.setValue)
            self.worker.finished_signal.connect(self.on_removal_finished)
            self.worker.start()

    def on_removal_finished(self, success, message):
        self.remove_button.setEnabled(True)
        if success:
            QMessageBox.information(self, "Успех", message)
        else:
            QMessageBox.warning(self, "Ошибка", message)

    def show_error(self, message):
        QMessageBox.critical(self, "Ошибка", message)

    def closeEvent(self, event):
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.wait(2000)
        event.accept()

def main():
    app = QApplication(sys.argv)
    
    # Устанавливаем стиль
    app.setStyle('Fusion')
    
    window = MaxRemoverApp()
    window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
