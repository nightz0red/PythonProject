import streamlit as st
from rich.jupyter import display

from Pages import Home, Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image

image = Image.open("img/icons8-berserk-48.png")
import pandas as pd
import numpy as np

st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)
pages = ["Home", "Project1", "Project2", "Project3"]
styles = {
    "nav": {
        "background-color": "#1a1a1a",
        "display": "flex",
        "justify-content": "center",

    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size": "15px",
        "top": "4px",
        "width": "100px",
        "height": "40px",

    },
    "span": {
        "border-radius": "0.5rem",
        "color": "#ffffff",
        "font-size": "14px",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "#ff0000",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.2)",
    }
}

page = navbar(pages, styles=styles)

if page == "Home":
    Home.Home().app()
elif page == "Project1":
    Project1.Project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    Home.Home().app()