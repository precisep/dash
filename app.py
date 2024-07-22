import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

from source.processing import (
    mobile_data_preprocessing,
    age_distribution_graph,
    financial_service_by_age_graph,
    gender_vs_financial_services,
    marital_status_vs_financial_services,
    personal_land_ownership_vs_financial_services,
    main_items_sold_vs_financial_services,
    employment_type_vs_financial_services,
    main_services_provided_vs_financial_services,
    land_ownership_vs_financial_services,
    sources_of_income_vs_financial_services,
    financial_service_classification_map  
)

DATA = mobile_data_preprocessing()

MOBILE_CLASSIFICATION = ['All'] + DATA['financial_service_classification'].unique().tolist()

app = dash.Dash(__name__, external_stylesheets=[
    'https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css',
    './assets/styles.css'
])

server = app.server

app.layout = html.Div([
    html.Div(className='header', children=[
        html.H1('Mobile Money Usage In Tanzania', className='mb-0')
    ]),

    html.Div(className='container my-4', children=[
        html.Div(className='introduction mb-4', children=[
            html.H4('Welcome! 👋🏾'),
            html.P('Created by Thabang P Mokoena'),
            html.P('This dashboard explores the relationship between mobile financial service usage and demographic factors for the citizens in Tanzania.')
        ]),

        html.Div(className='dropdown-container', children=[
            html.Label('Select a financial service classification', className='dropdown-label'),
            dcc.Dropdown(
                id='financial_service_classification_dropdown',
                options=[{'label': mobile_class, 'value': mobile_class} for mobile_class in MOBILE_CLASSIFICATION],
                value='All',
                clearable=False,
                className='dropdown mb-4',
                placeholder='Select a financial service classification',
                style={'width': '50%'},
            )
        ]),

        html.Div(className='graph-container', children=[
            dcc.Graph(id='age-financial-services-graph', className='graph'),
            dcc.Graph(id='financial-service-by-age-graph', className='graph'),
            dcc.Graph(id='gender-vs-financial-services-graph', className='graph'),
            dcc.Graph(id='marital_status_vs_financial_services', className='graph'),
            dcc.Graph(id='personal-land-ownership-vs-financial-services', className='graph'),
            dcc.Graph(id='main-items-sold-vs-financial-services', className='graph'),
            dcc.Graph(id='employment-type-vs-financial-services', className='graph'),
            dcc.Graph(id='main-services-provided-vs-financial-services', className='graph'),
            dcc.Graph(id='land-ownership-vs-financial-services', className='graph'),
            dcc.Graph(id='sources-of-income-vs-financial-services', className='graph'),
        ]),

        html.Div(className='map-container', children=[
            dcc.Graph(id='map', className='map')
        ])
    ]),

    html.Div(className='footer', children=[
        html.P('© 2024 Precise. All rights reserved.')
    ])
])

@app.callback(
    [
        Output('age-financial-services-graph', 'figure'),
        Output('financial-service-by-age-graph', 'figure'),
        Output('gender-vs-financial-services-graph', 'figure'),
        Output('marital_status_vs_financial_services', 'figure'),
        Output('personal-land-ownership-vs-financial-services', 'figure'),
        Output('main-items-sold-vs-financial-services', 'figure'),
        Output('employment-type-vs-financial-services', 'figure'),
        Output('main-services-provided-vs-financial-services', 'figure'),
        Output('land-ownership-vs-financial-services', 'figure'),
        Output('sources-of-income-vs-financial-services', 'figure'),
        Output('map', 'figure')
    ],
    Input('financial_service_classification_dropdown', 'value')
)
def update_graphs(selected_classification):
    try:
        if selected_classification == 'All':
            filtered_data = DATA
        else:
            filtered_data = DATA[DATA['financial_service_classification'] == selected_classification]

        fig1 = age_distribution_graph(filtered_data)
        fig2 = financial_service_by_age_graph(selected_classification)
        fig3 = gender_vs_financial_services(selected_classification)
        fig4 = marital_status_vs_financial_services(selected_classification)
        fig5 = personal_land_ownership_vs_financial_services(selected_classification)
        fig6 = main_items_sold_vs_financial_services(selected_classification)
        fig7 = employment_type_vs_financial_services(selected_classification)
        fig8 = main_services_provided_vs_financial_services(selected_classification)
        fig9 = land_ownership_vs_financial_services(selected_classification)
        fig10 = sources_of_income_vs_financial_services(selected_classification)

        map_fig = financial_service_classification_map(filtered_data)

        return fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, map_fig

    except Exception as e:
        print(f"Error in update_graphs callback: {str(e)}")
        return {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

if __name__ == '__main__':
    app.run_server(debug=True)
