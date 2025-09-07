#Importa le librerie necessarie
import streamlit as st
import polars as pl
import altair as alt
from PIL import Image
import urllib.request
import io
#Importa i temi per altair
from themes import my_custom_theme, my_first_theme, my_category_theme, my_strong_theme, my_weak_theme
#Importa delle funzioni 
from functions import three_digits, img_url_generator, dmg_colour, type_n_check, poke_colour, weakness_list, resist_list


#Crea la cache dei database per velocizzare i calcoli una volta caricata la pagina (in modo da non dover ricominciare da zero a ogni interazione)
@st.cache_data 
def load_data(): 
    data = pl.read_csv("data.csv", separator=";") 
    names = data.select("Name")
    options = names['Name'].to_list() 
    return data, names, options

#Carica i database
data, names, options = load_data()

#Crea la cache delle immagini per la sezione informativa per velocizzare i calcoli una volta caricata la pagina (in modo da non dover ricominciare da zero a ogni interazione)
@st.cache_data 
def load_info_images(): 
    with urllib.request.urlopen("https://archives.bulbagarden.net/media/upload/3/3e/Lets_Go_Pikachu_Eevee_Professor_Oak.png") as response: img_data = response.read()
    professor_oak = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Caterpie", data)) as response: img_data = response.read()
    caterpie = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Metapod", data)) as response: img_data = response.read()
    metapod = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Butterfree", data)) as response: img_data = response.read()
    butterfree = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Charizard", data)) as response: img_data = response.read()
    lizardon = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Mega Charizard X", data)) as response: img_data = response.read()
    lizardonX = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Mega Charizard Y", data)) as response: img_data = response.read()
    lizardonY = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Vulpix", data)) as response: img_data = response.read()
    vulpix = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Alolan Vulpix", data)) as response: img_data = response.read()
    alo_vulpix = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Pikachu", data)) as response: img_data = response.read()
    pikachu = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Bulbasaur", data)) as response: img_data = response.read()
    bulbasaur = Image.open(io.BytesIO(img_data))
    with urllib.request.urlopen(img_url_generator("Squirtle", data)) as response: img_data = response.read()
    reverse_squirtle = Image.open(io.BytesIO(img_data)).transpose(method=Image.FLIP_LEFT_RIGHT)
    with urllib.request.urlopen(img_url_generator("Charmander", data)) as response: img_data = response.read()
    charmander = Image.open(io.BytesIO(img_data))
    type_chart = Image.open(r"PokemonTabTipi.png")
    
    return professor_oak, caterpie, metapod, butterfree, lizardon, lizardonX, lizardonY, vulpix, alo_vulpix, pikachu, bulbasaur, reverse_squirtle, charmander, type_chart

#Carica le immagini per la sezione informazioni
professor_oak, caterpie, metapod, butterfree, lizardon, lizardonX, lizardonY, vulpix, alo_vulpix, pikachu, bulbasaur, reverse_squirtle, charmander, type_chart = load_info_images()

#Registra i temi importati da themes.py
alt.themes.register('my_custom_theme', my_custom_theme)
alt.themes.register('my_first_theme', my_first_theme)
alt.themes.register('my_category_theme', my_category_theme)
alt.themes.register('my_strong_theme', my_strong_theme)
alt.themes.register('my_weak_theme', my_weak_theme)


#Una sezione che si può espandere che spiega in breve cosa sono i Pokémon. 
#Tutti i concetti necessari per comprendere i grafici sono in GRASSETTO
#Utilizza immagini e testo, il tutto è disposto in colonne per avere una presentazione "carina" (si spera)
with st.expander("Che cos'é un Pokémon?",icon="ℹ️"):
    col1, col2, = st.columns([1,5])
    with col1:
        st.image(professor_oak, width=80)
    with col2:
                st.write("**Ciao!**  \n Mi chiamo **OAK**, ma tutti mi conoscono come il **PROFESSORE dei POKÉMON**!  \n Questo mondo è abitato da creature chiamate Pokémon! Per alcuni sono piccoli amici, altri li usano per lottare.  \n In quanto a me... il loro studio è il mio lavoro.  \n Lascia che ti spieghi l'essenziale sui Pokémon!")
    st.write("I Pokémon sono creature straordinarie, ognuno con abilità uniche, personalità e poteri speciali.  \n Ma per prima cosa bisogna catturarli!  \n Ogni Pokémon ha un diverso **Tasso di Cattura**: più alto è il valore più facile sarà da catturare!  \n Alcuni Pokémon estremamente potenti e rari, i cosiddetti **Leggendari**, hanno un tasso di cattura molto basso." )
    st.write("Il tratto distintivo di molti Pokémon è l'**Evoluzione**, cioè la capacità di trasformarsi in forme più forti e potenti!  \n Per esempio, Caterpie si evolve in Metapod, che a sua volta si evolve in Butterfree.  \n Butterfree non si può evolvere ulteriormente, perciò è detto l'**evoluzione finale** della propria linea.")
    col1, col2, col3,col4,col5 = st.columns([1,1,1,1,1])
    with col1:
        st.image(caterpie, width=80)
    with col2:
        st.write("Livello 7")
        st.write("➡️")
    with col3:
        st.image(metapod, width=80)
    with col4:
        st.write("Livello 10")
        st.write("➡️")
    with col5:
        st.image(butterfree, width=80)
    st.write("Alcuni Pokémon sono in grado di 'mega-evolversi'.  \n Le **Mega Evoluzioni** sono una forma temporanea e ancora più potente di alcuni Pokémon!  \n Durante una battaglia, un Pokémon può mega-evolversi se il suo allenatore usa una Megapietra. La Mega Evoluzione dura solo per la battaglia e dà al Pokémon statistiche e abilità migliorate.  \n Per esempio, Charizard può mega-evolversi in Charizard X e Charizard Y!")
    col1, col2, col3,col4,col5 = st.columns([1,1,1,1,1])
    with col1:
        st.image(lizardonX, width=80)
    with col2:
        st.write("Charizardite X")
        st.write("⬅️")
    with col3:
        st.image(lizardon, width=80)
    with col4:
        st.write("Charizardite Y")
        st.write("➡️")
    with col5:
        st.image(lizardonY, width=80)
    st.write("Alcune specie di Pokémon che vivono in regioni specifiche come Alola o Galar si sono adattate all'ambiente particolare di quella regione e hanno sviluppato un aspetto e un comportamento diverso rispetto agli esemplari della stessa specie.  \n Queste **forme regionali** assumono tipi e abilità diverse!  \n Per esempio, Vulpix è normalmente di tipo Fuoco, ma la sua forma di Alola è di tipo Ghiaccio!")
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.write("Vulpix  \n :red-background[Fuoco]")
    with col2:
        st.image(vulpix, width=80)
    with col3:        
        st.image(alo_vulpix, width=80)
    with col4:
        st.write("Vulpix di Alola  \n :blue-background[Ghiaccio]")
    st.write("Che sbadato! Stavo quasi per dimenticarmi di spiegarti cosa sono i **Tipi**!  \n Ogni Pokémon ha uno o due tipi, in base alle proprie caratteristiche. Per esempio...")
    col1, col2,col3,col4 = st.columns([1,2,1,2])
    with col1:
        st.image(pikachu, width=80)
    with col2:
        st.write("Pikachu è di tipo :orange-background[Elettro], in quanto ha abilità basate sull'elettricità.")  
    with col3:
        st.image(bulbasaur, width=80)
    with col4:
        st.write("Bulbasaur, invece, ha due tipi: :green-background[Erba] e :violet-background[Veleno].")
    st.write("Ogni Tipo di Pokémon può essere **efficace** o **debole** contro altri tipi.  \n Ad esempio, un attacco di tipo Acqua è molto efficace contro un Pokémon di tipo Fuoco.  \n Se Squirtle, un Pokèmon di tipo Acqua, usa l'attacco Pistolaqua contro Charmander, un Pokémon di tipo Fuoco, infliggerà il doppio dei danni! Un attacco... **super-efficace**!")
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
    with col1:
        st.write("")
    with col2:
        st.image(reverse_squirtle, width=80)
    with col3:
        st.write("Pistolaqua")
        st.write("➡️**x2**➡️")
    with col4:
        st.image(charmander, width=80)
    with col5:
        st.write("")
    st.write("Ecco una tabella che spiega l'efficacia degli attacchi tra i diversi tipi!")
    st.image(type_chart, width=500)
    st.write("Per sapere quale moltiplicatore hanno i Pokémon con doppio tipo, basta moltiplicare i valori. Per esempio un Pokémon di tipo :orange-background[Terra] :red-background[Roccia] subirà il quadruplo dei danni da un attacco di tipo Acqua (x2 da Terra, x2 da Roccia).  \n E questo è quanto! Spero di esserti stato di aiuto!  \n Adesso dai un'occhiata al **PokéDex**, il database di mia invenzione che contiene le informazioni su tutti i Pokémon. Buon proseguimento!")


