# Lenti Custom OpenAI Starter

Starter kit per progetto di lenti a contatto custom:
- calcolo parametri iniziali per lenti morbide custom;
- selezione preliminare prodotto MedLac per indicazione clinica;
- template ordine laboratorio;
- esempi YAML;
- test automatici;
- hook opzionale OpenAI API.

> Uso clinico: il calcolo è uno strumento di supporto. La scelta finale richiede valutazione professionale, topografia/tomografia, film lacrimale, biomicroscopia, refrazione e prova applicativa.

## Struttura

```text
calculators/
  morbide_custom.py
  morbide_custom_cli.py
  product_catalog.py
  product_selector_cli.py
  genera_sintesi_openai.py
examples/
  caso_morbida_torica.yaml
  caso_morbida_bitorica.yaml
  selezione_prodotto_cheratocono.yaml
  selezione_prodotto_multifocale.yaml
templates/
  ordine_medlac.md
tests/
  test_morbide_custom.py
  test_product_catalog.py
```

## Installazione

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt
```

## Esecuzione calcolatore morbide custom

```bash
python calculators/morbide_custom_cli.py examples/caso_morbida_torica.yaml
```

## Selezione prodotto MedLac

```bash
python calculators/product_selector_cli.py examples/selezione_prodotto_cheratocono.yaml
```

Indicazioni gestite nella fase 2:

```text
cornea_regolare
cornea_irregolare
cheratocono
prismatica
multifocale
controllo_miopia
terapeutica
filtrante
```

Prodotti MedLac inseriti:

```text
MED 02 PRISMA / SOFT BITORIC
MED PRISMODIREZIONALE
MED MULTIVISION SOFT
MED CONTROL
MED CONUS / KERATOPLUS
MED BIOPROTECT
MED FILTER / MED FILTER TORIC
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

## Fase 2

La fase 2 introduce un selettore prodotto separato dal calcolo geometrico. Il selettore assegna uno score in base a:
- indicazione clinica;
- compatibilità BC;
- compatibilità DIA;
- range sfera/cilindro/addizione/prisma;
- preferenza per materiali SiHy o ad alta permeabilità.

Il risultato è una lista ordinata di prodotti candidati con motivazioni e warning sui parametri fuori range.
