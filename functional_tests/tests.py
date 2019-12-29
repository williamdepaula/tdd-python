from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicação online interessante
        # para listas de tarefas. Ela decide verificar sua homepage
        self.browser.get(self.live_server_url)

        # Ela percebe que o titulo da página e o cabeçalho mencionam
        # lista de tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidade a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Entre com um to-do item'
        )

        # Ela digita "Comprar penas de pavão" em uma caixa de
        # texto
        inputbox.send_keys('Comprar penas de pavão')

        # Quando ela tecla enter, a página é atualizada, e agora a página lista
        # 1 - Comprar penas de pavão como um item de uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Comprar penas de pavão', [row.text for row in rows])

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item.
        # Ela insere "Usar penas de pavão para fazer um fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Usar penas de pavão para fazer um fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A página é atualizada novamente e agora mostra os dois itens em sua lista
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Comprar penas de pavão', [row.text for row in rows])
        self.assertIn('2: Usar penas de pavão para fazer um fly', [row.text for row in rows])


        # Edith se pergunta se o site lembrará de sua lista. Então ela nota que o site
        # gerou um URL único para ela -- há um pequeno texto explicativo para isso.

        # TODO: Aceitar mais de uma lista
        self.fail('Finish the test!')


        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita ela volta a dormir