#Qui inizia l'applicazione streamlit vera e propria

#Questa prima sezione si concentra su un solo Pokémon alla volta (una riga del dataframe alla volta)
with st.container():
    st.header("PokéDex")        
    st.write("Seleziona un Pokémon (puoi anche digitare il nome):")
    # Inizializza la variabile solo se non esiste. Questa variabile serve per rendere interattivi (o meno, se si è agli estremi della lista) i pulsanti PREC. E SUCC.
    if 'pok_index' not in st.session_state:
        st.session_state.pok_index = 0

    #Se si clicca uno dei pulsanti PREC. o SUCC., il valore di pok_index si aggiorna di conseguenza
    def onClick(selection_input):
        if selection_input == 'prev':
            st.session_state.pok_index -= 1
        if selection_input == 'next':
            st.session_state.pok_index += 1

    #Se si seleziona un Pokémon dal selectbox, il valore di pok_index si aggiorna di conseguenza
    def onSelect():
        st.session_state.pok_index = st.session_state.pkm_selector

    col1, col2, col3 = st.columns([1, 5, 1])
    with col1:
        #Pulsante per selezionare il Pokémon precedente nel dataset
        st.button("⏮️ Prec.", disabled=(st.session_state.pok_index == 0), on_click=onClick, args=('prev',))
    with col2:
        #Selectbox: 
        pkm_selector = st.selectbox(label="Seleziona un Pokémon (puoi anche digitare il nome):",
            options=range(len(options)),
            label_visibility="collapsed" ,
            format_func=lambda x: options[x],
            index=st.session_state.pok_index,
            key="pkm_selector",
            on_change=onSelect
        )
        #Aggiorna la variabile pok_index quando si cambia la selectbox
        st.session_state.pok_index = pkm_selector
    with col3:
        #Pulsante per selezionare il Pokémon successivo nel dataset
        st.button("Succ. ⏭️", disabled=(st.session_state.pok_index == len(options)-1), on_click=onClick, args=('next',))

    #Il pokémon selezionato corrisponde a una riga del dataframe. Si procede a mostrare un'immagine del pokémon grazie alla funzione image_url_generator e a mostrarne le informazioni
    row=data.row(by_predicate=(pl.col("Name") == options[pkm_selector]), named=True)
    col1, col2, col3 = st.columns([2, 2, 3])
    with col1:
        with urllib.request.urlopen(img_url_generator(options[pkm_selector], data)) as response: img_data = response.read()
        image = Image.open(io.BytesIO(img_data))
        st.write(f"#{three_digits(row['Number'])} **{options[pkm_selector]}**  \n Generazione: {row['Generation']}")
        st.image(image, width=150)
        st.write(type_n_check(1,row)+type_n_check(2,row))
        st.write("**Abilità:**  \n"+''.join(c for c in row["Abilities"] if c not in "[]'"))
    with col2:
        st.write(f"**STATISTICHE**")
        st.write(f" **Punti Salute:** {row['HP']}  \n **Attacco:** {row['Att']}  \n **Difesa:** {row['Def']}  \n **Attacco Speciale:** {row['Spa']}  \n **Difesa speciale:** {row['Spd']}  \n **Velocità:** {row['Spe']} ")
        st.write(f"**Totale:** {row['BST']} ")
        st.write(f"**Altezza:** {row['Height']} m  \n  **Peso:** {row['Weight']} kg  \n **Tasso di cattura:** {row['Catch Rate']}")
    with col3:
        st.write(f"**MOLTIPLICATORE DANNO SUBITO**")
        col1, col2= st.columns([1,1])
        with col1:
            st.write( f":gray-background[Normale]: {dmg_colour(row['Against Normal'])}  \n     :red-background[Fuoco]: {dmg_colour(row['Against Fire'])}  \n     :blue-background[Acqua]: {dmg_colour(row['Against Water'])}  \n     :orange-background[Elettro]: {dmg_colour(row['Against Electric'])}  \n     :green-background[Erba]: {dmg_colour(row['Against Grass'])}  \n     :blue-background[Ghiaccio]: {dmg_colour(row['Against Ice'])}  \n     :red-background[Lotta]: {dmg_colour(row['Against Fighting'])}  \n     :violet-background[Veleno]: {dmg_colour(row['Against Poison'])}  \n     :orange-background[Terra]: {dmg_colour(row['Against Ground'])}")
        with col2:
            st.write( f":blue-background[Volante]: {dmg_colour(row['Against Flying'])}  \n     :violet-background[Psico]: {dmg_colour(row['Against Psychic'])}  \n     :green-background[Coleottero]: {dmg_colour(row['Against Bug'])}  \n     :red-background[Roccia]: {dmg_colour(row['Against Rock'])}  \n     :violet-background[Spettro]: {dmg_colour(row['Against Ghost'])}  \n     :blue-background[Drago]: {dmg_colour(row['Against Dragon'])}  \n     :gray-background[Buio]: {dmg_colour(row['Against Dark'])}  \n     :gray-background[Acciaio]: {dmg_colour(row['Against Steel'])}  \n     :violet-background[Folletto]: {dmg_colour(row['Against Fairy'])}")
    
    st.write("**PERCENTUALE DI DEBOLEZZE E RESISTENZE**")
    #si ottengono due liste di tipi, una per le debolezze e una per le resistenze del pokémon selezionato
    weaknesses=weakness_list(row)
    strength=resist_list(row)
    #si ottiene il numero di Pokémon a cui è debole o resistente grazie al conteggio di unità in un sotto-insieme del dataframe. Il sotto-insieme lo si ottiene controllando se il tipo primario o secondario di un pokémon è nella lista delle debolezze/resistenze
    c1, c2 = 0, 0
    c1 = data.filter(
        pl.col("Type 1").is_in(weaknesses) | pl.col("Type 2").is_in(weaknesses)
    ).height
    c2 = data.filter(
        pl.col("Type 1").is_in(strength) | pl.col("Type 2").is_in(strength)
    ).height
    #si calcola il numero totale di pokémon
    tot=len(options)+1
    #si creano dei dataframe basici con numero di pokémon a cui è debole/resistente e a cui non lo è (serviranno per fare due grafici a torta)
    contatori_eff = pl.DataFrame({"Damage":["Normal","Weaknesses"], "Count":[ tot-c1, c1]})
    contatori_res = pl.DataFrame({"Damage":["Normal","Strengths",], "Count":[tot-c2, c2]})
    #si visualizzano i dataframe sopradefiniti con dei grafici a torta, utilizzando dei colori per trasmettere meglio la categoria di pokémon di cui si parla (debolezze o resistenze)
    col1, col2, col3, col4, col5 = st.columns([1,2,0.5,1,2])
    with col1:
        alt.themes.enable('my_weak_theme')
        Pie_Chart = alt.Chart(contatori_eff).mark_arc(radius=20, radius2=40, cornerRadius=5).encode(    
            alt.Theta("Count:Q", stack=True, sort="descending"),
            alt.Color("Damage", legend=None, sort="ascending"),
            tooltip=alt.value(None)
            ).properties(height=100, width=100)
        text = alt.Chart(contatori_eff).mark_text(
        align='center',
        baseline='middle',
        text=f"{round((100*c1/tot),1)} %",
        fontSize=12,
        color="#D4392F",
        tooltip=""
        )
        Pie_Chart+text
    with col2:
        st.write(f"Il {round((100*c1/tot),1)} % dei Pokémon ha un tipo super-efficace a {options[pkm_selector]}")
    with col3:
        pass #è qui solo per impaginare meglio
    with col4:
        alt.themes.enable('my_strong_theme')
        Pie_Chart = alt.Chart(contatori_res).mark_arc(radius=20, radius2=40, cornerRadius=5).encode(    
            alt.Theta("Count:Q", stack=True, sort="descending"),
            alt.Color("Damage", legend=None, sort="ascending"),
            tooltip=alt.value(None)
            ).properties(height=100, width=100)
        text = alt.Chart(contatori_eff).mark_text(
        align='center',
        baseline='middle',
        text=f"{round((100*c2/tot),1)} %",
        fontSize=12,
        color="#5D9C3C",
        tooltip=""
        )
        Pie_Chart+text
    with col5:
        st.write(f"Il {round((100*c2/tot),1)} % dei Pokémon ha un tipo non molto efficace a {options[pkm_selector]}")
    
    col1, col2= st.columns([2,1])
    with col1:
        st.write(f"**RILEVANZA DI {options[pkm_selector].upper()} NEL CORSO DELLE GENERAZIONI**")
    #questa colonna include un bottone che mostra un popup per spiegare cos'é una Generazione
    with col2:
        #popup
        @st.dialog("Cos'é una Generazione?")
        def show_info():
            st.write("Una 'generazione' può essere considerata come un raggruppamento di Pokémon in gruppi distinti per ordine di introduzione nei videogiochi della serie. Infatti:  \n   \n  *Una delle caratteristiche principali dei videogiochi del franchise Pokémon è il loro raggruppamento in 'generazioni'. Queste rappresentano suddivisioni cronologiche dei titoli [...]. Ogni qualvolta viene pubblicata una coppia di videogiochi della serie principale, che introduce nuovi Pokémon, una nuova regione e una storia e meccaniche di gioco inedite, ciò segna l'inizio di una nuova generazione Pokémon.*  \n Fonte: Wikipedia")
        #bottone
        if st.button("Cos'é una Generazione?",icon="ℹ️"):
            show_info()
    #A seguire c'è un grafico a linee spezzate. Salviamo il totale delle statistiche del pokémon selezionato...
    ref_BST = row['BST']
    #si crea un dataframe che include, per ogni generazione: il numero totale dei pokemon della generazione, il numero dei pokemon con tot statistiche maggiore di quello di riferimento e il rapporto tra questo numero e il totale (percentuale).
    proc_data = ( data.with_columns( pl.col("BST") )
             .group_by("Generation") 
             .agg( pl.count().alias("Total_Gen"), pl.col("BST").filter(pl.col("BST") < ref_BST).count().alias("Less_Than") ) 
             .with_columns( (pl.col("Less_Than") / pl.col("Total_Gen") * 100).alias("Percent") ) 
            ).sort(by="Generation")
    #si disegna il grafico che mostra l'evoluzione di questa percentuale nel tempo.
    col1, col2= st.columns([1,1])
    with col1:
        chart_1 = alt.Chart(proc_data).mark_line(point=True).encode( 
            x=alt.X("Generation:O", title="Generazione", axis=alt.Axis(grid=True, labelAngle=0)), 
            y=alt.Y("Percent:Q", title="Percentile").scale(domain=[0, 100]),
            color=alt.value(poke_colour(1, row)),
            tooltip=[alt.Tooltip("Percent:Q", format=".2")] 
            ).properties( width=300, height=400)
        chart_1
    with col2:
        st.write(f"La rilevanza viene calcolata in termini di **percentile**, una misura statistica che determina la 'posizione' di un'unità nel dataset. L'ordinamento è dato da una funzione punteggio, in questo caso il **Totale delle statistiche**.  \n Per esempio, un Pokémon con percentile pari a 35 ha il Totale delle statistiche superiore al 35% dei Pokémon, ma inferiore al resto.  \n In parole povere, più alto è il valore, più è potente (dunque rilevante) un Pokémon in una determinata Generazione.  \n Il grafico mostra dove {options[pkm_selector]} si trova rispetto ai Pokémon introdotti in quella generazione.")
    #alcune osservazioni
    st.write("Il percentile diminuisce nella Generazione 4 in quanto il numero di Pokémon al terzo stadio evolutivo introdotti è superiore, e diminuisce sensibilmente nella Generazione 6 in quanto sono state introdotte le Mega Evoluzioni, versioni più potenti di Pokémon già esistenti.  \n Queste cose verranno approfondite nella sezione di analisi più in basso.")

    #si  disegna un grafico analogo al precedente, ma confrontando più pokemon
    st.subheader("Confronto della rilevanza tra più Pokémon")
    #si selezionano le unità dal multiselect
    selected_pokemons = st.multiselect(
    "Seleziona i Pokémon da confrontare:",
    options,
    default=["Bulbasaur", "Charmander", "Squirtle"],
    )
    #Creo un dataframe vuoto
    confronti = pl.DataFrame()
    #creo una lista di colori vuota
    color_list=[]
    if selected_pokemons == []: #Nel caso nulla sia selezionato, disegna un grafico vuoto
        empty = alt.Chart(pl.DataFrame({ "Generation": [], "Percent": [], "Name": [] })).mark_line().encode( 
        x=alt.X("Generation:Q", title="Generazione", axis=alt.Axis(grid=True, labelAngle=0, labels=True, format="d")).scale(domain=[0.5, 8.5]), 
        y=alt.Y("Percent:Q", title="Percentuale").scale(domain=[0, 100]),
        ).properties(width=700, height=500)
        empty
    else:
        for name in selected_pokemons: #Altrimenti, riempie il dataframe e la lista
            row=data.row(by_predicate=(pl.col("Name") == name), named=True)
            color_list.append(poke_colour(1, row))
            temp = (data.group_by("Generation")
                .agg(
                    pl.count().alias("TotalGen"),
                    pl.col("BST").filter(pl.col("BST") < row['BST']).count().alias("Less_Than")
                )
                .with_columns(
                    (pl.col("Less_Than") / pl.col("TotalGen") * 100).alias("Percent"),
                    pl.lit(row['Name']).alias("Name")  # Aggiungi una colonna con il BST di riferimento
                )
            )
            confronti = pl.concat([confronti, temp], how="vertical").sort(by=["Generation", "Name"])
        
        #Ordina la lista dei colori in base ai Pokémon (per avere i colori associati corretti)
        indexes = sorted(range(len(selected_pokemons)), key=lambda i: selected_pokemons[i])
        ordered_color_list = [color_list[i] for i in indexes]
        #Dalla lista di colori si crea un tema altair per il grafico
        def confront_theme():
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
                            "category": ordered_color_list}
                    }
                }
        #si attiva la palette
        alt.themes.register('confront_theme', confront_theme)
        alt.themes.enable('confront_theme')
        #Si disegna il grafico multilinea, ognuna con il proprio colore
        chart_multi = alt.Chart(confronti).mark_line(point=True).encode( 
            x=alt.X("Generation:O", title="Generazione", axis=alt.Axis(grid=True, labelAngle=0, labels=True)), 
            y=alt.Y("Percent:Q", title="Percentuale").scale(domain=[0, 100]),
            color=alt.Color("Name:N", legend=None),
            tooltip=[alt.Tooltip("Percent:Q", format=".2")] 
            ).properties( width=700, height=500 )
        #Alla fine di ogni linea, stampa il nome del pokemon corrispondente
        names=alt.Chart(confronti.filter(pl.col("Generation")==8)).mark_text(align='left', dx=5).encode(
            x=alt.X("Generation:O", axis=alt.Axis(labels=False)),
            y="Percent:Q",
            color=alt.Color("Name:N", legend=None),
            text="Name:N"
        )
        chart_multi+names

