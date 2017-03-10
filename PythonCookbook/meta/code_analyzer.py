# -*- encoding: utf-8 -*-
import ast


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)

        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)

        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


