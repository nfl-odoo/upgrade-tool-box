import ast

from .base import BaseCheck


class AstCheck(BaseCheck):
    parser_ttype = 'ast'

    def get_decorator_name(self, node):
        if isinstance(node, ast.Call):
            return node.func.attr if isinstance(node.func, ast.Attribute) else node.func.id
        else:
            return node.attr if isinstance(node, ast.Attribute) else node.id

    def get_decorator_names(self, nodes):
        return [
            self.get_decorator_name(node)
            for node in nodes
        ]

    def node_filter(self, node):
        if self.ttype == 'decorator':
            return isinstance(node, ast.FunctionDef) and node.name == self.keywords['name'] and self.keywords['decorator'] in self.get_decorator_names(node.decorator_list)
        if self.ttype == 'function':
            return isinstance(node, ast.FunctionDef) and node.name == self.keywords['name']

    def get_nodes(self, tree):
        return filter(self.node_filter, ast.walk(tree))

    def process(self, tree, filename):
        return [
            {
                'type': self.ttype,
                'message': self.message,
                'filename': filename,
                'name': node.name,
            }
            for node in self.get_nodes(tree)
        ]


