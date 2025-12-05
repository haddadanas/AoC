from pathlib import Path
import re
import os
import sys
from typing import Any


__all__ = ["read_input", "validate_test"]


def _main_dir() -> str:
    main = Path(sys.argv[0])
    if main.exists() and main.is_file():
        return str(main.resolve().parent)
    return str(Path.cwd())


def read_input(
    file_path: str,
    delimator: str = '\n',
    pattern: str | None = None,
) -> list[str] | list[tuple[str, ...]]:
    dir_path = _main_dir()
    with open(os.path.join(dir_path, file_path), 'r') as file:
        lines = file.read().strip().split(delimator)
    if pattern:
        regex = re.compile(pattern)
        lines = [m.groups() for line in lines if (m := regex.match(line))]
    return lines


def validate_test(evaluated_value: Any, expected_value: Any) -> None:
    assert evaluated_value == expected_value, (
        f"Test failed: expected {expected_value}, got {evaluated_value}"
    )
