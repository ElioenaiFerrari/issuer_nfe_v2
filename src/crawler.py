import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class Crawler:
    def __init__(self, user, company, note):
        self.company = [
            {
                'id': 'qycnpjcpf',
                'value': company['cnpj']
            },
            {
                'id': 'qynome',
                'value': company['name']
            },
            {
                'id': 'input8',
                'value': company['zip_code']
            },
            {
                'id': 'input4',
                'value': company['district']
            },
            {
                'id': 'input5',
                'value': company['name']
            },
            {
                'id': 'input2',
                'value': company['city']
            },
            {
                'id': 'input3',
                'value': company['state']
            },
            {
                'id': 'input6',
                'value': company['street']
            },
            {
                'id': 'input10',
                'value': company['email']
            },
            {
                'id': 'qyrginscrestadual',
                'value': company['cnpj']
            },
            {
                'id': 'icodigo',
                'value': note['code']
            },
            {
                'id': 'qynfitensqtd',
                'value': note['quantity']
            },
            {
                'id': 'qynfitensvlrunitario',
                'value': note['unit_value']
            },

        ]

        self.user = [
            {
                'id': 'usuario',
                'value': user['username']
            },
            {
                'id': 'senha',
                'value': user['password']
            }
        ]

        self.service_code = user['service_code']

        url = os.environ.get("URL")
        options = Options()
        options.headless = False
        self.driver = webdriver.Chrome(
            os.environ.get('CHROMEDRIVER_PATH'), options=options)

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

        sleep(1)

        return {
            'code': self.driver.find_element_by_id("icodigo").get_attribute('value'),
            'quantity': self.driver.find_element_by_id("qynfitensqtd").get_attribute('value'),
            'unit_value': self.driver.find_element_by_id("qynfitensvlrunitario").get_attribute('value'),
        }

        # self.issue()

    def fill_form(self):
        service = self.driver.find_element_by_id("qyidatividade")
        Select(service).select_by_value(self.service_code)

        for field in self.company:
            self.driver.find_element_by_id(
                field['id']).send_keys(field['value'])

    def issue(self):
        note_total = self.driver.find_element_by_id("qynfitensvlrtotal")
        insert_note = self.driver.find_element_by_id("imagebutton1Imagem")
        confirm_note = self.driver.find_element_by_id("imagebutton4Texto")

        note_total.click()
        insert_note.click()
        sleep(1)
        confirm_note.click()