#Da questa sezione in poi si lavora con tutto il dataframe, manipolando i dati
with st.container():
    st.subheader("Distribuzione dei Tipi per Generazione")
    st.write("Questi grafici hanno lo scopo di studiare le distribuzioni dei diversi Tipi nelle generazioni.  \n Quali tipi sono più frequenti in una specifica Generazione?  \n Quale Generazione ha le distribuzioni meglio bilanciate?")
    selected_gen = st.slider("Seleziona la Generazione da analizzare:", 1,8,1, key=1)
    #Si disegnano dei grafici a torta per la distribuzione dei tipi nelle generazioni
    col1, col2 = st.columns([5, 4])
    with col1:
        st.write(f"**DISTRIBUZIONE IN TUTTE LE GENERAZIONI**") #non si filtrano i dati per generazione: visione globale
        #Alcuni pokémon hanno due tipi: devono figurare in entrambe le percentuali. Per questo conto separatamente le colonne Type1 e Type2, per poi unirne i conteggi in una colonna Type
        type1 = data.select(pl.col("Type 1")).rename({"Type 1": "Type"}).with_columns(pl.lit(1).alias("cnt")) 
        type2 = data.filter(pl.col("Type 2").is_not_null()).select(pl.col("Type 2")).rename({"Type 2": "Type"}).with_columns(pl.lit(1).alias("cnt"))
        combined = pl.concat([type1, type2]) 
        result = (combined .group_by("Type") .agg(pl.count("cnt").alias("Total_Count")).with_columns((pl.col("Total_Count") / pl.sum("Total_Count")).alias("Percent")) ) 
        totals= result.select(["Type", "Total_Count"])
        #Si abilita la palette con i colori dei tipi
        alt.themes.enable('my_custom_theme')
        #Grafico a torta con fette di angolo proporzionale alla frequenza dei tipi
        Pie_Chart = alt.Chart(result).mark_arc(radius=50, radius2=100, cornerRadius=5).encode(    
        alt.Theta("Total_Count"),
        alt.Color("Type"),
        tooltip="Type"
        ).properties(height=400)
        #Testo che mostra le percentuali di ogni fetta della torta
        rad_text = alt.Chart(result).mark_text(radius=115).encode(
            text=alt.Text('Percent:N', format=".1%"),
            theta=alt.Theta('Total_Count:Q', stack=True),
            color=alt.Color("Type"))
        Pie_Chart + rad_text
        #Grafico a barre con la lunghezza pari alla freq. percentuale dei tipi
        bars=alt.Chart(result).mark_bar().encode(
            x=alt.X("Percent",title=None,axis=alt.Axis(labelExpr='100 * datum.value'), scale=alt.Scale(domain=[0, 0.17])),
            y=alt.Y("Type",title=None).sort('-x'),
            tooltip="Type",
            color=alt.Color("Type", legend=None)
        ).properties( width=350, height=450 )
        #Testo che mostra le percentuali
        text = bars.mark_text(
            align='left',
            baseline='middle',
            dx=3,
            color='Type'
        ).encode( text=alt.Text('Percent:N', format=".1%"))
        st.write("**DISTRIBUZIONE PERCENTUALE IN TUTTE LE GENERAZIONI:**")
        bars+text

    with col2:
        #La generazione 1 non ha pokemon di tipo buio: devo abilitare la palette di colori di conseguenza!
        if selected_gen!=1:
            alt.themes.enable('my_custom_theme')
        else:
            alt.themes.enable('my_first_theme')
        st.write(f"**DISTRIBUZIONE NELLA GENERAZIONE {selected_gen}**")
        #Operazione analoga alla creazione del subset precedente, ma filtrando i dati per la generazione selezionata dall'utente
        type1 = data.filter(pl.col("Generation")==selected_gen).select(pl.col("Type 1")).rename({"Type 1": "Type"}).with_columns(pl.lit(1).alias("cnt")) 
        type2 = data.filter(pl.col("Generation")==selected_gen, pl.col("Type 2").is_not_null()).select(pl.col("Type 2")).rename({"Type 2": "Type"}).with_columns(pl.lit(1).alias("cnt"))
        combined = pl.concat([type1, type2]) 
        result = (combined .group_by("Type") .agg(pl.count("cnt").alias("Total_Count")).with_columns((pl.col("Total_Count") / pl.sum("Total_Count")).alias("Percent")) ) 
        #grafico a torta
        Pie_Chart = alt.Chart(result).mark_arc(radius=50, radius2=100, cornerRadius=5).encode(
        alt.Theta("Total_Count"),
        alt.Color("Type"),
        tooltip="Type"
        ).properties(height=400)
        #testo
        rad_text = alt.Chart(result).mark_text(radius=115).encode(
            
            text=alt.Text('Percent:N', format=".1%"),
            theta=alt.Theta('Total_Count:Q', stack=True),
            color=alt.Color("Type", legend=None))
        Pie_Chart + rad_text
        #abilito il tema con i colori dei tipi
        alt.themes.enable('my_custom_theme')
        #Per rendere comparabili i grafici a barre, il grafico della generazione 1 deve includere una colonna (vuota) anche per il tipo buio. Si aggiunge allora una colonna al subset di prima...
        if selected_gen==1: 
            append=pl.DataFrame({"Type": ["Dark"], "Total_Count": [0], "Percent": [0.0]})
            append=append.with_columns(pl.col("Total_Count").cast(pl.UInt32))
            result.extend(append)
        result=result.join(totals, on="Type", how="inner").with_columns( pl.col("Total_Count_right").alias("General_sort"))
        #grafico a barre
        bars=alt.Chart(result).mark_bar().encode(
            x=alt.X("Percent",title=None,axis=alt.Axis(labelExpr='100 * datum.value'), scale=alt.Scale(domain=[0, 0.17])),
            y=alt.Y("Type",title=None, sort=alt.SortField("General_sort",'descending')),
            color=alt.Color("Type", legend=None),
            tooltip="Type"
        ).properties( width=350, height=450 )
        #testo
        text = bars.mark_text(
            align='left',
            baseline='middle',
            dx=3,
            color='Type'
        ).encode( text=alt.Text('Percent:N', format=".1%"))
        st.write(f"**DISTRIBUZIONE PERCENTUALE NELLA GENERAZIONE {selected_gen}:**")
        bars+text
    #Commento
    st.write("In particolare, nella prima generazione il tipo Buio e Acciaio sono poco frequenti in quanto introdotti (ed applicati retrospettivamente ad alcuni Pokémon) nella seconda Generazione.  \n Lo stesso vale, per le prime cinque Generazioni, per il tipo Folletto: questo è stato introdotto solo dalla sesta Generazione.")
    st.write("In luce di quest'ultima informazione, si può dunque affermare che la Generazione 5 sia quella con le distribuzioni più bilanciate.  \n Questo è probabilmente dovuto al fatto che la Generazione 5 è quella di Pokémon Versione Nera e Pokémon Versione Bianca, i giochi che volevano essere un nuovo inizio per la serie, introducendo ben 156 nuovi Pokémon (163 se si considerano le forme alternative) e senza riutilizzare Pokémon delle precedenti Generazioni.")

