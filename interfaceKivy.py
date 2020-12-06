from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests
import json

class BuscaDados(GridLayout):
    def __init__(self, **kwargs):
        super(BuscaDados, self).__init__(**kwargs)
        urlId = 'https://api.thingspeak.com/channels/1229472/fields/1.json?api_key=LI404MY14S9WW1Q3&results=100'
        urlTemp = 'https://api.thingspeak.com/channels/1229472/fields/2.json?api_key=LI404MY14S9WW1Q3&results=100'
        urlHumi = 'https://api.thingspeak.com/channels/1229472/fields/3.json?api_key=LI404MY14S9WW1Q3&results=100'

        #propriedades que rececebem a resposta da requisição feita ao thingspeak
        self.campoId = requests.get(urlId)
        self.campoTemp = requests.get(urlTemp)
        self.campoHumi = requests.get(urlHumi)

        #definindo total de linhas da tela
        self.rows = 3

        #definindo box que recebera as labals e seu tamanho
        self.paineis = BoxLayout()
        self.paineis.size_hint_max_y= 80
        #passando valores a ela
        self.paineis.add_widget(Label(text='Id'))
        self.paineis.add_widget(Label(text='Temperatura'))
        self.paineis.add_widget(Label(text='Humidade'))
        #adicionando a tela
        self.add_widget(self.paineis)

        #definindo box que recebera os valores do thingspeak
        self.caixasDeTexto = BoxLayout()
        #criando textinputs
        self.panelTemp = TextInput()
        self.panelHumid = TextInput()
        self.panelId = TextInput()
        #adicionando ao box
        self.caixasDeTexto.add_widget(self.panelId)
        self.caixasDeTexto.add_widget(self.panelTemp)
        self.caixasDeTexto.add_widget(self.panelHumid)
        #adicionando o box a tela
        self.add_widget(self.caixasDeTexto)

        #botão que chama o metodo...
        self.buscarDados = Button(text='Buscar Dados',on_press=self.buscar)
        #definindo a altura com size_hint_max_y, largura usar size_hint_max_x
        self.buscarDados.size_hint_max_y = 80
        #adicionando botao de fazer a requisicao na tela
        self.add_widget(self.buscarDados)

    def buscar(self, button):
        Testeid = self.campoId.json()
        temp = self.campoTemp.json()
        humi = self.campoHumi.json()
        self.panelId.text = ''
        self.panelTemp.text = ''
        self.panelHumid.text = ''

        for y in Testeid['feeds']:
            self.panelId.text += str(y['field1'] + '\n')

        for t in temp['feeds']:
            self.panelHumid.text += str(t['field2'] + '\n')

        for h in humi['feeds']:
            self.panelTemp.text += str(h['field3'] + '\n')

class MyApp(App):
    def build(self):
        return BuscaDados()


MyApp().run()
