import os
from openai import OpenAI
from pathlib import Path
from PySide6.QtWidgets import (
    QWidget,
)
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class MainWidget(QWidget):
    def __init__(self):
        super(MainWidget, self).__init__()
        MainWidget.win = self.load_ui()

    def get_number_in_sentence(self, sentence):
        """
        Extract the number from the provided sentence
        """
        # Split the sentence into words
        words = sentence.split()

        # Check each word to see if it's a number
        for word in words:
            if word.isdigit():
                return word  # Return the number if found
        return None  # Return None if no number is found

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "../ui/form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        win = loader.load(ui_file, self)
        ui_file.close()

        win.summarize_button.clicked.connect(self.handle_summarize_button_clicked)
        win.back_button.clicked.connect(self.handle_back_button_clicked)

        return win

    def handle_summarize_button_clicked(self):
        """
        Handle the Compare button clicked event.
        """
        apple_text = self.win.apple_text_box.toPlainText()
        meta_text = self.win.meta_text_box.toPlainText()
        sony_text = self.win.sony_text_box.toPlainText()

        # Get mention counts
        apple_mention_count = self.get_device_mention_count(apple_text, "vision pro")
        meta_mention_count = self.get_device_mention_count(meta_text, "quest")
        sony_mention_count = self.get_device_mention_count(sony_text, "vr2")

        # Set the summary to the result label
        self.win.result_label.setText(
            f"{apple_mention_count}, {meta_mention_count}, {sony_mention_count}"
        )

        self.win.stacked_widget.setCurrentIndex(1)

    def handle_back_button_clicked(self):
        self.win.stacked_widget.setCurrentIndex(0)

    def summarize_privacy_policy_direct(self, text_content):
        """
        Summarize the privacy policy text content using the OpenAI API.
        """
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a proficient AI that specializes in extracting information from privacy policies to create a detailed table categorizing the data collection methods, data storage & processing strategies, user consent mechanisms, security measures, and compliance with regulatory standards. It reads text containing privacy policies and identifies specific categories like Data Collection Methods (including cameras, microphones, sensors, eye tracking, biometric data, hand tracking), Data Storage & Processing (focusing on on-device vs. cloud storage, encryption, data minimization, and anonymization), User Consent Mechanisms (consent for data collection, control over data), Security Measures (authentication, data security, regular updates), and Compliance Regulations (GDPR, CCPA).",
                },
                {
                    "role": "user",
                    "content": f"{text_content}\nPlease Extract privacy policy details.",
                },
            ],
            model="gpt-3.5-turbo-1106",
        )

        summary = completion.choices[0].message.content
        return summary

    def get_device_mention_count(self, text_content, device):
        """
        Get the number of times the device was mentioned in the
        provided text using the OpenAI API.
        """
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a proficient AI that specializes in extracting information from privacy policies to create a detailed table categorizing the data collection methods, data storage & processing strategies, user consent mechanisms, security measures, and compliance with regulatory standards. It reads text containing privacy policies and identifies specific categories like Data Collection Methods (including cameras, microphones, sensors, eye tracking, biometric data, hand tracking), Data Storage & Processing (focusing on on-device vs. cloud storage, encryption, data minimization, and anonymization), User Consent Mechanisms (consent for data collection, control over data), Security Measures (authentication, data security, regular updates), and Compliance Regulations (GDPR, CCPA).",
                },
                {
                    "role": "user",
                    "content": f'{text_content}\nPlease tell me the number of times the string "{device} has been explicitly or implicity been mentioned, your answer should be just a single integer and nothing else. I repeat, your answer should be just one word, which is the number.',
                },
            ],
            model="gpt-3.5-turbo-1106",
        )

        count = completion.choices[0].message.content
        return self.get_number_in_sentence(count)
