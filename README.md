PokéDex interattivo + Analisi esplorativa dei dati
====


Struttura e scopi del progetto
-------

Il progetto è diviso in due sezioni: PokéDex interattivo e Analisi esplorativa dei dati.

### PokéDex interattivo

Questa sezione fornisce le informazioni su un Pokémon selezionato dall'utente. Le informazioni mostrate includono:
- Immagine del Pokémon
- Nome e numero nel PokéDex nazionale
- Tipi e abilità
- Statistiche
- Debolezze e resistenze agli altri tipi

Viene inoltre fornito uno strumento per comparare più Pokémon tra di loro in termini di Totale delle Statistiche.



### Analisi esplorativa dei dati

In questa sezione vengono elaborati i dati per sviluppare dei grafici. 
I grafici includono:
- grafici a torta
- grafici a barre
- scatterplot
- boxplot


Dalle rappresentazioni dei dati si possono dedurre alcune relazioni tra le variabili.

In particolare si studiano:
- Totale delle statistiche
- Tasso di cattura

In relazione a:
- Numero di tipi
- Tipo
- Generazione
- Stadio evolutivo
- Rarità
- Mega Evoluzione


Origine del materiale impiegato
-------

Il progetto impiega materiali originari da alcune fonti sul web.

### Dataset

Il dataset è stato preso da:
https://www.kaggle.com/datasets/maca11/all-pokemon-dataset

Il dataset è stato modificato rispetto a quello originale della fonte.
Sono state aggiunte informazioni NON ottenibili tramite pre-processing:
- Evolutionary Stage
- Final Evolution

Informazioni confrontate per sicurezza con quelle dell'applicazione [dataDex](https://datadex.talzz.com/).

### Immagini

Immagini dei Pokémon prese da:
https://github.com/harshit23897/Pokemon-Sprites

Immagini mancanti (Forme regionali di Galar di: Slowpoke, Slowbro, Slowking, Articuno, Zapdos, Moltres e Darumaka) prese dal sito:
[serebii.net](https://serebii.net/)

Immagine del Professor Oak presa dal sito:
[Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Professor_Oak)


Immagine della tabella di efficacia degli attacchi tra i diversi tipi presa da:
https://it.wikipedia.org/wiki/File:PokemonTabTipi.png

Descrizione del dataset
-------

Le variabili presenti nel dataset sono:


`Number` (Intero): Numero identificativo del Pokémon (ID)

`Name` (Stringa): Nome del Pokémon

`Type 1` (Stringa): Primo tipo del Pokémon

`Type 2` (Stringa): Secondo tipo del Pokémon (può essere vuoto se non ha due tipi)

`Abilities` (Lista di Stringhe): Lista delle abilità del Pokémon  

`HP` (Intero): Punti salute

`Att` (Intero): Attacco

`Def` (Intero): Difesa

`Spa` (Intero): Attacco speciale 

`Spd` (Intero) Difesa speciale

`Spe` (Intero): Velocità

`BST` (Intero): Somma delle statistiche

`Height` (Float): Altezza del Pokémon (in metri) 

`Weight` (Float): Peso del Pokémon (in kg)

`Generation` (Intero - Categoriale): Generazione di appartenenza del Pokémon

`Experience type` (Stringa): Tipo di curva di esperienza

`Evolutionary Stage` (Intero): Stadio evolutivo (1, 2 o 3)

`Final Evolution` (Intero - Booleano): Indica se è l’evoluzione finale (1) o no (0)

`Catch Rate` (Intero): Tasso di cattura (0-255)

`Legendary` (Intero - Booleano): Indica se è un Pokémon leggendario (1) o no (0)

`Mega Evolution` (Intero - Booleano): Indica se è una mega-evoluzione (1) o no (0)

`Alolan Form` (Intero - Booleano): Indica se è una forma di Alola (1) o no (0)

`Galarian Form` (Intero - Booleano): Indica se è una forma di Galar (1) o no (0)

`Against Normal` (Float): Moltiplicatore di danno contro il tipo Normale

`Against Fire` (Float): Moltiplicatore di danno contro il tipo Fuoco

`Against Water` (Float): Moltiplicatore di danno contro il tipo Acqua

`Against Electric` (Float): Moltiplicatore di danno contro il tipo Elettro

`Against Grass` (Float): Moltiplicatore di danno contro il tipo Erba

`Against Ice` (Float): Moltiplicatore di danno contro il tipo Ghiaccio

`Against Fighting` (Float): Moltiplicatore di danno contro il tipo Lotta

`Against Poison` (Float): Moltiplicatore di danno contro il tipo Veleno

`Against Ground` (Float): Moltiplicatore di danno contro il tipo Terra

`Against Flying` (Float): Moltiplicatore di danno contro il tipo Volante

`Against Psychic` (Float): Moltiplicatore di danno contro il tipo Psico

`Against Bug` (Float): Moltiplicatore di danno contro il tipo Coleottero

`Against Rock` (Float): Moltiplicatore di danno contro il tipo Roccia

`Against Ghost` (Float): Moltiplicatore di danno contro il tipo Spettro

`Against Dragon` (Float): Moltiplicatore di danno contro il tipo Drago

`Against Dark` (Float): Moltiplicatore di danno contro il tipo Buio

`Against Steel` (Float): Moltiplicatore di danno contro il tipo Acciaio

`Against Fairy` (Float): Moltiplicatore di danno contro il tipo Folletto

Come eseguire:
-------

Il progetto è un'applicazione web programmata in Python con Streamlit. 
I grafici interattivi sono gestiti con Altair e il dataset è manipolato con Polars.
Le immagini sono gestite con Pillow.

Innanzitutto, è necessario clonare il repository per scaricare i file necessari.


Per eseguire l'applicazione più facilmente, *si raccomanda* di installare [uv](https://docs.astral.sh/uv/getting-started/installation/). 

Nel prompt dei comandi basterà digitare:

```
uv run streamlit run app.py
```


*Alternativamente*, si possono installare Python e le librerie necessarie per eseguire il progetto.
In questo caso, bisognerà digitare nel prompt dei comandi:

```
python -m streamlit run app.py
```

Alla prima esecuzione, la creazione del venv da parte di uv richiederà del tempo. Inoltre, Streamlit potrebbe chiedere di inserire la propria mail. Ciò può essere ignorato premendo Invio.

Purtroppo, quando si interagisce con la pagina, Streamlit non la aggiorna sempre completamente, e alcuni grafici Altair appaiono vuoti. In realtà sono stati calcolati, basta passarci sopra con il cursore per farli apparire.
