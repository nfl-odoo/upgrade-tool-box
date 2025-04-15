import ast
import os

from .base import BaseParser
from checks.base.base import CHECK_REGISTRY


class AstParser(BaseParser):
    def __init__(self, path, version_from, version_to):
        super().__init__(path, version_from, version_to)
        self.ttype = 'ast'

    def get_extensions(self):
        return ['py']

    def parse_file(self, file_path):
        source = self.read_file(file_path)
        if source is None:
            return None

        try:
            return ast.parse(source), self.path
        except SyntaxError:
            return None

    def process(self):
        all_results = []

        for file_path in self.get_files():
            parsed = self.parse_file(file_path)
            if parsed is None:
                continue

            tree, filename = parsed
            for check in CHECK_REGISTRY.get(self.ttype, []):
                if check.unmet_version(self.version_from, self.version_to):
                    continue

                results = check.process(tree, file_path)
                all_results.extend(results)

        return all_results
