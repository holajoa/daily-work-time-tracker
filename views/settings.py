from typing import Callable 
from app_settings import save_settings, load_settings
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QComboBox, QSlider
from PyQt5.QtCore import Qt


class SettingsFrame(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        layout = QGridLayout(self)
        
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.parent.show_timer_view)
        layout.addWidget(self.back_button, 0, 0, 1, 2)

        default_settings = load_settings()

        self.font_dropdown_label = QLabel("Select Font", self)
        layout.addWidget(self.font_dropdown_label, 1, 0)

        self.font_dropdown = QComboBox(self)
        self.font_choices = ["Arial", "Times New Roman", "Courier New", "Verdana", "Helvetica", "Fixedsys"]
        self.font_dropdown.addItems(self.font_choices)
        self.font_dropdown.setCurrentText(default_settings.font_name)
        layout.addWidget(self.font_dropdown, 1, 1)

        self.font_size_scale = QSlider(Qt.Horizontal, self)
        self.font_size_scale.setRange(10, 80)
        self.font_size_scale.setValue(default_settings.font_size)
        layout.addWidget(self.font_size_scale, 2, 0, 1, 2)

        self.apply_settings_button = QPushButton("Apply Settings", self)
        self.apply_settings_button.clicked.connect(self.apply_and_callback)
        layout.addWidget(self.apply_settings_button, 3, 0, 1, 2)

        self.default_button = QPushButton("Save as Default", self)
        self.default_button.clicked.connect(self.save_as_default)
        layout.addWidget(self.default_button, 4, 0, 1, 2)
        
        self.setLayout(layout)

    def apply_and_callback(self):
        self.parent.app_settings.font_name = self.font_dropdown.currentText()
        self.parent.app_settings.font_size = self.font_size_scale.value()
        self.parent.apply_settings()

    def save_as_default(self):
        self.parent.app_settings.font_name = self.font_dropdown.currentText()
        self.parent.app_settings.font_size = self.font_size_scale.value()
        save_settings(self.parent.app_settings)