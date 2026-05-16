from __future__ import annotations

import os
import sys
import json
from pathlib import Path
import yaml
from openai import OpenAI

from morbide_custom import SoftLensInput, calculate_soft_lens


SYSTEM_PROMPT = """Sei un assistente tecnico per contattologia.
Produci una sintesi operativa prudente, strutturata, in italiano.
Non sostituire la valutazione clinica. Evidenzia dati mancanti e controlli necessari.
"""


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python calculators/genera_sintesi_openai.py examples/caso.yaml")
        return 2

    if not os.getenv("OPENAI_API_KEY"):
        print("Errore: variabile OPENAI_API_KEY non impostata.")
        return 1

    data = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
    params = SoftLensInput(**data)
    result = calculate_soft_lens(params).to_dict()

    client = OpenAI()
    prompt = f"""
Caso YAML:
{json.dumps(data, indent=2, ensure_ascii=False)}

Output deterministico:
{json.dumps(result, indent=2, ensure_ascii=False)}

Compila:
1. Parametri ordine iniziale
2. Razionale
3. Controlli in studio
4. Possibili modifiche se lente stretta/larga/decentrata
5. Dati mancanti
"""

    response = client.responses.create(
        model="gpt-5.5-thinking",
        input=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    print(response.output_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
