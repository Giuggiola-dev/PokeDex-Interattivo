import polars as pl

#Ritorna un numero dato in input con tre cifre (per esempio 8 diventerà 008)
def three_digits(num):
    return f"{num:03d}"

#Dato il nome di un pokémon, ritorna l'url di una sua immagine.
#Il processo sarebbe stato più semplice se database e sorgente delle immagini avessero avuto
#un codice identificativo comune per ogni Pokémon, ma non è così.
#La funzione converte il nome del pokémon in un link, considerando alcune eccezioni:
# - casi particolari come Charizard che ha 2 forme mega
# - Pokémon con diverse forme alternative come Rotom
# - Pokémon mancanti dalla prima sorgente
#In un mondo ideale avrei usato una sola sorgente, ma
#1) Il repository GitHub dal quale prendo la maggior parte delle immagini stranamente omette delle immagini di alcuni Pokémon di Galar
#2) Serebii.net non permette di vedere il link https://www.serebii.net/pokemon/art/ (403 forbidden), quindi mi è impossibile decodificare il modo in cui funziona la loro nomenclatura delle immagini
#3) Il sito Pokémon ufficiale usa una nomenclatura delle immagini incompatibile con il mio dataset
#I crediti alle sorgenti sono nel README.
def img_url_generator(name, data):
    row=data.row(by_predicate=(pl.col("Name") == name), named=True)
    url="https://raw.githubusercontent.com/harshit23897/Pokemon-Sprites/refs/heads/master/assets/images/"
    url=url+three_digits(row["Number"])
    if row["Mega Evolution"] == 1:
        if row["Number"] == 382 or row["Number"] == 383:
            url=url + "-Primal"
        else:
            url=url + "-Mega"
        if row["Name"] == "Mega Charizard X" or row["Name"]=="Mega Mewtwo X":
            url=url + "-X"
        elif row["Name"] == "Mega Charizard Y" or row["Name"]=="Mega Mewtwo Y":
            url=url + "-Y"
    if row["Alolan Form"] == 1:
        url=url + "-Alola"        
    if row["Galarian Form"] == 1:
        url=url + "-Galar"
        if row["Number"] in [79, 80, 144, 145, 146, 199, 554]:
            url=f"https://www.serebii.net/pokemon/art/{three_digits(row['Number'])}-g"
    if row["Number"] == 386:
        if row["Name"] == "Deoxys Defense Form":
            url=url + "-Defense"
        elif row["Name"] == "Deoxys Attack Form":
            url=url + "-Attack"
        elif row["Name"] == "Deoxys Speed Form":
            url=url + "-Speed"
    if row["Name"] == "Darmanitan Zen-Mode" or row["Name"] == "Galarian Darmanitan Zen-Mode":
        url=url + "-Zen"
    if row["Name"] == "Giratina-Origin":
        url=url + "-Origin"
    if row["Number"] == 479:
        if row["Name"] == "Rotom-Wash":
            url=url + "-Wash"
        elif row["Name"] == "Rotom-Fan":
            url=url + "-Fan"
        elif row["Name"] == "Rotom-Frost":
            url=url + "-Frost"
        elif row["Name"] == "Rotom-Mow":
            url=url + "-Mow"
        elif row["Name"] == "Rotom-Heat":
            url=url + "-Heat"
    if row["Number"] == 646:
        if row["Name"] == "White Kyurem":
            url=url + "-White"
        elif row["Name"] == "Black Kyurem":
            url=url + "-Black"
    if row["Name"] == "Meloetta-Pirouette":
        url=url + "-Pirouette"
    if row["Name"] == "Thundurus-Therian" or row["Name"] == "Tornadus-Therian" or row["Name"] == "Landorus-Therian":
        url=url + "-Therian"
    if row["Number"] == 718:
        if row["Name"] == "Zygarde 10%":
            url=url + "-10"
        elif row["Name"] == "Zygarde Complete":
            url=url + "-Complete"
        else:
            url=url + "-50"
    if row["Name"] == "Hoopa Unbound":
        url=url + "-Unbound"
    if row["Number"] == 741:
        if row["Name"] == "Oricorio Pom-Pom Style":
            url=url + "-Pom-Pom"
        elif row["Name"] == "Oricorio Sensu Style":
            url=url + "-Sensu"
        elif row["Name"] == "Oricorio Pa'u Style":
            url=url + "-Pau"
    if row["Number"] == 745:
        if row["Name"] == "Lycanroc Midnight":
            url=url + "-Midnight"
        elif row["Name"] == "Lycanroc Dusk":
            url=url + "-Dusk"
    if row["Name"] == "Wishiwashi School":
            url=url + "-School"
    if row["Name"] == "Minior Core Form":
            url=url + "-Red"
    if row["Number"] == 800:
        if row["Name"] == "Dusk Mane Necrozma":
            url=url + "-Dusk"
        elif row["Name"] == "Dawn Mane Necrozma":
            url=url + "-Dawn"
        elif row["Name"] == "Ultra Necrozma":
            url=url + "-Ultra"
    return url+".png"


#Dato il valore del moltiplicatore danni, ritona una stringa formattata per streamlit colorata in base al valore
def dmg_colour(num):
    if num==1:
        return f"{num}"
    elif num>1:
        return f":red[**{num}**]"
    else:
        return f":blue[**{num}**]"
    

