from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

def cluster_deliveries(csv_path, n_clusters=2):
    # Carrega os dados do arquivo CSV
    data = pd.read_csv(csv_path)

    # Seleciona apenas as coordenadas
    coords = data[['x', 'y']]

    # Cria o modelo K-Means
    model = KMeans(n_clusters=n_clusters, random_state=42)

    # Ajusta o modelo aos dados e cria os clusters
    data['cluster'] = model.fit_predict(coords)

    return data

def plot_clusters(data):
    plt.figure()
    plt.scatter(data['x'], data['y'], c=data['cluster'])
    plt.title("Clusterização das Entregas")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.savefig("docs/grafico_clusters.png")
    plt.show()
