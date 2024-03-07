import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from src.utils.format_helpers import *
from src.utils.colors import *

ABS_PATH = './src/assets/data'

def plot_educational_expenses_graph():
    df = pd.read_csv(f"{ABS_PATH}/pib_educational_expenses.csv")
    
    x_values = df.set_index('Ano').T.index
    y1_values = df.set_index('Ano').T['Brasil'].apply(replace_comma_with_dot).values
    y2_values = df.set_index('Ano').T['OCDE'].apply(replace_comma_with_dot).values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y1_values, 
            mode='lines+markers', 
            name='Brasil', 
            line_color=COLOR_PALETTE["blue"], 
            line_width=4, 
            marker=dict(size=8)
        )
    )

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y2_values, 
            mode='lines+markers', 
            name='OCDE', 
            line_color=COLOR_PALETTE["yellow"], 
            line_width=4, 
            marker=dict(size=8)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[2000, 2009], 
            y=[5.28, 5.28], 
            mode='lines',
            showlegend=False,
            line=dict(color=COLOR_PALETTE["dark"], width=0.4)
        ),
    )
    
    fig.add_trace(
        go.Scatter(
            x=[2009, 2009], 
            y=[0, 5.28], 
            mode='lines',
            showlegend=False,
            line=dict(color=COLOR_PALETTE["dark"], width=0.4)
        ),
    )
    
    fig.add_trace(
        go.Scatter(
            x=[2006, 2006],
            y=[6.32, 0],
            mode='lines',
            showlegend=False,
            line=dict(color=COLOR_PALETTE["dark"], width=0.4)
        )
    )
    
    fig.add_trace(
        go.Scatter(
            x=[2006, 2020],
            y=[6.32, 6.32],
            mode='lines',
            showlegend=False,
            line=dict(color=COLOR_PALETTE["dark"], width=0.4)
        )
    )


    fig.add_annotation(x=2002, y=7.32, text="Plano Nacional de Educação (PNE)", showarrow=False, font=dict(color=COLOR_PALETTE["dark"], size=12))
    fig.add_annotation(x=2002, y=6.92, text="Ampliação do investimento público em educação", showarrow=False, font=dict(color=COLOR_PALETTE["dark"], size=12))

    fig.add_annotation(x=2016, y=7.32, text="Fundo de Manutenção e Desenvolvimento", showarrow=False, font=dict(color=COLOR_PALETTE["dark"], size=12))
    fig.add_annotation(x=2016, y=6.92, text="da Educação Básica (FUNDEB)", showarrow=False, font=dict(color=COLOR_PALETTE["dark"], size=12))

    fig.update_layout(
        title='Gastos com educação (% PIB)',
        title_font=dict(color='black'),
        xaxis_title='',
        yaxis_title='',
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickmode='linear', tickfont=dict(color='black'), range=[1999.5, 2020.5]),
        yaxis=dict(showgrid=False, tickmode='linear', tickvals=[0, 5, 10], tickfont=dict(color='black')),
        title_x=0.45,
        legend=dict(x=0.45, y=-0.2, orientation='h', font=dict(color='black')),
        width=1300,
        paper_bgcolor='white'
    )
    
    st.plotly_chart(fig, config= {'displayModeBar': False})
    

def plot_poverty_rate_graph():
    df = pd.read_csv(f"{ABS_PATH}/poverty_rate.csv")
    x_values = df.set_index('Indicator Name').T.index
    y1_values = df.set_index('Indicator Name').T['Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)'].apply(replace_comma_with_dot).values
    y2_values = df.set_index('Indicator Name').T['Poverty headcount ratio at $6.85 a day (2017 PPP) (% of population)'].apply(replace_comma_with_dot).values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y1_values, 
            mode='lines', 
            name='Indice de pobreza a U$2.15 por dia (2017) (% da população)', 
            line_color=COLOR_PALETTE["blue"], 
            line_width=4
        )
    )

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y2_values, 
            mode='lines', 
            name='Indice de pobreza a U$6.85 por dia (2017) (% da população)', 
            line_color=COLOR_PALETTE["yellow"], 
            line_width=4
        )
    )

    fig.update_layout(
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickmode='linear', tickvals=[1981, 2021], tickfont=dict(color='black'), tickangle=-45),
        yaxis=dict(showgrid=False, tickvals=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], tickfont=dict(color='black'), range=[0, 85]),
        title_x=0.5,
        legend=dict(x=0.2, y=-0.2, orientation='h', font=dict(color='black')),
        font=dict(color='black'),
        paper_bgcolor='white',
        width=650
    )
    
    st.plotly_chart(fig)
    

