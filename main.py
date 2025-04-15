from checks.base.base import CHECK_REGISTRY

import checks

from parser.ast import AstParser
from parser.etree import EtreeParser


def main(path):
    # TODO: get those from odoo sources passed in future arguments as paths.
    version_from, version_to = '15.0', '18.0'

    for parser in [
        AstParser(path, version_from, version_to),
        EtreeParser(path, version_from, version_to),
    ]:
        results = parser.process()
        parser.display(results)

if __name__ == '__main__':
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
