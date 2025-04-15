import ast


CHECK_REGISTRY = {}

def register_check(check_cls):
    check = check_cls()

    if check.parser_ttype not in CHECK_REGISTRY:
        CHECK_REGISTRY.update({check.parser_ttype: []})
    CHECK_REGISTRY[check.parser_ttype].append(check)


class BaseCheck():
    ttype = None
    parser_ttype = None

    version_from = None
    version_to = None

    keywords = None
    message = None

    def unmet_version(self, version_from, version_to):
        return (self.version_from and self.version_from > version_to) or\
          (self.version_to and self.version_to < version_from)

