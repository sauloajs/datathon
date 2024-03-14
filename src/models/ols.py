from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd


def getOLS():
    df = pd.read_csv('./src/assets/data/datas-fd.csv')

    # Preparando os dados para a análise de clusters
    variaveis_de_interesse = ['IDADE_ALUNO_2020', 'ANOS_PM_2020', 'IEG_2020', 'IDA_2020', 'INDE_2020', 'IPS_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020']
    dados_para_cluster = df[variaveis_de_interesse].dropna()

    # Normalizando os dados
    scaler = StandardScaler()
    dados_normalizados = scaler.fit_transform(dados_para_cluster)

    # Redução de dimensionalidade (opcional, para visualização)
    pca = PCA(n_components=2)
    dados_reduzidos = pca.fit_transform(dados_normalizados)

    # Aplicação do K-Means
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(dados_reduzidos)

    # Adicionando os clusters ao DataFrame original
    df['Cluster'] = clusters

    # Visualização dos clusters (se houver redução de dimensionalidade)
    plt.scatter(dados_reduzidos[:, 0], dados_reduzidos[:, 1], c=df['Cluster'])
    plt.title("Clusters de Alunos")
    plt.xlabel("PCA 1")
    plt.ylabel("PCA 2")
    plt.show()

    # Assumindo que 'df' é o seu DataFrame e que 'INDE_2020' é a variável que você quer prever
    variaveis_independentes = ['IDADE_ALUNO_2020', 'ANOS_PM_2020', 'IEG_2020', 'IDA_2020', 'IPS_2020', 'IPP_2020', 'IPV_2020', 'IAN_2020', 'Cluster']

    X = df[variaveis_independentes]  # Certifique-se de que INDE_2020 não está incluído aqui
    Y = df['INDE_2020']

    # Adicionando uma constante ao modelo
    X = sm.add_constant(X)

    # Criando o modelo de regressão
    modelo = sm.OLS(Y, X).fit()

    return modelo