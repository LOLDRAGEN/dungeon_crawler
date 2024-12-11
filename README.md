# Dungeon Crawler

Dette prosjektet er et tekstbasert spill hvor spilleren navigerer gjennom rom med ulike egenskaper som kan påvirke helsen. Målet er å komme seg gjennom labyrinten uten å dø.

## Innhold

- `main.py`: Hovedprogrammet som styrer spillets flyt.
- `player.py`: Definerer spillerklassen.
- `room.py`: Inneholder definisjoner for forskjellige romtyper.
- `test_dungeon.py`: Inneholder tester for de ulike komponentene i prosjektet.

## Spillmekanikk

1. Spilleren starter med 10 HP.
2. Labyrinten består av flere typer rom:
   - **Vanlige rom** (`Room`): Inneholder kun beskrivelse og valg av retning.
   - **Helsende rom** (`HealRoom`): Øker spillerens HP.
   - **Skaderom** (`DmgRoom`): Reduserer spillerens HP.
   - **Tilfeldige rom** (`RandRoom`): Kan enten øke eller redusere HP basert på tilfeldigheter.
3. Spilleren navigerer gjennom rommene ved å velge retninger.
4. Spillet avsluttes når spilleren enten dør eller når målet.

## Filstruktur

- **`main.py`**: Starter spillet og håndterer logikken for navigasjon og hendelser i rom.
- **`player.py`**: Implementerer spillerens egenskaper og helse.
- **`room.py`**: Inneholder klasser for de forskjellige romtypene.
- **`test_dungeon.py`**: Enhetstester for prosjektets klasser.

## Klasser og Funksjoner

### `Player` (i `player.py`)
- Attributter:
  - `name` (str): Navn på spilleren.
  - `hp` (int): Spilleren starter med 10 HP.

### `Room` (i `room.py`)
- Attributter:
  - `name` (str): Navn på rommet.
  - `desc` (str): Beskrivelse av rommet.
  - `connect` (list): Tilkoblede rom.

### `HealRoom` (i `room.py`)
- Arver fra `Room`.
- Ekstra attributt:
  - `heal` (int): Hvor mye HP spilleren helbredes.

### `DmgRoom` (i `room.py`)
- Arver fra `Room`.
- Ekstra attributt:
  - `dmg` (int): Hvor mye skade spilleren tar.

### `RandRoom` (i `room.py`)
- Arver fra `Room`.
- Ekstra attributter:
  - `heal` (int): Potensiell helbredelse.
  - `dmg` (int): Potensiell skade.

## Testing

Enhetstester for prosjektet er implementert i `test_dungeon.py`. Testene dekker følgende:

- Initialisering av `Player`.
- Initialisering av `Room`, `HealRoom`, `DmgRoom` og `RandRoom`.

For å kjøre testene, bruk følgende kommando:
```bash
pytest test_dungeon.py
