import pandas as pd
import numpy as np
import time
import plotly.express as px
import streamlit as st
import dash_bootstrap_components as dbc
import dash_core_components as dcc

adidas = pd.read_excel("Adidas.xlsx")
adidas.head(5)