with st.container():
    st.header("Analisi")
    st.subheader("Totale statistiche spiegato da Stadio evolutivo, Rarità e Mega-Evoluzione")
    st.write("Si vuole studiare se è presente una relazione tra il Totale delle statistiche (misura della potenza di un Pokémon), lo Stadio evolutivo (il Pokémon è l'evoluzione finale della propria linea? È la prima, la seconda o la terza evoluzione?), la Rarità (il Pokémon è Leggendario o no?) e Mega-Evoluzione (il Pokémon è una Mega Evoluzione?).")
    #L'utente seleziona la Generazione da analizzare. I dati verranno filtrati per quella generazione
    selected_gen = st.slider("Seleziona la Generazione da analizzare:", 1,8,1, key=2)
    subdata=data.filter(pl.col("Generation")==selected_gen)
    alt.themes.enable('my_category_theme')  #abilito la palette per i grafici
    #Creo uno scatterplot che divide i Pokémon della generazione selezionata tra i tre stadi evolutivi, cambiando contorno del punto, forma e colore dell'area per codificare Evoluzione finale, Leggendarietà e Mega Evoluzione
    Points = alt.Chart(subdata).mark_point(size=100, width=50).encode(
        alt.X('jitter:Q', title=None,axis=alt.Axis(values=[0], ticks=False, grid=False, labels=False),
        scale=alt.Scale(domain=(-0.5, 1.5)),
        ),  #utilizzo il jitter per far sì che i punti non siano sovrapposti tra di loro
        alt.Y("BST", title='Totale Statistiche').scale(domain=[100, 800]),
        shape=alt.Shape("Legendary:N").title(["[Forma] Leggendario","(0=No, 1=Sì):"]),
        color=alt.Color('Final Evolution:N').title(["[Contorno] Evoluzione Finale","(0=No, 1=Sì):"]),
        fill=alt.Fill('Mega Evolution:N').title(["[Area] Mega Evoluzione","(0=No, 1=Sì):"]),
        tooltip=["Name", "BST"],
        column=alt.Column(
        'Evolutionary Stage:N',
        title="Stadio Evolutivo",
        header=alt.Header(
            labelFontSize=14,
            titleFontSize=14,
            labelAngle=0,
            titleOrient='bottom',
            labelOrient='bottom',
            labelAlign='center',
            labelPadding=25,
            titleColor="black"        
        ))
    ).transform_calculate(
    # Genera jitter uniforme
    jitter="random()"
    ).properties(width=170, height=500).configure_facet(spacing=0)
    #Si disegna il grafico
    Points
    #Commento
    st.write("Il grafico evidenziano una correlazione tra Stadio evolutivo , Rarità, Mega-Evoluzione e la potenza del Pokémon misurata in termini di Statistiche totali.  \n In particolare, i Pokémon del tutto evoluti sono più potenti di quelli non del tutto evoluti. Inoltre, all'aumentare dello stadio evolutivo, aumenta la potenza (anche tra quelli del tutto evoluti).  \n I Pokémon Leggendari sono l'eccezione alla regola: svettano indipendentemente dal loro stadio evolutivo.  \n Le Mega Evoluzioni, come ci si poteva aspettare, sono più potenti delle loro forme base.")
    st.write("Si può inoltre notare come, all'aumentare dello stadio evolutivo, la varianza del totale delle statistiche diminuisca.")

    #Grafico analogo al precedente, ma anziché avere BST sull'asse Y ora c'è Catch Rate
    st.subheader("Tasso di cattura e Stadio evolutivo")
    st.write("Si vuole studiare se è presente una relazione tra il Tasso di cattura (misura di quanto facile da catturare è un Pokémon), lo Stadio evolutivo (il Pokémon è l'evoluzione finale della propria linea? È la prima, la seconda o la terza evoluzione?), la Rarità (il Pokémon è Leggendario o no?) e Mega-Evoluzione (il Pokémon è una Mega Evoluzione?).")
    selected_gen = st.slider("Seleziona la Generazione da analizzare:", 1,8,1, key=3)
    subdata=data.filter(pl.col("Generation")==selected_gen)
    alt.themes.enable('my_category_theme')
    Points = alt.Chart(subdata).mark_point(size=100, width=50).encode(
        alt.X('jitter:Q', title=None,axis=alt.Axis(values=[0], ticks=False, grid=False, labels=False),
        scale=alt.Scale(domain=(-0.5, 1.5)),
        ),
        alt.Y('Catch Rate', title='Tasso di Cattura').scale(domain=[0, 260]),
        shape=alt.Shape("Legendary:N").title(["[Forma] Leggendario","(0=No, 1=Sì):"]),
        color=alt.Color('Final Evolution:N').title(["[Contorno] Evoluzione Finale","(0=No, 1=Sì):"]),
        fill=alt.Fill('Mega Evolution:N').title(["[Area] Mega Evoluzione","(0=No, 1=Sì):"]),
        tooltip=["Name", 'Catch Rate'],
        column=alt.Column(
        'Evolutionary Stage:N',
        title="Stadio Evolutivo",
        header=alt.Header(
            labelFontSize=14,
            titleFontSize=14,
            labelAngle=0,
            titleOrient='bottom',
            labelOrient='bottom',
            labelAlign='center',
            labelPadding=25,
            titleColor="black"        
        ))
    ).transform_calculate(
    # Genera jitter uniforme
    jitter="random()"
    ).properties(width=170, height=500).configure_facet(spacing=0)
    Points
    st.write("Il grafico evidenziano una correlazione tra Stadio evolutivo , Rarità, Mega-Evoluzione e il Tasso di cattura dei Pokémon.  \n In luce dei risultati ottenuti dal grafico precedente (ovvero che la potenza di un Pokémon è proporzionale alla sua rarità e al suo stadio evolutivo), si può affermare che più è debole un Pokémon, più è facile da catturare.")
    st.write("Si può inoltre notare come, all'aumentare dello stadio evolutivo, la varianza del Tasso di cattura diminuisca.")

