# Run this app with `python dashboards/app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# open a new terminal window (Ctrl+Shift+` in VS Code.)

from dash import Dash, html, dcc, Input, Output
from datetime import date
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np


external_stylesheets = [dbc.themes.SKETCHY]
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "CSE314 HW2"

#import datasets from Ploty's Github Page
df_ag = pd.read_html("https://github.com/plotly/datasets/blob/master/2011_us_ag_exports.csv")[0]
df_apple = pd.read_html("https://github.com/plotly/datasets/blob/master/2014_apple_stock.csv")[0]
df_airports = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv")
df_flight_paths = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv")


app.layout = html.Div([

    html.Div(html.H2("CSE314 Homework2: Python Dashboards"), style = {"display":"inline-block","margin-left":"15px","margin-top":"15px"}),

    dbc.Tabs([

        dbc.Tab(label="2011 Agricultral Exports", children=[
            html.Div([

                html.Div([
                    dcc.Graph(
                        id="ag_exports",
                        style = {"margin-top":"20px"}
                    )
                ]),
                
                html.Div([
                     "Select agricultural exports catagory : ",
                     dcc.Dropdown(
                        ["total exports","beef","pork", "poultry","dairy","fruits fresh","fruits proc","total fruits",
                        "veggies fresh","veggies proc","total veggies","corn","wheat","cotton"], 
                        "total exports",
                        id="ag_type",
                        clearable=False
                    )
                ], style = {"width": "20%","margin":"auto","text-align":"center","min-width":"220px"}
                ),

                html.Div([
                    dcc.Checklist(
                        df_ag["state"].unique(),
                        ["Arizona","California","Maryland","Missouri","Ohio"], 
                        id = "states",
                        inputStyle = {"margin-left": "15px","margin-bottom": "12px","margin-right": "20px"},
                        labelStyle = {"display":"inline-block","margin-top": "10px"}
                    )
                ], style = {"margin-top":"20px"}
                )

            ], style = {"width":"80%","margin":"auto"}
            )
        ]),

        dbc.Tab(label="2014 Apple Stock", children=[

            dcc.Graph(
                id = "APPL",
                style = {"width": "80%","margin":"auto","margin-top":"20px"}
            ),

            html.Div([
                dcc.DatePickerRange(
                    id="my-date-picker-range",
                    min_date_allowed=date(2014, 1, 2),
                    max_date_allowed=date(2014, 12, 12),
                    initial_visible_month=date(2014, 1, 2),
                    start_date = date(2014, 1, 2),
                    end_date = date(2014, 12, 12),
                    style = {"background-color":"black"}
                )
            ], style = {"width": "100%", "display": "flex", "align-items": "center", "justify-content": "center","margin-top":"50px"},
            ),
    
            html.Div(id = "output-container-date-picker-range")
        ]),

        dbc.Tab(label="Feb. 2011 AA Flights", children = [
           
            dcc.Graph(
                id = "flight_map"
            ),

            html.Div([

                html.Div([
                     "Select your filter type : ",
                     dcc.Dropdown(
                        ["All Routes","By Hubs","By Departure Airport", "By Arrival Airport"], 
                        ["All Routes"],
                        id ="filter_choice",
                    )
                ], style = {"width": "20%","margin":"auto","text-align":"center","min-width":"220px"}
                ),

                html.Div([
                    dcc.Checklist(
                        id = "airport_check_list",
                        inputStyle = {"margin-left": "15px","margin-bottom": "12px","margin-right": "20px"},
                        labelStyle = {"display":"inline-block","margin-top": "10px"}
                    )
                ], style = {"width": "80%", "display": "flex", "margin-top":"20px","align-items": "center","justify-content": "center"}
                )

            ],style = {"width": "80%", "display": "flex","flex-direction":"column","align-items": "center", "justify-content": "center","margin":"auto"},
            )
        ])
    ])
], className ="tab-content")

@app.callback(Output("ag_exports","figure"),Input("states","value"),Input("ag_type","value"))
def update_ag_export_fig(states,ag_type):
    filtered_df = df_ag[df_ag["state"].isin(states)]
    fig = px.ecdf(filtered_df, x = "state", y = ag_type,template = "simple_white")
    title_string = "Agricultral Export of " + ag_type + " from States in 2011 (eCDF)"
    fig.update_layout(
        title = title_string,
        title_x = 0.5,
        xaxis_title = "States",
        showlegend = False,
        font = dict(
            size = 18,
            family = "Cabin Sketch"
        )
    )
    return fig


