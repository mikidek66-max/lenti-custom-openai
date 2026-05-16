from __future__ import annotations

import json
import sys
from pathlib import Path
import yaml

from product_catalog import ProductQuery, select_products


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python calculators/product_selector_cli.py examples/selezione_prodotto.yaml")
        return 2

    data = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8"))
    query = ProductQuery(**data)
    matches = select_products(query)
    print(json.dumps([match.to_dict() for match in matches], indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