with st.container():
    st.subheader("Numero di nuovi Pokémon introdotti per Generazione")
    #Segue un grafico a barre che mostra quanti Pokémon sono stati introdotti in ogni generazione. Si evidenziano tre categorie "speciali": Keggendari, MegaEvoluzioni, del tutto evoluti.
    selection=st.selectbox(
    "Seleziona quale classe di Pokémon evidenziare:",
    ["Leggendari", "Mega Evoluzioni", "Pokémon alla fase evolutiva finale"], index=0)
    #Converto l'input dell'utente nei nomi delle colonne
    if selection == "Leggendari":
        selected="Legendary"
    elif selection == "Mega Evoluzioni":
        selected="Mega"
    else: selected="Final"
    processed_select=selected
    if selected is not "Legendary":
        processed_select=processed_select+" Evolution"

    #Grafico a barre. Si raggruppano i dati per generazione e categoria selezionata, aggiungendo le colonne conteggio per determinare l'altezza delle barre
    bars = alt.Chart(data.group_by(["Generation", processed_select]).agg(pl.col( processed_select).count().alias(f"{selected}_Count")).sort("Generation")).mark_bar().encode(
        y=alt.Y(f"{selected}_Count:Q", title='Numero di nuovi Pokémon introdotti').stack('zero'),
        x=alt.X("Generation:N", title='Generazione', axis=alt.Axis(labelAngle=-0)),
        color=alt.Color(f"{processed_select}:N").title([f"[Colore] {processed_select}","(0=No, 1=Sì):"]))
    #Testo che mostra i valori di ogni sotto-barra
    text = alt.Chart(data.group_by(["Generation", processed_select]).agg(pl.col( processed_select).count().alias(f"{selected}_Count")).sort("Generation")).mark_text(dx=0, dy=3, color='white', fontWeight="bold", yOffset=5).encode(
        y=alt.Y(f"{selected}_Count:Q", title='Numero di nuovi Pokémon introdotti').stack('zero'),
        x=alt.X("Generation:N", title='Generazione', axis=alt.Axis(labelAngle=-0)),
        detail=f"{processed_select}:N",
        text=alt.Text(f"sum({selected}_Count):Q"),
        )
    #Con questo si aggiunge un contorno al testo, rendendolo più leggibile
    text_background = text.mark_text(
        stroke='#6D4A97',
        strokeWidth=4,
        strokeJoin='round',
        dy=8
    )
    #Questo testo mostra il totale di unità sopra ogni barra
    text2=alt.Chart(data.group_by("Generation").count()).mark_text(dx=0, dy=3, color='black', fontWeight="bold", yOffset=-10).encode(
        y=alt.Y(f"count:Q", title='Numero di nuovi Pokémon introdotti').stack('zero'),
        x=alt.X("Generation:N", title='Generazione', axis=alt.Axis(labelAngle=-0)),
        
        text=alt.Text(f"count:Q"),
        )
    #Si sovrappongono i grafici nell'ordine corretto
    barplot= alt.layer(bars,text_background,text,text2).properties(width=700, height=500)
    barplot
    #commento
    st.write("Questo grafico mostra quanti Pokémon sono stati introdotti in ogni Generazione, ponendo l'attenzione su alcune categorie importanti per le analisi successive.  \n In particolare, si può notare:  \n - le Mega Evoluzioni siano presenti solo nella sesta Generazione  \n - la quarta Generazione ha introdotto, in proporzione, più Pokémon alla loro fase evolutiva finale rispetto alle altre Generazioni  \n - il numero di Pokémon Leggendari ha inizialmente trend crescente, stabilizzatosi dalla quinta Generazione in poi. L'unica eccezione è un picco nella settima Generazione, dovuto alla presenza delle Ultracreature.")

