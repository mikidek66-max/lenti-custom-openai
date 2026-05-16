# Caso simulato — progettazione lente morbida torica semestrale

> Documento tecnico simulato per progettazione di lente a contatto morbida torica custom semestrale.  
> Caso non riferito a paziente reale. Da validare sempre con esame clinico, topografia/tomografia reale, film lacrimale, prova applicativa, valutazione alla lampada a fessura e sovrarefrazione.

---

## 1. Obiettivo

Simulare una progettazione completa per **OD** di una lente morbida torica custom semestrale, usando criteri di calcolo coerenti con una tabella MedLac per lenti morbide toriche e con un approccio sagittale moderno.

---

## 2. Dati simulati di partenza — OD

| Parametro | Valore simulato |
|---|---:|
| Refrazione occhiale | **-2.25 / -1.75 × 175** |
| Distanza apice | 12 mm |
| K piatto | **42.25 D @ 180 = 7.99 mm** |
| K ripido | **44.10 D @ 90 = 7.65 mm** |
| Astigmatismo corneale | **1.85 D secondo regola** |
| HVID | **11.80 mm** |
| Pupilla mesopica | 5.8 mm |
| Eccentricità media | 0.48 |
| OC-SAG simulata a corda 14.00 mm | **3210 µm** |
| Quadro topografico | Bow-tie regolare, nessun sospetto ectasico |

### Interpretazione

- Cornea simulata **regolare**.
- Astigmatismo prevalentemente corneale.
- Indicazione compatibile con **lente morbida torica custom**.
- Non vi sono, nella simulazione, indizi che orientino verso RGP, sclerale o ortocheratologia.

---

## 3. Scelta lente

| Voce | Scelta |
|---|---|
| Tipo | **Morbida torica custom** |
| Modello | **MED 06 Torica** |
| Ricambio | **6 mesi / semestrale** |
| Geometria | **Bicurva torica** |
| Materiale | **SiHy / Definitive 74** |
| Trattamento | **Hydra-PEG consigliato** |
| Ottica | **HD** |
| Marcatura | riferimento ore 6 |
| Porto | Daily wear |

### Razionale

La scelta di una lente torica morbida custom semestrale è coerente con:

- astigmatismo corneale regolare;
- cilindro rifrattivo significativo;
- richiesta specifica di lente morbida torica semestrale;
- necessità di diametro, base curve e asse personalizzabili.

---

## 4. Calcolo diametro

Criterio di partenza per lente morbida torica:

```text
TD LAC = HVID + 2.20 mm
```

Calcolo:

```text
11.80 + 2.20 = 14.00 mm
```

### Diametro proposto

```text
DIA = 14.00 mm
```

---

## 5. Calcolo curva base / BOZR

K piatto simulato:

```text
Ks = 7.99 mm
```

Per diametro **14.00–14.40 mm** e materiale **Definitive 65/74**, criterio usato:

```text
BC = Ks + 0.90 mm
```

Calcolo:

```text
7.99 + 0.90 = 8.89 mm
```

### Curva base proposta

```text
BC / BOZR = 8.90 mm
```

### Razionale

Con materiale SiHy/Definitive 74, la BC 8.90 mm dovrebbe mantenere un buon equilibrio fra:

- copertura corneo-limbare;
- centratura;
- stabilità rotazionale;
- movimento post-ammiccamento non eccessivo;
- rischio ridotto di fitting troppo chiuso.

---

## 6. Controllo sagittale simulato

| Parametro | Valore |
|---|---:|
| OC-SAG simulata a 14.00 mm | **3210 µm** |
| CL-SAG stimata con BC 8.90 / DIA 14.00 | **3404 µm** |
| Δ-sag | **+194 µm** |

### Interpretazione sagittale

```text
Δ-sag = CL-SAG - OC-SAG = 3404 - 3210 = +194 µm
```

Il valore simulato di circa **+194 µm** è coerente con un fitting morbido stabile ma non eccessivamente stretto.

### Decisione

Non partirei più piatta di **8.90 mm**.  
Una BC 9.00 mm rischierebbe di ridurre troppo la profondità sagittale e di aumentare mobilità/decentramento.  
Una BC 8.80 mm sarebbe da considerare solo se alla prova la lente risultasse mobile o instabile.

---

## 7. Potere lente

