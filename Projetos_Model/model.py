from mesa import Agent, Model
from mesa import datacollection
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import networkx as nx
from mesa.space import NetworkGrid
import random
import math

# Quantidade de projetos Iniciais para a alocacao em areas de pesquisa
projetos = 1

'''
Classe para a geracao da visualizacao baseado nos atributos e metodos dos agentes.
'''
class AreaNetwork(Model):
    def __init__(self, areas=9):
        self.num_agents = areas
        self.G = nx.erdos_renyi_graph(n=0, p=0.5)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)
        list_ids = [[1,3,2,4], [0,6,7], [0,3,8], [0,2], [0,5], [4], [1], [1], [2]]
        list_areas = [4, 3, 3, 2, 2, 1, 1, 1, 1]
        
        # cria os agentes
        for i in range(self.num_agents):
            a = ProjectAgent(i, self, list_areas[i],list_ids[i])
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
    def __init__(self, unique_id, model, edges, areas):
        super().__init__(unique_id, model)               
        self.edges = edges      # Relacoes entre projetos
        self.areas = areas
        self.projects = 0       # Quantidade de projeto

    def setprojects(self):
        global projetos        
        # Incrementa a quantidade de projetos de acordo com o numero de ligacoes que possui
        aux = 0
        # Soma o numero de projetos de cada area de conhecimento ligada a area atual
        for i in range(self.edges):
            aux += self.model.schedule.agents[self.areas[i]].getprojects()

        # O numero de projetos da area depende do numero de areas relacionadas e a soma feita anteriormente
        self.projects += math.ceil(random.randint(1, (projetos*self.edges)+ math.ceil(aux*0.2))/9)

    def getprojects(self):
        return self.projects    # Retorna o quantitativo de projetos

    def step(self):
        global projetos
        self.setprojects()      # Chama a funcao de incremento de projetos a cada step
