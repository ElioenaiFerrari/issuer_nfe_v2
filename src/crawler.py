import os
import sys
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class Crawler:
    def __init__(self):
        self.company = [
            {
                'id': 'qycnpjcpf',
                'value': os.environ.get("COMPANY_CNPJ")
            },
            {
                'id': 'qynome',
                'value': os.environ.get("COMPANY_NAME")
            },
            {
                'id': 'input8',
                'value': os.environ.get("COMPANY_ZIP_CODE")
            },
            {
                'id': 'input4',
                'value': os.environ.get("COMPANY_DISTRICT")
            },
            {
                'id': 'input5',
                'value': os.environ.get("COMPANY_NAME")
            },
            {
                'id': 'input2',
                'value': os.environ.get("COMPANY_CITY")
            },
            {
                'id': 'input3',
                'value': os.environ.get("COMPANY_STATE")
            },
            {
                'id': 'input6',
                'value': os.environ.get("COMPANY_STREET")
            },
            {
                'id': 'input10',
                'value': os.environ.get("COMPANY_EMAIL")
            },
            {
                'id': 'qyrginscrestadual',
                'value': os.environ.get("COMPANY_CNPJ")
            },
            {
                'id': 'icodigo',
                'value': os.environ.get("NOTE_CODE")
            },
            {
                'id': 'qynfitensqtd',
                'value': os.environ.get("NOTE_QUANTITY")
            },
            {
                'id': 'qynfitensvlrunitario',
                'value': os.environ.get("NOTE_VALUE")
            },

        ]

        self.user = [
            {
                'id': 'usuario',
                'value': os.environ.get("USER_CNPJ")
            },
            {
                'id': 'senha',
                'value': os.environ.get("USER_PASS")
            }
        ]

        url = os.environ.get("URL")
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(
            "/Users/elioenaiferrari/Documents/drivers/chromedriver", options=options)

        self.driver.get(url)

    def signin(self):

        for field in self.user:
            self.driver.find_element_by_id(
                field['id']).send_keys(field['value'])

        submit = self.driver.find_element_by_class_name('textoButton')

        submit.click()

    def open_notes_page(self):
        note_tab = self.driver.find_element_by_id("img1")

        note_tab.click()

    def scrap(self):
        self.signin()

        sleep(1)

        self.open_notes_page()

        sleep(1)

        self.fill_form()

        sleep(10)

    def fill_form(self):
        service = self.driver.find_element_by_id("qyidatividade")
        Select(service).select_by_value(os.environ.get("USER_SERVICE_CODE"))

        for field in self.company:
            self.driver.find_element_by_id(
                field['id']).send_keys(field['value'])

        note_total = self.driver.find_element_by_id("qynfitensvlrtotal")
        insert_note = self.driver.find_element_by_id("imagebutton1Imagem")
        confirm_note = self.driver.find_element_by_id("imagebutton4Texto")

        note_total.click()
        insert_note.click()
        sleep(1)
        confirm_note.click()