#Dato un pokémon, ritorna una stringa formattata per streamlit (include un colore di sfondo) per il suo n-esimo tipo
def type_n_check(n, row):
    if row[f'Type {n}'] is not None:
            if row[f'Type {n}'] == "Normal": return(":gray-background[Normale]")
            elif row[f'Type {n}'] == "Fire": return(":red-background[Fuoco]")
            elif row[f'Type {n}'] == "Water": return(":blue-background[Acqua]")
            elif row[f'Type {n}'] == "Electric": return(":orange-background[Elettro]")
            elif row[f'Type {n}'] == "Grass": return(":green-background[Erba]")
            elif row[f'Type {n}'] == "Ice": return(":blue-background[Ghiaccio]")
            elif row[f'Type {n}'] == "Fighting": return(":red-background[Lotta]")
            elif row[f'Type {n}'] == "Poison": return(":violet-background[Veleno]")
            elif row[f'Type {n}'] == "Ground": return(":orange-background[Terra]")
            elif row[f'Type {n}'] == "Flying": return(":blue-background[Volante]")
            elif row[f'Type {n}'] == "Psychic": return(":violet-background[Psico]")
            elif row[f'Type {n}'] == "Bug": return(":green-background[Coleottero]")
            elif row[f'Type {n}'] == "Rock": return(":red-background[Roccia]")
            elif row[f'Type {n}'] == "Ghost": return(":violet-background[Spettro]")
            elif row[f'Type {n}'] == "Dragon": return(":blue-background[Drago]")
            elif row[f'Type {n}'] == "Dark": return(":gray-background[Buio]")
            elif row[f'Type {n}'] == "Steel": return(":gray-background[Acciaio]")
            elif row[f'Type {n}'] == "Fairy": return(":violet-background[Folletto]")
    else: return("")


#Dato un Pokémon, ritorna un colore in base al suo tipo primario
def poke_colour(n, row):
    if row[f'Type {n}'] == "Normal": return("#A1A1A1")
    elif row[f'Type {n}'] == "Fire": return("#D4392F")
    elif row[f'Type {n}'] == "Water": return("#4B79BB")
    elif row[f'Type {n}'] == "Electric": return("#EFBE31")
    elif row[f'Type {n}'] == "Grass": return("#5D9C3C")
    elif row[f'Type {n}'] == "Ice": return("#78CBEF")
    elif row[f'Type {n}'] == "Fighting": return("#EF8733")
    elif row[f'Type {n}'] == "Poison": return("#6D4A97")
    elif row[f'Type {n}'] == "Ground": return("#7F451A")
    elif row[f'Type {n}'] == "Flying": return("#8FB7E4")
    elif row[f'Type {n}'] == "Psychic": return("#DC4C79")
    elif row[f'Type {n}'] == "Bug": return("#94A135")
    elif row[f'Type {n}'] == "Rock": return("#ADA984")
    elif row[f'Type {n}'] == "Ghost": return("#6B426E")
    elif row[f'Type {n}'] == "Dragon": return("#4C5FA8")
    elif row[f'Type {n}'] == "Dark": return("#4E403F")
    elif row[f'Type {n}'] == "Steel": return("#73A2B9")
    elif row[f'Type {n}'] == "Fairy": return("#BA7FB5")


#Dato un Pokémon, controlla i valori del moltiplicatore danni per tipo e crea una lista dei tipi a cui è debole
def weakness_list(row):
    weak_list=[]
    if row['Against Normal']>1: weak_list.append("Normal")
    if row['Against Fire']>1: weak_list.append("Fire")
    if row['Against Water']>1: weak_list.append("Water")
    if row['Against Electric']>1: weak_list.append("Electric")
    if row['Against Grass']>1: weak_list.append("Grass")
    if row['Against Ice']>1: weak_list.append("Ice")
    if row['Against Fighting']>1: weak_list.append("Fighting")
    if row['Against Poison']>1: weak_list.append("Poison")
    if row['Against Ground']>1: weak_list.append("Ground")
    if row['Against Flying']>1: weak_list.append("Flying")
    if row['Against Psychic']>1: weak_list.append("Psychic")
    if row['Against Bug']>1: weak_list.append("Bug")
    if row['Against Rock']>1: weak_list.append("Rock")
    if row['Against Ghost']>1: weak_list.append("Ghost")
    if row['Against Dragon']>1: weak_list.append("Dragon")
    if row['Against Dark']>1: weak_list.append("Dark")
    if row['Against Steel']>1: weak_list.append("Steel")
    if row['Against Fairy']>1: weak_list.append("Fairy")
    return weak_list


#Dato un Pokémon, controlla i valori del moltiplicatore danni per tipo e crea una lista dei tipi a cui è resistente
def resist_list(row):
    res_list=[]
    if row['Against Normal']<1: res_list.append("Normal")
    if row['Against Fire']<1: res_list.append("Fire")
    if row['Against Water']<1: res_list.append("Water")
    if row['Against Electric']<1: res_list.append("Electric")
    if row['Against Grass']<1: res_list.append("Grass")
    if row['Against Ice']<1: res_list.append("Ice")
    if row['Against Fighting']<1: res_list.append("Fighting")
    if row['Against Poison']<1: res_list.append("Poison")
    if row['Against Ground']<1: res_list.append("Ground")
    if row['Against Flying']<1: res_list.append("Flying")
    if row['Against Psychic']<1: res_list.append("Psychic")
    if row['Against Bug']<1: res_list.append("Bug")
    if row['Against Rock']<1: res_list.append("Rock")
    if row['Against Ghost']<1: res_list.append("Ghost")
    if row['Against Dragon']<1: res_list.append("Dragon")
    if row['Against Dark']<1: res_list.append("Dark")
    if row['Against Steel']<1: res_list.append("Steel")
    if row['Against Fairy']<1: res_list.append("Fairy")
    return res_list