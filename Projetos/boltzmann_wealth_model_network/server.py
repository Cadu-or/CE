from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from mesa.visualization.modules import ChartModule
from mesa.visualization.modules import NetworkModule
from .model import BoltzmannWealthModelNetwork


# def network_portrayal(G):
#     # The model ensures there is 0 or 1 agent per node

#     portrayal = dict()
#     portrayal["nodes"] = [
#         {
#             "id": node_id,
#             "size": 3 if agents else 1,
#             "color": "#CC0000" if not agents or agents[0].wealth == 0 else "#007959",
#             "label": None
#             if not agents
#             else "Agent:{} Wealth:{}".format(agents[0].unique_id, agents[0].wealth),
#         }
#         for (node_id, agents) in G.nodes.data("agent")
#     ]

#     portrayal["edges"] = [
#         {"id": edge_id, "source": source, "target": target, "color": "#000000"}
#         for edge_id, (source, target) in enumerate(G.edges)
#     ]

#     return portrayal

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

# grid = NetworkModule(network_portrayal, 500, 500, library="sigma")
grid2 = NetworkModule(network_area, 500, 500, library="sigma")


# chart = ChartModule(
#     [{"Label": "Gini", "Color": "Black"}], data_collector_name="datacollector"
# )
chart2 = ChartModule([
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
    },

], data_collector_name="datacollector2")

# model_params = {
#     "num_agents": UserSettableParameter(
#         "slider",
#         "Number of agents",
#         7,
#         2,
#         10,
#         1,
#         description="Choose how many agents to include in the model",
#     ),
#     "num_nodes": UserSettableParameter(
#         "slider",
#         "Number of nodes",
#         10,
#         3,
#         12,
#         1,
#         description="Choose how many nodes to include in the model, with at "
#         "least the same number of agents",
#     ),
# }

server = ModularServer(
    BoltzmannWealthModelNetwork, [grid2, chart2], "Projects Model"
)
server.port = 3000