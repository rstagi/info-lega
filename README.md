# Info lega

Per installare le dipendenze lancia:
```
pip3 install
```

Per prendere le info della tua lega, semplicemente lancia il seguente comando:
```
python3 get-info-lega.py <nome-lega>
```

Lo script ritorna le seguenti informazioni:
- Nome competizione
- Squadre
- Calendario (con i risultati, se disponibili)
- Classifica
- Coundown per la prossima partita

## Output di esempio

```
NOME COMPETIZIONE:
FantaPippo 2023/2024


SQUADRE:
I Magnifici Undici
Goal Diggers
Fantamaniacs
Dream Team
Calcioholics
Fantabombers
Squadra Vittoria
Fantafuriaeam Picco


CALENDARIO:

Giornta 1:
I Magnifici Undici - Goal Diggers: 2 - 1
Fantamaniacs - Dream Team: 1 - 1
Calcioholics - Fantabombers: 3 - 2
Squadra Vittoria - Fantafuriaeam Picco: 2 - 0

Giornata 2:
I Magnifici Undici - Fantamaniacs: 3 - 1
Goal Diggers - Dream Team: 2 - 2
Calcioholics - Squadra Vittoria: 1 - 0
Fantabombers - Fantafuriaeam Picco: 2 - 1

...

Giornata 38:
Fantamaniacs - Calcioholics: -
Dream Team - Fantabombers: -
Squadra Vittoria - I Magnifici Undici: -
Fantafuriaeam Picco - Goal Diggers: -


CLASSIFICA:
1. I Magnifici Undici (9.0 pt)
2. Fantamaniacs (7.0 pt)
3. Calcioholics (6.0 pt)
4. Fantabombers (6.0 pt)
5. Goal Diggers (4.0 pt)
6. Dream Team (1.0 pt)
7. Squadra Vittoria (1.0 pt)
8. Fantafuriaeam Picco (0.0 pt)


COUNTDOWN:
3d 8h 11m 58s
```