def plot_life_expectation_graph():
    df = pd.read_csv(f"{ABS_PATH}/life_expectation.csv")
    
    x_values = df.set_index('Ano').T.index
    y1_values = df.set_index('Ano').T['Expectativa'].apply(put_missing_commas).dropna().apply(replace_comma_with_dot).values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y1_values, 
            mode='lines', 
            name='Expectativa de vida', 
            line_color=COLOR_PALETTE["yellow"], 
            line_width=4
        )
    )

    fig.update_layout(
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickmode='linear', tickvals=[1981, 2021], tickangle=-45, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, tickvals=[50, 55, 60, 65, 70, 75, 80], range=[50, 85], tickfont=dict(color='black')),
        title_x=0.5,
        legend=dict(x=0.4, y=-0.2, orientation='h'),
        width=650,
        paper_bgcolor='white'
    )
    
    st.plotly_chart(fig)
    

def plot_murder_rate_graph():
    df = pd.read_csv(f"{ABS_PATH}/murderS_by_100k.csv")

    x_values = df.set_index('Ano').T.index
    y1_values = df.set_index('Ano').T['Homicídios (por 100 mil pessoas)'].apply(replace_comma_with_dot).values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y1_values, 
            mode='lines', 
            name='Homicídios (por 100 mil pessoas)', 
            line_color=COLOR_PALETTE["blue"], 
            line_width=4
        )
    )

    fig.update_layout(
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickmode='linear', tickvals=[1990, 2020], tickangle=-35, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, tickvals=[0, 5, 10, 15, 20, 25, 30, 35], range=[0, 40], tickfont=dict(color='black')),
        title_x=0.5,
        legend=dict(x=0.4, y=-0.2, orientation='h'),
        paper_bgcolor='white',
        width=650
    )
    
    st.plotly_chart(fig, config= {'displayModeBar': False})
    
def plot_salaries_graph():
    sll = pd.read_csv(f"{ABS_PATH}/salaries_t.csv")

    x_values = sll.set_index('Ano').T.index
    y1_values = sll.set_index('Ano').T['Embu-Guaçu'].values
    y2_values = sll.set_index('Ano').T['Brasil'].values
    y3_values = sll.set_index('Ano').T['São Paulo'].values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y1_values, 
            mode='lines', 
            name='Embu-Guaçu', 
            line_color=COLOR_PALETTE["yellow"], 
            line_width=4
        )
    )

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y2_values, 
            mode='lines', 
            name='Brasil', 
            line_color=COLOR_PALETTE["blue"], 
            line_width=4
        )
    )

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y3_values, 
            mode='lines', 
            name='São Paulo', 
            line_color=COLOR_PALETTE["light_blue"], 
            line_width=4
        )
    )


    fig.update_layout(
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickmode='linear', automargin=True, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, tickformat=".3f", range=[1, 5], tickvals=[1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], tickfont=dict(color='black')),
        legend=dict(x=0.25, y=-0.2, orientation='h', font=dict(color='black')),
        margin=dict(l=50, r=50, t=5, b=0, pad=15),
        paper_bgcolor='white',
        width=650
    )
    
    st.plotly_chart(fig, config= {'displayModeBar': False})
    
def plot_age_distortion_graph():
    dfad = pd.read_csv(f"{ABS_PATH}/age_distortion.csv")

    x_values = dfad.set_index('Ano').T.index
    y1_values = dfad.set_index('Ano').T['Embu-Guaçu'].apply(replace_percentage).values
    y2_values = dfad.set_index('Ano').T['Brasil'].apply(replace_percentage).values
    y3_values = dfad.set_index('Ano').T['São Paulo'].apply(replace_percentage).values

    fig = go.Figure()

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y1_values, 
            mode='lines', 
            name='Embu-Guaçu', 
            line_color=COLOR_PALETTE["yellow"], 
            line_width=4
        )
    )

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y2_values, 
            mode='lines', 
            name='Brasil', 
            line_color=COLOR_PALETTE["blue"], 
            line_width=4
        )
    )

    fig.add_trace(go.Scatter(
            x=x_values, 
            y=y3_values, 
            mode='lines', 
            name='São Paulo', 
            line_color=COLOR_PALETTE["light_blue"], 
            line_width=4
        )
    )


    fig.update_layout(
        title={
            'text':'Homens têm maior defasagem idade-série, especialmente no ensino médio',
            'font': dict(
                color='#333',
                size=12
            )
        },
        plot_bgcolor='white',
        xaxis=dict(showgrid=False, tickmode='linear', automargin=True, tickfont=dict(color='black')),
        yaxis=dict(showgrid=False, tickformat=".2f", ticksuffix="%", range=[0, 16], tickfont=dict(color='black')),
        title_x=0.2,
        legend=dict(x=0.25, y=-0.2, orientation='h', font=dict(color='black')),
        margin=dict(l=0, r=50, t=50, b=0, pad=15),
        paper_bgcolor='white',
        font=dict(color='black'),
        width=650
    )
    
    st.plotly_chart(fig)