import os
import xml.etree.ElementTree as ET

from .base import BaseParser
from checks.base.base import CHECK_REGISTRY


class EtreeParser(BaseParser):
    def __init__(self, path, version_from, version_to):
        super().__init__(path, version_from, version_to)
        self.ttype = 'etree'

    def get_extensions(self):
        return ['xml']

    def parse_file(self, file_path):
        source = self.read_file(file_path)
        if source is None:
            return None

        try:
            return source, file_path
        except ET.ParseError:
            return None

    def process(self):
        all_results = []

        for file_path in self.get_files():
            parsed = self.parse_file(file_path)
            if parsed is None:
                continue

            xml_string, filename = parsed
            for check in CHECK_REGISTRY.get(self.ttype, []):
                if check.unmet_version(self.version_from, self.version_to):
                    continue

                results = check.process(xml_string, filename)
                all_results.extend(results)

        return all_results