@app.callback(
    Output("airport_check_list","options"),
    Output("airport_check_list","value"),
    Input("filter_choice","value")
)
def generate_checklist_from_filter(filter_choice):
    if filter_choice == "By Departure Airport":
        checkboxes = [{"label": i, "value": i} for i in df_flight_paths["airport1"].unique()]
        default_box = ["DFW"]

    elif filter_choice == "By Arrival Airport":
        checkboxes = [{"label": i, "value": i} for i in df_flight_paths["airport2"].unique()]
        default_box = ["ABQ"]

    elif filter_choice == "By Hubs":
        hub = {"ORD":"O'Hare","DFW":"Dallas/Fort Worth","LAX":"Los Angeles","MIA":"Miami",
        "JFK":"New York–JFK","LGA":"New York–LaGuardia","PHL":"Philadelphia","DCA":"Washington–Reagan"}
        checkboxes = [{"label": hub[i], "value": i} for i in hub]
        default_box = ["ORD","DFW","LAX","MIA","JFK","LGA","PHL","DCA"]

    else:
        checkboxes = []
        default_box = []

    return checkboxes,default_box


@app.callback(
    Output("flight_map","figure"),
    Input("filter_choice","value"),
    Input("airport_check_list","value")
)
def update_flight_map(filter_type, airport_choice):
    if filter_type == "By Departure Airport":
        df_flight_paths_filtered = df_flight_paths.where(df_flight_paths["airport1"].isin(airport_choice))

    elif filter_type == "By Arrival Airport":
        df_flight_paths_filtered = df_flight_paths.where(df_flight_paths["airport2"].isin(airport_choice))

    elif filter_type == "By Hubs":
        df_flight_paths_filtered = df_flight_paths.where(df_flight_paths["airport2"].isin(airport_choice)|df_flight_paths["airport1"].isin(airport_choice))

    else:
        df_flight_paths_filtered = df_flight_paths

    # The following codes to turn flight path dataset into lines on map is borrowed from the Plotly Graphing Libraries
    # https://plotly.com/python/lines-on-maps/

    fig = go.Figure()

    lons = []
    lats = []
    lons = np.empty(3 * len(df_flight_paths_filtered))
    lons[::3] = df_flight_paths_filtered["start_lon"]
    lons[1::3] = df_flight_paths_filtered["end_lon"]
    lons[2::3] = None
    lats = np.empty(3 * len(df_flight_paths_filtered))
    lats[::3] = df_flight_paths_filtered["start_lat"]
    lats[1::3] = df_flight_paths_filtered["end_lat"]
    lats[2::3] = None

    fig.add_trace(
        go.Scattergeo(
            locationmode = "USA-states",
            lon = lons,
            lat = lats,
            mode = "lines",
            line = dict(width = 1,color = "red"),
            opacity = 0.5
        )
    )
    fig.add_trace(go.Scattergeo(
        locationmode = "USA-states",
        lon = df_airports["long"],
        lat = df_airports["lat"],
        hoverinfo = "text",
        text = df_airports["airport"],
        mode = "markers",
        marker = dict(
            size = 2,
            color = "rgb(255, 0, 0)",
            line = dict(
                width = 3,
                color = "rgba(68, 68, 68, 0)"
            )
        )))
    fig.update_layout(
        title_text = "Feb. 2011 American Airline flight paths",
        title_x=0.5,
        showlegend = False,
        geo = go.layout.Geo(
            scope = "north america",
            projection_type = "azimuthal equal area",
            showland = True,
            landcolor = "rgb(243, 243, 243)",
            countrycolor = "rgb(204, 204, 204)",
        ),
        height = 700,
        font=dict(
            size=18,
            family="Cabin Sketch"
        )
    )
    return fig

@app.callback(
    Output("APPL", "figure"),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date")
)
def update_AAPL_fig(start_date,end_date):
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime("%Y-%m-%d")

    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime("%Y-%m-%d")

    ranged_df = df_apple.where((df_apple["AAPL_x"]>=start_date_string)&(df_apple["AAPL_x"]<=end_date_string))

    fig = px.line(ranged_df, x="AAPL_x", y="AAPL_y",template = "simple_white")
    fig.update_layout(
        title="Apple Stock Price Versus Days in 2014",
        title_x=0.5,
        xaxis_title="Dates",
        yaxis_title="Stock Price ($)",
        font=dict(
            size=18,
            family="Cabin Sketch"
        )
    )
    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
