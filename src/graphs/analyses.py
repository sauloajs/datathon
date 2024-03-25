import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from wordcloud import WordCloud
import matplotlib.pyplot as plt

from src.utils.format_helpers import *
from src.utils.colors import *

ABS_PATH = './src/assets/data'

df = pd.read_csv(f'{ABS_PATH}/datas-fd.csv')

def getIegXIndeGraph():
    sns.scatterplot(data=df, x='IEG_2020', y='INDE_2020', color=COLOR_PALETTE['yellow'])
    sns.set_palette(COLOR_PALETTE.values())
    plt.title('Relação entre IEG_2020 e INDE_2020')
    plt.xlabel('IEG_2020')
    plt.ylabel('INDE_2020')
    
    st.pyplot(plt)
    
def getEngagementClustersGraph():
    X = df[['IEG_2020']]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3)  # Escolha o número de clusters com base na análise
    df['Cluster_IEG'] = kmeans.fit_predict(X_scaled)

    # Define custom color palette
    custom_palette = COLOR_PALETTE.values()  # Example custom palette

    # Set the color palette
    sns.set_palette(custom_palette)

    # Visualizando os clusters de engajamento
    sns.scatterplot(data=df, x='IEG_2020', y='INDE_2020', hue='Cluster_IEG', palette=["#012b66", "#f6a522", "#ff5216"])
    plt.title('Clusters de Engajamento')
    plt.xlabel('IEG_2020')
    plt.ylabel('INDE_2020')
    # plt.show()
    
    st.pyplot(plt)


def getLongCluster(ano):
    if f'IEG_{ano}' and f'IDA_{ano}' and f'INDE_{ano}' in df.columns:
        X_cluster = df[[f'IEG_{ano}', f'IDA_{ano}', f'INDE_{ano}']].dropna()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_cluster)

        kmeans = KMeans(n_clusters=3, random_state=42)
        df[f'Cluster_{ano}'] = kmeans.fit_predict(X_scaled)

        sns.scatterplot(x=f'IEG_{ano}', y=f'INDE_{ano}', hue=f'Cluster_{ano}', data=df, palette=["#012b66", "#f6a522", "#ff5216"])
        plt.title(f'Clusters de Engajamento e Desempenho em {ano}')
        
        st.pyplot(plt)
    
def getEngagementWorldCloud(ano):
    if f'DESTAQUE_IEG_{ano}' in df.columns:
        textos_concatenados = ' '.join(df[f'DESTAQUE_IEG_{ano}'].dropna().astype(str))
        wordcloud = WordCloud(stopwords=['de', 'e', 'o', 'a', 'em', 'que', 'do', 'sua', 'seu', 'destaque', 'das', 'nas'], background_color='white').generate(textos_concatenados)
        
        plt.figure(figsize=(5.5, 2.5))
        plt.imshow(wordcloud, interpolation='bilinear', aspect='auto')
        
        plt.axis('off')
        st.pyplot(plt, None, False)