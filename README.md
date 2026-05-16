# Lenti Custom OpenAI Starter

Starter kit per progetto di lenti a contatto custom:
- calcolo parametri iniziali per lenti morbide custom;
- template ordine laboratorio;
- template referto applicativo;
- esempi YAML;
- test automatici;
- hook opzionale OpenAI API.

> Uso clinico: il calcolo è uno strumento di supporto. La scelta finale richiede valutazione professionale, topografia/tomografia, film lacrimale, biomicroscopia, refrazione e prova applicativa.

## Struttura

```text
calculators/
  morbide_custom.py
  morbide_custom_cli.py
  genera_sintesi_openai.py
examples/
  caso_morbida_torica.yaml
  caso_morbida_bitorica.yaml
templates/
  ordine_medlac.md
  referto_applicativo.md
tests/
  test_morbide_custom.py
```

## Installazione

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

## Esecuzione calcolatore

```bash
python calculators/morbide_custom_cli.py examples/caso_morbida_torica.yaml
```

## Esecuzione test

```bash
pytest
```

## Uso OpenAI API opzionale

Impostare la variabile ambiente:

```bash
export OPENAI_API_KEY="..."
```

Poi:

```bash
python calculators/genera_sintesi_openai.py examples/caso_morbida_torica.yaml
```

## Convenzioni adottate

### Diametro totale
- lente sferica: HVID + 2.00 mm
- lente torica/bitorica: HVID + 2.20 mm

### BC iniziale
Secondo tabella MedLac caricata nel progetto:
- gruppo morbido classico: BENZ-38 / G3X / G4X / HYDRO-49
- gruppo intermedio: CONTAFLEX 67 / ULTRAPERM 74 / G72-HW
- gruppo SiHy: DEFINITIVE 65 / DEFINITIVE 74

### Delta-sag
Se è disponibile OC-SAG, viene suggerito un target CL-SAG = OC-SAG + 120/280 µm.
