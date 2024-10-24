from dash import Dash, dcc, html, Input, Output, callback
import numpy as np


def create_qubit_sliders(id=''):
    slider_P_0 = dcc.Slider(min=0.0,
                            max=1.0,
                            value=0.0,
                            id=f'{id}_P_0_slider')
    slider_theta_0 = dcc.Slider(min=-180.0,
                                max=180.0,
                                value=0.0,
                                id=f'{id}_theta_0_slider')
    slider_theta_1 = dcc.Slider(min=-180.0,
                                max=180.0,
                                value=0.0,
                                id=f'{id}_theta_1_slider')
    return slider_P_0, slider_theta_0, slider_theta_1


app = Dash(__name__)

P_0_slider, theta_0_slider, theta_1_slider = create_qubit_sliders(id='dummy')

app.layout = html.Div([
    html.H3(""),
    html.H4("P_0"),
    P_0_slider,
    html.H4("theta_0 (deg)"),
    theta_0_slider,
    html.Div(id='0_output'),
    html.Br(),
    html.H4("P_1"),
    html.Div(id='P_1_output'),
    html.H4("theta_1 (deg)"),
    theta_1_slider,
    html.Div(id='1_output'),
])


@callback(
    Output(component_id='P_1_output', component_property='children'),
    Input(component_id='dummy_P_0_slider', component_property='value')
)
def update_p_1(p_0):
    return f'P_1: {round(1-p_0,2)}'


@callback(
    Output(component_id='0_output', component_property='children'),
    Input(component_id='dummy_P_0_slider', component_property='value'),
    Input(component_id='dummy_theta_0_slider', component_property='value')
)
def update_0(p_0,theta_0):
    mod_a = np.sqrt(p_0)
    re_0 = mod_a * np.cos(theta_0)
    im_0 = mod_a * np.sin(theta_0)
    return f'|0> = {round(re_0,2)} + {round(im_0,2)}i'


@callback(
    Output(component_id='1_output', component_property='children'),
    Input(component_id='dummy_P_0_slider', component_property='value'),
    Input(component_id='dummy_theta_1_slider', component_property='value')
)
def update_1(p_0,theta_1):
    mod_a = np.sqrt(1-p_0)
    re_1 = mod_a * np.cos(theta_1)
    im_1 = mod_a * np.sin(theta_1)
    return f'|1> = {round(re_1,2)} + {round(im_1,2)}i'


if __name__ == '__main__':
    app.run(debug=True)
