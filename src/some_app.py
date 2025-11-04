"""Some App that uses a spell book"""

import ast
from pathlib import Path
from typing import Any

import magic2


class AllImports(ast.NodeVisitor):
    def __init__(self, source: str) -> None:
        self.source = source
        self.imports: list[str | None] = []

    def visit_Import(self, node: ast.Import) -> None:
        self.imports.append(ast.get_source_segment(self.source, node))

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        self.imports.append(ast.get_source_segment(self.source, node))


def get_spells(module: str) -> list[magic2.Spell]:
    source = Path(module).with_suffix(".py").read_text()
    spell_book_code = ast.parse(source, module, "exec")

    visitor = AllImports(source)
    visitor.visit(spell_book_code)
    if visitor.imports:
        raise ValueError(f"import detected: {visitor.imports}")

    global_defs: dict[str, Any] = {}
    local_vars: dict[str, Any] = {}
    exec("from magic2 import *", global_defs, local_vars)
    exec(source, global_defs, local_vars)
    return local_vars["spells"]


def main():
    s = get_spells("world_spells")
    print(s)
    m = get_spells("malicious_spells")
    print(m)


if __name__ == "__main__":
    main()
