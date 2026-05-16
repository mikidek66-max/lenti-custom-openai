# Caso anonimo — progetto lente RGP corneale OD

> File tecnico anonimizzato. Non contiene nome, data di nascita o altri identificativi personali.  
> Progetto basato su topografia OD caricata. Da validare con refrazione soggettiva completa, prova diagnostica, fluoresceina, sovrarefrazione e valutazione biomicroscopica.

---

## 1. Dati topografici disponibili

| Parametro | Valore |
|---|---:|
| Occhio | OD |
| Data esame | 2024-11-18 |
| K piatto / SimK | 41.84 D = 8.07 mm @ 138° |
| K ripido / SimK | 43.08 D = 7.83 mm @ 48° |
| Astigmatismo corneale | 1.24 D |
| BFS Maloney | 42.34 D |
| BFC Maloney | 1.08 D |
| Topo Irregularity Index | 0.7 |
| HVID | 11.74 mm |
| Hsag | 2463 µm |
| C-V | 0.5 mm |
| Alfa | 3.2° |
| Sag @ 11.5 mm 180-0° | 2359 µm |
| Sag @ 11.5 mm 210-30° | 2360 µm |
| Sag @ 11.5 mm 150-330° | 2333 µm |
| Sag @ 11.5 mm 270-90° | 2413 µm |

---

## 2. Refrazione comunicata

```text
OD SF -4.50
```

Assunzione operativa: refrazione a piano occhiale con distanza apice circa 12 mm. Mancano cilindro soggettivo, asse e visus.

---

## 3. Valutazione

- Astigmatismo corneale moderato-basso: 1.24 D.
- Pattern topografico compatibile con astigmatismo obliquo relativamente regolare.
- TI 0.7: non orienta, da solo, verso disegno da cheratocono.
- Prima scelta: RGP corneale standard/asferica, non cheratoconica.
- Geometria bitorica non necessaria in prima prova, salvo fluoresceina instabile o basculamento marcato.
- Con refrazione solo sferica, la prima RGP può restare sferica/asferica posteriore. Il cilindro corneale dovrebbe essere in buona parte gestito dal menisco lacrimale.

---

## 4. Progetto prima lente diagnostica RGP OD

| Parametro | Scelta proposta |
|---|---:|
| Tipo lente | RGP corneale |
| Geometria | Asferica / tangenziale, posteriore sfero-asferica |
| Materiale | GP alto Dk, preferibilmente Dk 100–125 |
| BOZR / BC | 8.00 mm |
| Diametro totale | 9.70 mm |
| BOZD / zona ottica posteriore | 7.70 mm |
| Periferia | standard, edge lift medio |
| Potere teorico iniziale | circa -4.50 D |

---

## 5. Razionale tecnico

### BOZR

- K piatto = 8.07 mm.
- K ripido = 7.83 mm.
- Media cheratometrica approssimata = circa 7.95 mm.
- Con astigmatismo corneale 1.24 D, una prima BOZR a 8.00 mm è vicina all'allineamento centrale, leggermente più stretta del K piatto e più piatta del K ripido.

### Diametro

- HVID 11.74 mm.
- Diametro corneale RGP proposto: 9.70 mm.
- Scelta orientata a centratura e comfort, con diametro non eccessivamente piccolo.

### Geometria

- Non partire con disegno cheratoconico.
- Non partire con bitorica interna.
- Usare asferica/tangenziale per seguire meglio la periferia corneale e migliorare comfort/centratura.

---

## 6. Calcolo potere teorico

Refrazione a piano occhiale:

```text
SF -4.50
```

Compensazione al vertice stimata a 12 mm:

```text
-4.50 D → circa -4.25 D a piano corneale
```

Curva base scelta:

```text
BC 8.00 mm ≈ 42.19 D
```

K piatto:

```text
41.84 D
```

Differenza BC rispetto a K piatto:

```text
42.19 - 41.84 = +0.35 D
```

La lente è circa 0.35 D più stretta del K piatto; quindi genera un menisco lacrimale positivo di circa +0.35 D. Per compensarlo, si aggiunge circa -0.35 D al potere della lente.

Calcolo:

```text
-4.25 + (-0.35) = -4.60 D
```

Arrotondamento produttivo:

```text
BVP teorico iniziale = -4.50 D
```

Nota: -4.75 D è accettabile se in refrazione si tende a preferire il massimo positivo/minimo negativo non sufficiente o se alla prova la sovrarefrazione indica ulteriore negativo.

---

## 7. Progetto sintetico ordinabile come prova

```text
OD — RGP corneale asferica/tangenziale
BC 8.00
DIA 9.70
BOZD 7.70
Periferia standard / edge lift medio
Materiale GP alto Dk 100–125
BVP -4.50 D teorico iniziale
```

---

## 8. Valutazione in prova

| Controllo | Target |
|---|---|
| Centratura | centrale o lieve superiore, non decentrata infero-temporale |
| Movimento | 1.0–1.5 mm dopo ammiccamento |
| Fluoresceina centrale | allineamento o lievissimo pooling centrale |
| Mid-periphery | appoggio regolare, no bearing marcato |
| Bordo | anello periferico continuo, non eccessivo |
| Comfort iniziale | accettabile per RGP diagnostica |
| Visus | stabile dopo ammiccamento |
| Sovrarefrazione | necessaria per BVP finale |

---

## 9. Problem solving

| Reperto alla prova | Modifica |
|---|---|
| Appoggio centrale marcato | stringere BC a 7.95 mm |
| Pooling centrale e lente ferma | appiattire BC a 8.05 mm |
| Decentramento inferiore | aumentare diametro a 9.80–9.90 mm o valutare edge lift |
| Movimento eccessivo / edge lift eccessivo | aumentare diametro o ridurre lift periferico |
| Sigillatura periferica | aprire periferia / aumentare edge lift |
| Basculamento obliquo stabile | valutare posteriore torica o diametro maggiore |
| Residuo cilindrico in sovrarefrazione > 0.75 D | valutare front toric o bitorica |

---

## 10. Dati ancora da confermare

- Refrazione soggettiva completa.
- Visus con refrazione.
- Distanza apice effettiva.
- Sovrarefrazione sopra lente diagnostica.
- Fluoresceina e centratura dopo assestamento.

Formula operativa finale:

```text
BVP finale = potere lente diagnostica + sovrarefrazione compensata + eventuale correzione lacrima/vertice
```
