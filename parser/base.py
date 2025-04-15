import os


class BaseParser():
    def __init__(self, path, version_from, version_to):
        self.path = path
        self.version_from = version_from
        self.version_to = version_to
        self.ttype = None

    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return None

    def get_extensions(self):
        return []

    def get_files(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if any(file.endswith(extension) for extension in self.get_extensions()):
                    yield os.path.join(root, file)

    def process(self):
        return []

    def display(self, results):
        for result in results:
            print(result)
