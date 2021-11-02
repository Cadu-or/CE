from mesa import Agent, Model
from mesa import datacollection
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import networkx as nx
from mesa.space import NetworkGrid
import random

# Quantidade de projetos Iniciais para a alocacao em areas de pesquisa
projetos = 10

'''
Classe para a geracao da visualizacao baseado nos atributos e metodos dos agentes.
'''
class AreaNetwork(Model):
    def __init__(self, areas=9):
        self.num_agents = areas
        self.G = nx.erdos_renyi_graph(n=0, p=0.5)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)
        list_areas = [4, 3, 3, 2, 2, 1, 1, 1, 1]

        # cria os agentes
        for i in range(self.num_agents):
            a = ProjectAgent(i, self, list_areas[i])
            self.schedule.add(a)

        # Retorna os valores dos projetos de cada area
        self.datacollector = DataCollector(
            model_reporters={"Multidisciplinar": self.schedule.agents[0].getprojects,
                             "Ciências Humanas": self.schedule.agents[1].getprojects,
                             "Ciências Biologicas": self.schedule.agents[2].getprojects,
                             "Ciências Agrarias": self.schedule.agents[3].getprojects,
                             "Ciências Exatas": self.schedule.agents[4].getprojects,
                             "Engenharias": self.schedule.agents[5].getprojects,
                             "Linguística, Letras e Artes": self.schedule.agents[6].getprojects,
                             "Ciências Sociais": self.schedule.agents[7].getprojects,
                             "Ciências da Saúde": self.schedule.agents[8].getprojects
                            })

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        global projetos
        self.schedule.step()
        self.datacollector.collect(self)
        projetos += 1

    def run_model(self, n):
        global projetos
        for _ in range(n):
            self.step()


'''
Areas de conhecimento sendo tratadas como agentes.
'''

class ProjectAgent(Agent):
    def __init__(self, unique_id, model, edges):
        super().__init__(unique_id, model)               
        self.edges = edges      # Relacoes entre projetos
        self.projects = 0       # Quantidade de projeto

    def setprojects(self):
        global projetos         # Pega a relacao de quantos projetos existem ate o momento
        self.projects += random.randint(1, projetos*self.edges)    # Incrementa relacionando com a quantidade de ligacoes que possui

    def getprojects(self):
        return self.projects    # Retorna o valor dos projetos

    def step(self):
        global projetos
        self.setprojects()      # Chama a funcao de incremento de projetos a cada step.
