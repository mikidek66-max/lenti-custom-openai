# Uso operativo con topografia e prescrizione

Questa guida descrive il flusso pratico quando si possiede una topografia/tomografia e una prescrizione.

## 1. Raccogliere i dati minimi

### Dalla topografia/tomografia
- K piatto, preferibilmente in mm e D
- K steep, preferibilmente in mm e D
- asse dei meridiani principali
- astigmatismo corneale
- Kmax, se presente
- HVID / diametro irideo visibile orizzontale
- eccentricità o asfericità, se presente
- SAG / OC-SAG, se disponibile
- mappa assiale/tangenziale/elevazione/pachimetria, se disponibili
- diagnosi o sospetto: cornea regolare, astigmatismo elevato, cheratocono, post-chirurgia, ecc.

### Dalla prescrizione
- sfera
- cilindro
- asse
- distanza apice, se nota
- addizione, se presbite
- AV con occhiale
- occhio: OD o OS

### Dalle esigenze del paziente
- ore di porto richieste
- uso: lavoro, sport, guida, VDT, multifocale, controllo miopia, terapeutica
- precedenti lenti usate e problemi riscontrati

## 2. Decidere il tipo di lente desiderata

Prima della progettazione, indicare il tipo di lente da progettare:

- morbida custom
- morbida torica
- morbida bitorica
- morbida per cheratocono / cornea irregolare
- RGP
- sclerale
- ortho-k
- multifocale
- prismatica
- terapeutica / filtrante

## 3. Compilare il caso in formato YAML

Esempio per morbida torica:

```yaml
k_flat_mm: 7.80
k_steep_mm: 7.55
hvid_mm: 11.80
sphere_spectacle: -3.75
cyl_spectacle: -1.25
axis: 180
vertex_distance_mm: 12.0
lens_type: torica
material_group: definitive65_74
ocular_sag_um: 3600
notes: "Caso da topografia e prescrizione."
```

## 4. Lanciare il calcolo parametri

```bash
python calculators/morbide_custom_cli.py examples/caso_morbida_torica.yaml
```

Il risultato fornisce:
- diametro totale stimato
- BC iniziale
- potere al piano corneale
- cilindro e asse
- astigmatismo corneale stimato
- target SAG, se OC-SAG presente
- warning sui dati mancanti

## 5. Lanciare la selezione prodotto

Esempio cheratocono:

```yaml
indication: cheratocono
bc_mm: 8.10
dia_mm: 14.50
sphere_d: -6.00
cyl_d: -2.50
prefer_silicone_hydrogel: true
```

Comando:

```bash
python calculators/product_selector_cli.py examples/selezione_prodotto_cheratocono.yaml
```

Il risultato propone prodotti candidati con score, motivazioni e warning.

## 6. Output finale atteso

Per ogni caso il risultato operativo dovrebbe contenere:

- tipo lente consigliata
- prodotto candidato
- materiale
- BC
- diametro
- sfera
- cilindro
- asse
- eventuale toricità interna
- target SAG o nota sulla sua assenza
- note ordine laboratorio
- controlli in studio dopo applicazione

## 7. Uso rapido senza terminale

Se non si usa Python, il flusso più semplice è:

1. caricare in ChatGPT la topografia/tomografia;
2. scrivere la prescrizione completa;
3. indicare il tipo di lente desiderata;
4. chiedere: "calcola progetto iniziale e ordine laboratorio";
5. ChatGPT restituisce il progetto, usando i file del progetto e i criteri del repository.

## 8. Nota clinica

Il calcolo non sostituisce la prova su occhio. Validare sempre centraggio, movimento, push-up, copertura limbare, stabilità assiale, comfort, AV, sovrarefrazione e biomicroscopia.