with st.container():
    #Il grafico più complesso del progetto. Si vedranno dei boxplot affiancati (per generazione) con scatterplot annessi.
    #Per gestire, sull'asse X, sia jitter che generazione, si sono affiancati più grafici grazie al metodo column di altair.
    st.subheader("Distribuzione del Totale delle Statistiche nel corso delle Generazioni")
    st.write("Si vuole studiare se i Pokémon introdotti nelle Generazioni più recenti sono più potenti (in termini di Totale delle statistiche) dei Pokémon delle generazioni precedenti.")
    st.write('Seleziona se includere queste classi di Pokémon nel grafico:')
    option_1 = st.checkbox('Leggendari', value=False)
    option_2 = st.checkbox('Mega Evoluzioni', value=False)
    tipo_pok = st.selectbox(
    "Seleziona il Tipo da analizzare:",
    ["Tutti i tipi", "Normale", "Fuoco", "Acqua", "Elettro", "Erba", "Ghiaccio", "Lotta", "Veleno", "Terra", "Volante", "Psico", "Coleottero", "Roccia", "Spettro", "Drago", "Buio", "Acciaio", "Folletto"], index=0)
    box_data= data
    #In base all'input dell'utente, si filtrano o meno i dati
    if not option_1:
        box_data=box_data.filter(pl.col("Legendary")==0)
    if not option_2:
        box_data=box_data.filter(pl.col('Mega Evolution')==0)
    #Si converte l'input dell'utente in un'operazione polars (se si è selezionato un tipo specifico)
    if tipo_pok == "Normale":
        box_data=box_data.filter((pl.col('Type 1')=="Normal")| (pl.col("Type 2") == "Normal"))
    elif tipo_pok == "Fuoco":
        box_data=box_data.filter((pl.col('Type 1')=="Fire")| (pl.col("Type 2") == "Fire"))
    elif tipo_pok == "Acqua":
        box_data=box_data.filter((pl.col('Type 1')=="Water")| (pl.col("Type 2") == "Water"))
    elif tipo_pok == "Elettro":
        box_data=box_data.filter((pl.col('Type 1')=="Electric")| (pl.col("Type 2") == "Electric"))
    elif tipo_pok == "Erba":
        box_data=box_data.filter((pl.col('Type 1')=="Grass")| (pl.col("Type 2") == "Grass"))
    elif tipo_pok == "Ghiaccio":
        box_data=box_data.filter((pl.col('Type 1')=="Ice")| (pl.col("Type 2") == "Ice"))
    elif tipo_pok == "Lotta":
        box_data=box_data.filter((pl.col('Type 1')=="Fighting")| (pl.col("Type 2") == "Fighting"))
    elif tipo_pok == "Veleno":
        box_data=box_data.filter((pl.col('Type 1')=="Poison")| (pl.col("Type 2") == "Poison"))
    elif tipo_pok == "Terra":
        box_data=box_data.filter((pl.col('Type 1')=="Ground")| (pl.col("Type 2") == "Ground"))
    elif tipo_pok == "Volante":
        box_data=box_data.filter((pl.col('Type 1')=="Flying")| (pl.col("Type 2") == "Flying"))
    elif tipo_pok == "Psico":
        box_data=box_data.filter((pl.col('Type 1')=="Psychic")| (pl.col("Type 2") == "Psychic"))
    elif tipo_pok == "Coleottero":
        box_data=box_data.filter((pl.col('Type 1')=="Bug")| (pl.col("Type 2") == "Bug"))
    elif tipo_pok == "Roccia":
        box_data=box_data.filter((pl.col('Type 1')=="Rock")| (pl.col("Type 2") == "Rock"))
    elif tipo_pok == "Spettro":
        box_data=box_data.filter((pl.col('Type 1')=="Ghost")| (pl.col("Type 2") == "Ghost"))
    elif tipo_pok == "Drago":
        box_data=box_data.filter((pl.col('Type 1')=="Dragon")| (pl.col("Type 2") == "Dragon"))
    elif tipo_pok == "Buio":
        box_data=box_data.filter((pl.col('Type 1')=="Dark")| (pl.col("Type 2") == "Dark"))
    elif tipo_pok == "Acciaio":
        box_data=box_data.filter((pl.col('Type 1')=="Steel")| (pl.col("Type 2") == "Steel"))
    elif tipo_pok == "Folletto":
        box_data=box_data.filter((pl.col('Type 1')=="Fairy")| (pl.col("Type 2") == "Fairy"))
    
    #Creo una base per il grafico (verranno sovrapposti)
    base=alt.Chart()
    #Si definisce il boxplot
    Boxplot = base.mark_boxplot(size=45, opacity=0.7, ticks=True).encode(
        alt.Y('BST', title='Totale Statistiche').scale(domain=[0, 800]),
        tooltip=["Name", 'BST'],
        )
    #Si vedrà anche lo scatterplot
    Points = base.mark_point().encode(
        alt.X('jitter:Q', title=None,axis=alt.Axis(values=[0], ticks=False, grid=False, labels=False), scale=alt.Scale(domain=(-0.5, 1.5)), #L'asse X è per il jitter
        ),
        alt.Y('BST', title='Totale Statistiche').scale(domain=[0, 800]),
        tooltip=["Name", 'BST'],
        shape=alt.Shape("Legendary:N").title(["[Forma] Leggendario","(0=No, 1=Sì):"]),
        color=alt.Color('Mega Evolution:N').title(["[Area] Mega Evoluzione","(0=No, 1=Sì):"]),
        ).transform_calculate(
    # Genera jitter uniforme
    jitter="random()"
    )

    #In base alla selezione, l'ordine di sovrapposizione dei grafici cambia. 
    #Ho pensato che, se la selezione è un tipo speciale, potesse essere interessante vedere le posizioni di ogni Pokémon (punti) sopra il boxplot (così puoi vedere il tooltip)
    if tipo_pok == "Tutti i tipi":
        layered=alt.layer(Points, Boxplot,data=box_data).properties(width=60, height=500).facet(
        column=alt.Column(
            'Generation:N',
            title="Generazione",
            header=alt.Header(
                labelFontSize=14,
                titleFontSize=14,
                labelAngle=0,
                titleOrient='bottom',
                labelOrient='bottom',
                labelAlign='center',
                labelPadding=25,
                titleColor="black"        
            )), 
        spacing=0).configure_view(stroke=None)
    else:
        layered=alt.layer(Boxplot,Points, data=box_data).properties(width=60, height=500).facet(
            column=alt.Column(
                'Generation:N',
                title="Generazione",
                header=alt.Header(
                    labelFontSize=14,
                    titleFontSize=14,
                    labelAngle=0,
                    titleOrient='bottom',
                    labelOrient='bottom',
                    labelAlign='center',
                    labelPadding=25,
                    titleColor="black"        
                )), 
            spacing=0).configure_view(stroke=None)
    #Si disegna il grafico
    layered
    
    #Commenti
    if tipo_pok != "Tutti i tipi":
        st.write("**ATTENZIONE!** Le unità statistiche presenti in certi Tipi sono troppo poche per trarre risultati statistici affidabili.  \n Per un'analisi statistica, si selezioni 'Tutti i tipi'.  \n L'utilità di vedere i boxplot per singolo Tipo è utile solo per vedere se, in una determinata Generazione, hanno introdotto Pokémon potenti o meno per quel determinato tipo.")
    else:
        st.write("Si può vedere come la mediana del Totale delle statistiche cresca con l'aumentare della Generazione.  \n In particolare:  \n - la mediana della Generazione 4 risulta più alta rispetto a quello che ci si attenderebbe dal trend perché presenta un rapporto tra i Pokémon del tutto evoluti e quello dei Pokémon non del tutto evoluti più alto di qualsiasi altra generazione  \n - se si considerano le Mega Evoluzioni, la Generazione 6 è quella con la mediana più alta.  \n - se si includono i Pokémon Leggendari, il trend della mediana del Totale delle statistiche cresce più in fretta. Ciò è dovuto al trend crescente del numero di Pokémon Leggendari col passare delle Generazioni.")
        st.write("Il grafico, al netto di Pokémon Leggendari e Mega Evoluzioni, sembra comunque evidenziare una correlazione tra il Totale delle statistiche di un Pokémon e la Generazione.")

