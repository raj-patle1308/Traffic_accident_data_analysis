from pydoc import doc
from dash import dcc
import dash
from dash import html
from components import Header
import components
import pandas as pd



from clustermap_severity import create_cluster_map
from fun_style import SIDEBAR_STYLE

# sidebar = html.Div(
#     [
#         html.Div(
#             children=[
#                 html.Div(
#                     html.Img(src="/assets/dsdsdd.png", height=55, style={"width": "80%", "margin": "auto", "display": "block"})
#                 )
#             ],
#             style={"display": "flex", "flex-direction": "column", "justify-content": "center", "align-items": "center"}
#         ),
#         html.Div(
#             children=[
#                 html.A(
#                     html.Img(src="/assets/admin.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "align-self": "flex-end"}),
#                     href="http://127.0.0.1:8050/form",  # Set the href attribute to the desired URL
#                 )
#             ],
#             style={"display": "flex", "flex-direction": "column", "justify-content": "center", "align-items": "center"}
#         ),
#         html.Div(
#             children=[
#                 html.A(
#                     html.Img(src="/assets/admin.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "align-self": "flex-end"}),
#                     href="https://lookerstudio.google.com/s/pdbCPDa2Hmg",  # Set the href attribute to the desired URL
#                 )
#             ],
#             style={"display": "flex", "flex-direction": "column", "justify-content": "center", "align-items": "center"}
#         ),
#         html.Div(
#             children=[
#                 html.A(
#                     html.Img(src="/assets/admin.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "align-self": "flex-end"}),
#                     href="http://127.0.0.1:8050/dashB1",  # Set the href attribute to the desired URL
#                 )
#             ],
#             style={"display": "flex", "flex-direction": "column", "justify-content": "center", "align-items": "center"}
#         )
#     ],
#     style=SIDEBAR_STYLE,
# )
sidebar = html.Div(
    [
        html.Div(
            children=[
                html.Div(
                    html.Img(src="/assets/dsdsdd.png", height=55, style={"width": "80%", "display": "block"})
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    html.Img(src="/assets/pridict.png", height=45, style={"width": "60%",  "display": "block", "position": "absolute", "bottom": "180px"}),
                    href="http://127.0.0.1:8050/pridict",  # Set the href attribute to the desired URL
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    html.Img(src="/assets/dashboard.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "100px" }),
                    href="https://lookerstudio.google.com/s/pdbCPDa2Hmg",  # Set the href attribute to the desired URL
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    # Set the href attribute to the desired URL
                    html.Img(src="/assets/upload.jpg", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "20px"}),
                    href="http://127.0.0.1:8050/upload", 
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        ),
        html.Div(
            children=[
                html.A(
                    # Set the href attribute to the desired URL
                    html.Img(src="/assets/admin.png", height=45, style={"width": "60%", "margin": "auto", "display": "block", "position": "absolute", "bottom": "260px"}),
                    href="http://127.0.0.1:8050/", 
                )
            ],
            style={"display": "flex", "flex-direction": "column", "justify-content": "flex-end", "align-items": "center"}
        )
    ],
    style=SIDEBAR_STYLE,
)






dash.register_page(__name__, path='/upload')
df = pd.read_excel('testdata.xlsx')

# prompt: function to give a dataframe which has the district give in passing variable 


layout = html.Div([
    Header.header(df),sidebar,
    dcc.Upload(
    id='upload-data',
    children=html.Div(['Drop or ', html.A('Select Files')]),
    style={
        'width': '200px',
        'height': '50px',
        'lineHeight': '50px',
        'borderWidth': '1px',
        'borderStyle': 'dashed',
        'borderRadius': '5px',
        'textAlign': 'center',
        'margin': 'auto',  # Aligning to the center horizontally
        'color': 'black',  # Text color
        'backgroundColor': '#6495ED',  # Blue background color
        'display': 'block',  # Ensure it's a block element for margin auto to work
        'marginTop': '50vh',  # Aligning to the center vertically
        'transform': 'translateY(-50%)',  # Centering vertically
    },
    # Allow multiple files to be uploaded
    multiple=False
),
])
# style={'backgroundColor': '#192444'})\

# layout =  html.Div(
#     [
#     Header.header(df),sidebar,
#     html.Div([
#         html.H2("I am man")]
#     ,style={
#             "position": "fixed",
#             "top": "10px",
#             "left": "10px",
#             "background-color": "white",
#             "padding": "5px",
#             "border": "1px solid black"
#         })
#         ],style={'backgroundColor': '#192444' ,'height':'100vh'})
# #print(centers)