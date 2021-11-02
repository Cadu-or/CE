from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from mesa.visualization.modules import NetworkModule
from .model import AreaNetwork

'''
Declaração do grafo para demonstração da relação entre as grandes áreas de conhecimento.
'''
def network_area(G):
    areas = dict()
    areas["nodes"] = [
        {
            "id": "multi",
            "size": 5,
            "color": "#FF007F",
            "label": "Multidisciplinar"
        },
        {
            "id": "engenharias",
            "size": 5,
            "color": "#00FF00",
            "label": "Engenharias"
        },
        {
            "id": "saude",
            "size": 5,
            "color": "#2986CC",
            "label": "Ciências da Saúde"
        },
        {
            "id": "humanas",
            "size": 5,
            "color": "#6A329F",
            "label": "Ciências Humanas"
        },
        {
            "id": "linguistica",
            "size": 5,
            "color": "#6CE2C9",
            "label": "Linguística, Letras e Artes"
        },
        {
            "id": "biologicas",
            "size": 5,
            "color": "#CC0000",
            "label": "Ciências Biólogicas"
        },
        {
            "id": "agraria",
            "size":5,
            "color": "#F9D71C",
            "label": "Ciências Agrárias"
        },
        {
            "id": "sociais",
            "size": 5,
            "color" : "#654321",
            "label": "Ciências Sociais Aplicadas"
        },
        {
            "id": "exatas",
            "size": 5,
            "color": "#C2C5CC",
            "label": "Ciências Exatas e da Terra"
        }
    ]

    areas["edges"] = [
        {"id": "1", "source": "multi", "target": "humanas", "color": "#000000"},
        {"id": "2", "source": "multi", "target": "biologicas", "color": "#000000"},
        {"id": "3", "source": "multi", "target": "exatas", "color": "#000000"},
        {"id": "4", "source": "multi", "target": "agraria", "color": "#000000"},
        {"id": "5", "source": "biologicas", "target": "agraria", "color": "#000000"},
        {"id": "6", "source": "exatas", "target": "engenharias", "color": "#000000"},
        {"id": "7", "source": "linguistica", "target": "humanas", "color": "#000000"},
        {"id": "8", "source": "sociais", "target": "humanas", "color": "#000000"},
        {"id": "9", "source": "biologicas", "target": "saude", "color": "#000000"}
    ]

    return areas

# Definicao do grafo
grid = NetworkModule(network_area, 500, 500, library="sigma")

'''
Declaração do grafico de linhas para demonstração do crescimento da produção
dos projetos de cada grande área.
'''
chart = ChartModule([
    {
        "Label": "Multidisciplinar",
        "Color": "Pink"
    },
    {
        "Label": "Engenharias",
        "Color": "Green"
    },
    {
        "Label": "Ciências da Saúde",
        "Color": "Blue"
    },
    {
        "Label": "Ciências Humanas",
        "Color": "Purple"
    },
    {
        "Label": "Ciências Agrarias",
        "Color": "Yellow"
    },
    {
        "Label": "Linguística, Letras e Artes",
        "Color": "Cyan"
    },
    {
        "Label": "Ciências Exatas",
        "Color": "Gray"
    },
    {
        "Label": "Ciências Biologicas",
        "Color": "Red"
    },
    {
        "Label": "Ciências Sociais",
        "Color": "Brown"
    }
    ], data_collector_name="datacollector")

# Declaração do server
server = ModularServer(
    AreaNetwork, [grid, chart], "Projects Model"
)
server.port = 3000