with st.container():
    st.subheader("Distribuzione del Numero di Tipi per Generazione e per Stadio Evolutivo")
    #Si vuole disegnare un grafico a barre che conti, per generazione, quanti pokémon con uno o due tipi sono stati introdotti.
    #Si crea una colonna "Tipo" che classifica i pokémon in Monotipo o Doppio tipo (in base ai valori di Type 2), poi si raggruppa per generazione e "Tipo"  e si aggiunge la colonna conteggio
    bar_data=data.with_columns(
    pl.when(pl.col("Type 2").is_null())
      .then(pl.lit("Monotipo"))
      .otherwise(pl.lit("Doppio Tipo"))
      .alias("Tipo")
    ).group_by("Generation", "Tipo"
    ).agg(pl.col("Tipo").count().alias(f"Tipo_Count")
    ).sort("Generation")
    #Si sovrapporranno più grafici, quindi si crea la base
    base=alt.Chart()
    #Grafico a barre
    bars = base.mark_bar().encode(
        y=alt.Y(f"Tipo_Count:Q", title='Numero di nuovi Pokémon introdotti').stack('zero'),
        x=alt.X("Generation:N", title='Generazione', axis=alt.Axis(labelAngle=-0)),
        xOffset=alt.XOffset("Tipo", sort="descending"),
        color=alt.Color(f"Tipo:N").title(""))
    #Testo
    text = base.mark_text(dx=0, dy=3, color='black', fontWeight="bold", yOffset=-10).encode(
        y=alt.Y(f"Tipo_Count:Q", title='Numero di nuovi Pokémon introdotti').stack('zero'),
        x=alt.X("Generation:N", title='Generazione', axis=alt.Axis(labelAngle=-0)),
        detail=f"Tipo:N",
        xOffset=alt.XOffset("Tipo", sort="descending"),
        text=alt.Text(f"sum(Tipo_Count):Q"),
        )
    #Sovrappongo i grafici
    layered=alt.layer(bars, text,data=bar_data).properties(width=800, height=500)
    #Disegno il grafico
    layered
    #Commento
    st.write("Il rapporto tra i Pokémon Monotipo o con Doppio Tipo è pressoché costante in ogni Generazione, tranne che nella sesta e nella settima.  \n   \n  .")

    col1, col2= st.columns([3,1])
    with col1:
        #Si vuole creare un grafico a barre che, per ogni stadio evolutivo, abbia barre affiancate per Mono e Doppio tipo, suddivise per opacità in base al valore di Final Evolution
        bar_data=data.with_columns(
        pl.when(pl.col("Type 2").is_null())
        .then(pl.lit("Monotipo"))
        .otherwise(pl.lit("Doppio Tipo"))
        .alias("Tipo")
        ).group_by("Generation", "Tipo", "Final Evolution", "Evolutionary Stage"
        ).agg(pl.col("Tipo").count().alias(f"Tipo_Count")
        ).sort("Generation")
        #Si sovrapporranno più grafici, quindi si crea la base
        base=alt.Chart()
        #bars e bars2 sono lo stesso grafico
        bars = base.mark_bar().encode(
            y=alt.Y(f"Tipo_Count:Q", title='Numero di Pokémon').stack('zero').stack('zero'),
            x=alt.X("Evolutionary Stage:N", title='Stadio Evolutivo', axis=alt.Axis(labelAngle=-0)),
            xOffset=alt.XOffset("Tipo:N",sort=alt.SortField(field='Tipo', order='descending')),
            color=alt.Color(f"Tipo:N").title("[Colore] Numero di tipi"),
            opacity=alt.Opacity("Final Evolution:N").title("[Opacità] Evoluzione Finale","(0=No, 1=Sì):"))
        bars2 = base.mark_bar().encode(
            y=alt.Y(f"Tipo_Count:Q", title='Numero di Pokémon').stack('zero').stack('zero'),
            x=alt.X("Evolutionary Stage:N", title='Stadio Evolutivo', axis=alt.Axis(labelAngle=-0)),
            xOffset=alt.XOffset("Tipo:N",sort=alt.SortField(field='Tipo', order='descending')),
            color=alt.Color(f"Tipo:N").title("[Colore] Numero di tipi"),
            opacity=alt.Opacity("Final Evolution:N").title("[Opacità] Evoluzione Finale","(0=No, 1=Sì):"))
        #Il testo dice quante unità ci sono nella barra
        text = base.mark_text(dy=10, color="black", fontWeight="bold").encode(
            y=alt.Y("sum(Tipo_Count):Q").stack('zero'),
            x=alt.X("Evolutionary Stage:N"),
            xOffset=alt.XOffset("Tipo:N",sort=alt.SortField(field='Tipo', order='descending')),
            text="sum(Tipo_Count):Q",
            detail="Final Evolution:N"
        )
        #Il contorno del testo lo rende più leggibile
        text_background = text.mark_text(
            stroke='white',
            strokeWidth=4,
            strokeJoin='round',
            dy=10
        )
        #Sovrappongo 2 volte lo stesso grafico, così i colori sono più opaci. Non particolarmente elegante, ma funziona.
        #Non ho trovato come gestire l'opacità in altair (nel senso che sia io a decidere che valori assegnare)
        layered=alt.layer(bars, bars2, text_background, text,data=bar_data).properties(width=500, height=350)
        #Si disegna il grafico
        layered
    with col2:
        st.write("All'aumentare dello stadio evolutivo, aumenta la frequenza dei Pokémon con due tipi e diminuisce quella dei Pokémon con un solo tipo.  \n Inoltre, tra i Pokémon del tutto evoluti, prevalgono quelli con due tipi.")

with st.container():
    #Si disegna un grafico molto simile al boxplot+jitter precedente
    st.subheader("Distribuzione del Totale delle Statistiche per Numero di Tipi nel corso delle Generazioni")
    st.write("Si vuole studiare se i Pokémon con due tipi siano più potenti (in termini di Totale delle statistiche) dei Pokémon con un solo tipo.")
    st.write('Seleziona se includere queste classi di Pokémon nel grafico:')
    option_1 = st.checkbox('Leggendari', value=True, key="4th")
    option_2 = st.checkbox('Mega Evoluzioni', value=True, key="5th")
    #Come prima, si crea la colonna Tipo
    box_data=data.with_columns(
    pl.when(pl.col("Type 2").is_null())
      .then(pl.lit("Monotipo"))
      .otherwise(pl.lit("Doppio Tipo"))
      .alias("Tipo")
    )
    #In base alla selezione dell'utente, si filtrano i dati in base a se si vuole includere o meno MegaEvoluzioni e Leggendari
    if not option_1:
        box_data=box_data.filter(pl.col("Legendary")==0)    
    if not option_2:        
        box_data=box_data.filter(pl.col('Mega Evolution')==0)    
    #Boxplot affiancati (si studia BST, categoriale: Tipo)
    Boxplot = base.mark_boxplot(size=20, opacity=1, ticks=True).encode(
        alt.Y('BST', title='Totale Statistiche').scale(domain=[150, 800]),
        xOffset=alt.XOffset("Tipo", sort="descending"),
        color="Tipo:N",
        tooltip=["Name", 'BST'],
        )
    #Si affiancano le colonne per ogni generazione.
    layered=alt.layer(Boxplot,data=box_data.group_by("Generation", "Tipo", "BST", "Name").agg(pl.col("Tipo").count().alias(f"Tipo_Count")).sort("Generation")).properties(width=50, height=500).facet(
    column=alt.Column(
        'Generation:N',
        title="Generazione",
        header=alt.Header(
            labelFontSize=14,
            titleFontSize=14,
            labelAngle=0,
            titleOrient='bottom',
            labelOrient='bottom',
            labelAlign='center',
            labelPadding=25,
            titleColor="black"        
        )), 
    spacing=20).configure_view(stroke=None)
    #Disegna il grafico
    layered
    #Commento
    st.write("In ogni Generazione il Totale delle statistiche è mediamente più alto per i Pokémon con due tipi.  \n Ciò suggerisce una correlazione tra Totale delle statistiche e Numero di Tipi di un Pokémon.  \n Ciò può essere spiegato dal fatto che i Doppi Tipi siano prevalenti nei Pokémon evoluti, che come precedentemente visto sono più potenti.")

