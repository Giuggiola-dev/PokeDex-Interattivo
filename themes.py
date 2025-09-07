#Definizione di una serie di palette di colori per Altair.

def my_custom_theme():  #Palette per i colori dei Tipi Pokémon
        return {
            "config": {
                "view": {"continuousWidth": 400, "continuousHeight": 300},
                "mark": {"color": "steelblue"},
                "axis": {
                    "labelFontSize": 12,
                    "titleFontSize": 14,
                    "labelColor": "gray",
                    "titleColor": "black"
                },
                "range": {
                    "category": ["#94A135","#4E403F","#4C5FA8","#EFBE31","#BA7FB5","#EF8733","#D4392F","#8FB7E4","#6B426E","#5D9C3C","#7F451A","#78CBEF","#A1A1A1","#6D4A97","#DC4C79","#ADA984","#73A2B9","#4B79BB"]}
            }}

def my_first_theme():   #Palette per i colori dei Tipi Pokémon ESCLUSIVAMENTE per la prima Generazione (niente tipi buio!)
    return {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300},
            "mark": {"color": "steelblue"},
            "axis": {
                "labelFontSize": 12,
                "titleFontSize": 14,
                "labelColor": "gray",
                "titleColor": "black"
            },
            "range": {"category": ["#94A135","#4C5FA8","#EFBE31","#BA7FB5","#EF8733","#D4392F","#8FB7E4","#6B426E","#5D9C3C","#7F451A","#78CBEF","#A1A1A1","#6D4A97","#DC4C79","#ADA984","#73A2B9","#4B79BB"] }
        }}

def my_strong_theme():  #Palette per il grafico a torta sulle resistenze 
    return {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300},
            "mark": {"color": "steelblue"},
            "axis": {
                "labelFontSize": 12,
                "titleFontSize": 14,
                "labelColor": "gray",
                "titleColor": "black" },
            "range": {"category": [ "#EFBE31", "#5D9C3C"]}
        }}

def my_weak_theme():  #Palette per il grafico a torta sulle debolezze 
    return {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300},
            "mark": {"color": "steelblue"},
            "axis": {
                "labelFontSize": 12,
                "titleFontSize": 14,
                "labelColor": "gray",
                "titleColor": "black"},
            "range": {"category": [ "#EFBE31", "#D4392F"]}
        }}

def my_category_theme():  #Palette generale per i grafici
    return {
        "config": {
            "view": {"continuousWidth": 400, "continuousHeight": 300},
            "mark": {"color": "steelblue"},
            "axis": {
                "labelFontSize": 12,
                "titleFontSize": 14,
                "labelColor": "gray",
                "titleColor": "black"},
            "range": {"category": [ "#EFBE31", "#6D4A97"] }
        }}