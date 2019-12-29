from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

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
        self.wait_for_row_in_list_table('1: Comprar penas de pavão')

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item.
        # Ela insere "Usar penas de pavão para fazer um fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Usar penas de pavão para fazer um fly')
        inputbox.send_keys(Keys.ENTER)

        # A página é atualizada novamente e agora mostra os dois itens em sua lista
        self.wait_for_row_in_list_table('1: Comprar penas de pavão')
        self.wait_for_row_in_list_table('2: Usar penas de pavão para fazer um fly')

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota que o site
        # gerou um URL único para ela -- há um pequeno texto explicativo para isso.

        # TODO: Aceitar mais de uma lista
        self.fail('Finish the test!')


        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita ela volta a dormir