with st.container():
    #Boxplot con punti "jitterati"
    st.subheader("Distribuzione del Totale delle Statistiche per Tipo")
    st.write('Si vuole studiare se è presente una relazione tra il Tipo di un Pokémon e il Totale delle statistiche.')
    st.write('Seleziona se includere queste classi di Pokémon nel grafico:')
    option_1 = st.checkbox('Leggendari', value=False, key="2nd")
    option_2 = st.checkbox('Mega Evoluzioni', value=False, key="3rd")
    selected_generation = st.selectbox(
    "Seleziona quale generazione analizzare:",
    ["Tutte le generazioni", 1,2,3,4,5,6,7,8], index=0)
    box_data= data
    #Processa i dati in modo da far rientrare un pokemon con due tipi sia nel boxplot del tipo primario che del secondario
    #(si può vedere facilmente con Ash Greninja, che è il punto più alto sia del tipo Buio che Acqua, se si escludono Mega Evoluzioni e Leggendari)
    data_type1 = (data.with_columns(pl.col("Type 1").alias("Type")))
    # Aggiungi le righe per Type 2 (solo se non è null)
    data_type2 = (
        data
        .filter(pl.col("Type 2").is_not_null())
        .with_columns(pl.col("Type 2").alias("Type"))    )
    # Unisci i due dataframe
    box_data = pl.concat([data_type1, data_type2])
    #Si filtrano i dati in base all'input dell'utente
    if not option_1:
        box_data=box_data.filter(pl.col("Legendary")==0)    
    if not option_2:        
        box_data=box_data.filter(pl.col('Mega Evolution')==0)    
    if selected_generation is not "Tutte le generazioni":        
        box_data=box_data.filter(pl.col('Generation')==selected_generation)
    #Boxplot
    Boxplot = base.mark_boxplot(size=20, opacity=0.7, ticks=True).encode(
        alt.Y('BST', title='Totale Statistiche').scale(domain=[150, 800]),
        tooltip=["Name", 'BST'],
        )
    #Punti con jitter
    Points = base.mark_point().encode(
        alt.X('jitter:Q', title=None,axis=alt.Axis(values=[0], ticks=False, grid=False, labels=False),
        scale=alt.Scale(domain=(-0.5, 1.5)),
        ),
        alt.Y('BST', title='Totale Statistiche').scale(domain=[150, 800]),
        tooltip=["Name", 'BST'],
        shape=alt.Shape("Legendary:N").title(["[Forma] Leggendario","(0=No, 1=Sì):"]),
        color=alt.Color('Mega Evolution:N').title(["[Area] Mega Evoluzione","(0=No, 1=Sì):"]),
        ).transform_calculate(
    # Genera jitter uniforme
    jitter="random()"
    )
    #Sovrappine i grafici
    layered=alt.layer(Points, Boxplot,data=box_data).properties(width=30, height=500).facet(
    column=alt.Column(
        'Type:N',
        title="Tipo",
        header=alt.Header(
            labelFontSize=14,
            titleFontSize=14,
            labelAngle=-45,
            titleOrient='bottom',
            labelOrient='bottom',
            labelAlign='center',
            labelPadding=25,
            titleColor="black"        
        )), 
    spacing=0).configure_view(stroke=None)
    #Disegna il grafico
    layered
    #Commento
    if selected_generation != "Tutte le generazioni":
        st.write("**ATTENZIONE!** Le unità statistiche presenti in certi Tipi sono troppo poche per trarre risultati statistici affidabili.  \n Per un'analisi statistica, si selezioni 'Tutte le generazioni'.  \n L'utilità di vedere i boxplot per singolo Tipo in una Generazione specifica è utile solo per vedere se, in una determinata Generazione, hanno introdotto Pokémon potenti o meno per quel determinato tipo.")
    else:
        st.write("Si può vedere come certi Tipi di Pokémon abbiano Totale delle statistiche mediamente più alto di altri. In particolare:  \n - il tipo Coleottero ha mediana, primo e terzo quartile più bassi degli altri tipi  \n - il tipo Erba e Veleno hanno le mediana del Totale delle statistiche più bassa dopo il tipo Coleottero  \n - il tipo Drago e Ghiaccio hanno la mediana del Totale delle statistiche più alto degli altri tipi  \n - altri tipi potenti, in termini di mediana del Totale delle statistiche, sono Lotta, Psico e Acciaio  \n - se si includono i Pokémon Leggendari, il Totale delle statistiche cresce soprattutto per il tipo Drago e Psico, in minor misura per il tipo Acciaio  \n - se si includono le Mega Evoluzioni, il Totale delle statistiche del tipo Drago e, in minor misura, del tipo Acciaio, aumentano più degli altri tipi.")
        st.write("Il grafico sembra dunque evidenziare una correlazione tra il Totale delle statistiche e il Tipo di un Pokémon, oltre a suggerire una relazione tra i pokémon Leggendari e i tipi Drago e Psico.")

with st.container():
    st.subheader("Distribuzione del Numero di Tipi, Evoluzioni Finali e Leggendari per ogni Tipo")
    st.write('Si vuole studiare se alcuni tipi presentano una frequenza maggiore di alcune categorie (Pokémon con due Tipi, Evoluzioni Finali e Leggendari) che influenzano il Totale delle statistiche.')
    selection=st.selectbox(
    "Seleziona di quale classe di Pokémon calcolare la percentuale per ogni Tipo:",
    ["Leggendari", "Pokémon con due Tipi", "Pokémon alla fase evolutiva finale"], index=0)

    if selection == "Leggendari":
        processed_select="Legendary"
    elif selection == "Pokémon con due Tipi":
        processed_select="Tipo"
    else:
        processed_select="Final Evolution"
    
    final_data= data
    #Processa i dati in modo da far rientrare un pokemon con due tipi sia nel boxplot del tipo primario che del secondario
    #(si può vedere facilmente con Ash Greninja, che è il punto più alto sia del tipo Buio che Acqua, se si escludono Mega Evoluzioni e Leggendari)
    data_type1 = (data.with_columns(pl.col("Type 1").alias("Type")))
    # Aggiungi le righe per Type 2 (solo se non è null)
    data_type2 = (
        data
        .filter(pl.col("Type 2").is_not_null())
        .with_columns(pl.col("Type 2").alias("Type"))    )
    # Unisci i due dataframe
    final_data = pl.concat([data_type1, data_type2])
    #Classifica i Pokémon in Monotipo o Doppio Tipo in base al valore di Type 2
    final_data = final_data.with_columns(
        (pl.when(pl.col("Type 2").is_null()).then(pl.lit("Monotipo")).otherwise(pl.lit("Doppio Tipo")).alias("Tipo"))
    ).group_by(["Legendary", "Final Evolution", "Type", "Tipo"]).agg( #si aggiungono i conteggi per categoria speciale
        (pl.count().alias("Tipo_count")),
        (pl.col("Legendary").count().alias("Leg_count")),
        (pl.col("Final Evolution").count().alias("Evo_count"))
    ).with_columns(  #Si aggiungono le percentuali come nuove colonne
        (pl.col("Leg_count") / pl.col("Leg_count").sum() * 100).alias("perc_Legendary"),
        (pl.col("Tipo_count") / pl.col("Tipo_count").sum() * 100).alias("perc_Tipo"),
        (pl.col("Evo_count") / pl.col("Evo_count").sum() * 100).alias("perc_Final Evolution"),
    )

    #Grafico a barre per la categoria selezionata
    bar_chart = alt.Chart(final_data.group_by("Type",processed_select).agg(pl.col(f"perc_{processed_select}").sum())).mark_bar().encode(
        y=alt.Y("Type:N", title="Tipo del Pokémon", axis=alt.Axis(labelAngle=0)),
        x=alt.X(f"perc_{processed_select}:Q", stack="normalize", title= "Percentuale"),  # Asse Y: percentuale
        color=alt.Color(f"{processed_select}:N"),  #Colore in base alla categoria scelta dall'utente
        tooltip=alt.value(None)
    ).properties(
        width=800,
        height=500
    ).configure_view(stroke=None, strokeWidth=0,)
    #Disegna il grafico
    bar_chart
    #Commento
    st.write("Dal grafico si può osservare che:  \n - i tipi Drago e Psico (seguiti da Acciaio e Lotta) hanno una maggiore percentuale di Pokémon Leggendari rispetto agli altri Tipi.  \n Invece il tipo Coleottero, assieme a Normale e Veleno, ha la minor frequenza di Pokémon Leggendari.  \n - La frequenza di Pokémon con due tipi non sembra essere correlata ai Tipi di Pokémon con Totale delle Statistiche più alto.  \n - il tipo Drago, Lotta, Acciaio e Psico hanno una maggior percentuale di Pokémon del tutto evoluti al loro interno.  \n Il tipo Erba, Veleno e Coleottero invece ne hanno la frequenza minore.")

with st.container():
    st.header("Conclusioni")
    st.write("Dall'analisi si può evincere come Stadio Evolutivo, Mega-Evoluzione e Rarità di un Pokémon siano direttamente correlate alla sua potenza (in termini di Somma delle statistiche).")
    st.write("Altre variabili, che sembrano essere correlate al totale delle Statistiche, appaiono tali poiché sono correlate alle tre variabili sopracitate.  \n È il caso del Numero di Tipi di un Pokémon: i Pokémon con doppio tipo sono più potenti di quelli con un tipo solo perché il Doppio Tipo ha una frequenza che cresce con lo stadio evolutivo dei Pokémon, risultando maggiore tra i Pokémon del tutto evoluti.")
    st.write("Per quanto riguarda il Tipo di un Pokémon, il Totale delle Statistiche sembra essere spiegato soltanto in parte da questa variabile.  \n In alcuni casi, come i tipi Drago, Psico, Acciaio e Lotta, il Totale delle statistiche tende ad essere più alto degli altri tipi perché questi sono correlati alla frequenza di Pokémon Leggendari e alla frequenza di Pokémon del tutto evoluti al loro interno.  \n Ma in altri casi, come il tipo Ghiaccio, non ci sono relazioni con altre variabili che sembrino giustificare il diverso andamento del Totale delle statistiche.")
    st.write("Si può dunque affermare che il Totale delle statistiche è maggiormente influenzato da Stadio Evolutivo, Mega-Evoluzione e Rarità, e solo in minor parte dal Tipo di un Pokémon.")
