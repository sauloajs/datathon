import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.utils.format_helpers import *
from src.utils.colors import *

ABS_PATH = './src/assets/data'

def plotEducationalDistGraph():
    dfMat = pd.read_csv(f"{ABS_PATH}/matriculas.csv")

    dfMat['Educação infantil'] = dfMat['Educação infantil'].apply(replace_percentage)
    dfMat['Ensino Fundamental 1'] = dfMat['Ensino Fundamental 1'].apply(replace_percentage)
    dfMat['Ensino Fundamental 2'] = dfMat['Ensino Fundamental 2'].apply(replace_percentage)
    dfMat['Ensino Médio'] = dfMat['Ensino Médio'].apply(replace_percentage)
    
    categories = dfMat.set_index('Cidade').T.index
    groups = ['Embu-Guaçu', 'Brasil', 'São Paulo']
    data = {
        'Educação infantil': dfMat.set_index('Cidade')['Educação infantil'].values,
        'Ensino Fundamental 1': dfMat.set_index('Cidade')['Ensino Fundamental 1'].values,
        'Ensino Fundamental 2': dfMat.set_index('Cidade')['Ensino Fundamental 2'].values,
        'Ensino Médio': dfMat.set_index('Cidade')['Ensino Médio'].values
    }

    categoryColors = {
        'Educação infantil': 'blue',
        'Ensino Fundamental 1': 'light_blue',
        'Ensino Fundamental 2': 'yellow',
        'Ensino Médio': 'green'
    }

    traces = []
    for category in categories:
        trace = go.Bar(
            x=groups, 
            y=[data[category][i] for i in range(len(groups))], 
            name=category,
            text=[f'{data[category][i]}%' for i in range(len(groups))],
            textposition='inside',
            textfont=dict(color='white', size=20),
            width=0.3,
            marker=dict(color=COLOR_PALETTE[categoryColors[category]]),
        )
        traces.append(trace)

    layout = go.Layout(
        title={
            'text':'Associação Passos Mágicos concentra o atendimento nas turmas de ensino fundamental',
            'font': dict(color='#333', size=12)
        },
        barmode='stack'
    )

    fig = go.Figure(data=traces, layout=layout)
    fig.update_layout(
        title_x=0.12,
        legend=dict(x=0.25, y=-0.2, orientation='h', font=dict(color='black')),
        xaxis=dict(showgrid=False, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, tickfont=dict(color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        width=650
    )
    
    st.plotly_chart(fig)
    
def plotSchoolsAdm():
    dfsadm = pd.read_csv(f"{ABS_PATH}/school_adm.csv")

    dfsadm = dfsadm.set_index('Cidade')
    
    cities = dfsadm.index
    groups = dfsadm.columns

    traces = []

    GROUP_COLORS = {
        'Privada': 'light_blue',
        'Federal': 'red',
        'Estadual': 'blue',
        'Municipal': 'yellow'

    }

    for group in groups:
        data = dfsadm[group].apply(replace_percentage).values
        traces.append(
            go.Bar(
                x=cities, 
                y=data, 
                name=group,
                width=0.17,
                text=[f'{dfsadm[group][i]}' for i in range(len(cities))],
                textposition='outside',
                textfont=dict(color='black'),
                marker=dict(color=COLOR_PALETTE[GROUP_COLORS[group]]),
            )
        )
        
    layout = go.Layout(
        xaxis=dict(showgrid=False, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, range=[0, 60], tickfont=dict(color='black')),
        plot_bgcolor='white',
        legend=dict(x=0.13, y=-0.2, orientation='h', font=dict(size=14, color='black')),
        paper_bgcolor='white',
        width=650,
        margin=dict(l=50, r=50, t=0, b=0, pad=15),
    )

    fig = go.Figure(data=traces, layout=layout)
    
    st.plotly_chart(fig)
    
def plotMatSPGraph():
    dfmat_sp = pd.read_csv(f'{ABS_PATH}/mat_23_sp.csv', names=['Limite', 'Total'])
    
    categories = dfmat_sp['Limite'].values
    group1 = dfmat_sp['Total'].values
    
    trace1 = go.Bar(
        x=categories, 
        y=group1, 
        width=0.3, 
        marker=dict(color=COLOR_PALETTE['blue']),
        text=[f'{group1[i]}' for i in range(len(categories))],
        textfont=dict(color='black'),
        textposition='outside',
    )

    layout = go.Layout(
        xaxis=dict(showgrid=False, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0, 13000], tickfont=dict(color='black')),
        plot_bgcolor='white',  
        paper_bgcolor='white',
        width=1681
    )

    fig = go.Figure(data=[trace1], layout=layout)

    st.plotly_chart(fig)

def plotMatEmGraph():
    dfmat_em = pd.read_csv(f'{ABS_PATH}/mat_23_embu.csv', names=['Limite', 'Total'])
    
    categories = dfmat_em['Limite'].values
    group1 = dfmat_em['Total'].values
    
    trace1 = go.Bar(
        x=categories, 
        y=group1, 
        width=0.3, 
        marker=dict(color=COLOR_PALETTE['yellow']),
        text=[f'{group1[i]}' for i in range(len(categories))],
        textfont=dict(color='black'),
        textposition='outside',
    )

    layout = go.Layout(
        xaxis=dict(showgrid=False, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0, 30], tickfont=dict(color='black')),
        plot_bgcolor='white',  
        paper_bgcolor='white',
        width=1681
    )

    fig = go.Figure(data=[trace1], layout=layout)

    st.plotly_chart(fig)


def plotMatBRGraph():
    dfmat_em = pd.read_csv(f'{ABS_PATH}/mat_23_br.csv', names=['Limite', 'Total'])
    
    categories = dfmat_em['Limite'].values
    group1 = dfmat_em['Total'].values
    
    trace1 = go.Bar(
        x=categories, 
        y=group1, 
        width=0.3, 
        marker=dict(color=COLOR_PALETTE['blue']),
        text=[f'{group1[i]}' for i in range(len(categories))],
        textfont=dict(color='black'),
        textposition='outside',
    )

    layout = go.Layout(
        xaxis=dict(showgrid=False, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, showticklabels=False, range=[0, 13000], tickfont=dict(color='black')),
        plot_bgcolor='white',  
        paper_bgcolor='white',
        width=1681
    )

    fig = go.Figure(data=[trace1], layout=layout)

    st.plotly_chart(fig)
