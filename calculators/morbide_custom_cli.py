from __future__ import annotations

import sys
import json
from pathlib import Path
import yaml

from morbide_custom import SoftLensInput, calculate_soft_lens


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python calculators/morbide_custom_cli.py examples/caso.yaml")
        return 2

    path = Path(sys.argv[1])
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    params = SoftLensInput(**data)
    result = calculate_soft_lens(params)

    print(json.dumps(result.to_dict(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