Refrazione occhiale:

```text
-2.25 / -1.75 × 175
```

Compensazione al vertice meridionale approssimata:

| Meridiano | Potere occhiale | Potere circa su LAC |
|---|---:|---:|
| 175° | -2.25 | -2.19 |
| 85° | -4.00 | -3.82 |

Riscrittura torica approssimata:

```text
-2.25 / -1.75 × 175
```

Dato il potere moderato, la variazione da compensazione al vertice è clinicamente minima. In prima lente manterrei il cilindro pieno.

---

## 8. Stabilizzazione e asse

### Simulazione alla prova

| Osservazione | Valore |
|---|---:|
| Marcatura a ore 6 | ruota **5° a sinistra** |
| Regola applicata | **LARS** |
| Asse refrattivo | 175° |
| Asse da ordinare | **180°** |

Regola LARS:

```text
Left Add, Right Subtract
```

Se la lente ruota a sinistra di 5°:

```text
175 + 5 = 180°
```

---

## 9. Progetto finale simulato — OD

| Parametro | Valore finale |
|---|---:|
| Lente | **MED 06 Torica** |
| Ricambio | **Semestrale / 6 mesi** |
| Materiale | **Definitive 74 SiHy** |
| Trattamento | **Hydra-PEG consigliato** |
| Geometria | **Bicurva torica** |
| BC / BOZR | **8.90 mm** |
| DIA | **14.00 mm** |
| Sfera | **-2.25 D** |
| Cilindro | **-1.75 D** |
| Asse ordinato | **180°** |
| Ottica | **HD** |
| Marcatura | ore 6 |
| Porto | **Daily wear** |

### Prescrizione sintetica ordinabile

```text
OD MED 06 TORIC
Materiale: Definitive 74 SiHy
BC 8.90
DIA 14.00
PWR -2.25 / -1.75 × 180
Ricambio 6 mesi
Ottica HD
Hydra-PEG consigliato
```

---

## 10. Controllo alla consegna

Valutare dopo almeno **15–20 minuti** di assestamento.

| Controllo | Target |
|---|---|
| Centratura | completa copertura corneo-limbare |
| Movimento post-ammiccamento | circa **0.20–0.40 mm** |
| Push-up test | mobile ma non libera |
| Rotazione | stabile, idealmente ≤5° |
| Recupero asse dopo ammiccamento | rapido |
| Comfort | buono entro pochi minuti |
| Sovrarefrazione | preferibilmente plano o minima |
| Iperemia/staining | assenti |
| Impronta congiuntivale | assente |
| Visione | stabile, senza fluttuazione marcata |

---

## 11. Problem solving

| Problema | Correzione tecnica |
|---|---|
| Lente troppo mobile / decentrata | aumentare DIA a **14.20** oppure stringere BC a **8.80–8.85** |
| Lente troppo stretta / push-up resistente | appiattire BC a **9.00** o ridurre DIA se copertura e centratura lo permettono |
| Visione instabile con rotazione | applicare LARS e rivalutare stabilizzazione |
| Rotazione >10° non stabile | cambiare design/stabilizzazione, non solo asse |
| Comfort scarso inferiore | controllare bordo, spessore, interazione palpebrale |
| Sovrarefrazione sferica costante | integrare nella sfera finale |
| Sovrarefrazione cilindrica | sospettare asse errato, flessione o rotazione instabile |

---

## 12. Affidabilità della simulazione

### Affidabilità tecnica

**Media-alta**, perché i parametri sono coerenti con:

- tabella di calcolo per morbide toriche;
- criterio HVID + 2.20 mm;
- scelta BC da Ks + incremento per materiale;
- controllo sagittale;
- gestione asse con regola LARS.

### Limiti clinici

**Non sostituisce una prova reale.** Mancano:

- topografia/tomografia reale;
- HVID reale misurato;
- valutazione palpebrale;
- NIBUT/TBUT e qualità lacrimale;
- biomicroscopia;
- prova applicativa;
- sovrarefrazione;
- controllo dopo ore di porto.

---

## 13. Output finale

```text
OD — MED 06 TORICA SEMESTRALE
BC 8.90
DIA 14.00
PWR -2.25 / -1.75 × 180
Materiale Definitive 74 SiHy
Hydra-PEG consigliato
Ottica HD
Daily wear
```
