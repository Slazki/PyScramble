import ast
import random
import string
import base64
import argparse

class Obfuscator(ast.NodeTransformer):
    def __init__(self, encrypt_strings=False, inject_dummy=False):
        self.mapping = {}
        self.encrypt_strings = encrypt_strings
        self.inject_dummy = inject_dummy
        self.decryption_func_added = False
        self.decryption_func_name = self._get_random_name()

    def _get_random_name(self, length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))

    def _xor_encrypt(self, text, key="secret"):
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))

    def _encode_string(self, s):
        encrypted = self._xor_encrypt(s)
        return base64.b64encode(encrypted.encode()).decode()

    def visit_FunctionDef(self, node):
        new_name = self._get_random_name()
        self.mapping[node.name] = new_name
        node.name = new_name
        self.generic_visit(node)
        if self.inject_dummy:
            dummy = ast.parse("for _ in range(0): pass").body[0]
            node.body.insert(0, dummy)
        return node

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load) and node.id in self.mapping:
            node.id = self.mapping[node.id]
        elif isinstance(node.ctx, ast.Store):
            if node.id not in self.mapping:
                self.mapping[node.id] = self._get_random_name()
            node.id = self.mapping[node.id]
        return node

    def visit_Constant(self, node):
        if self.encrypt_strings and isinstance(node.value, str):
            # Don't encrypt f-strings (JoinedStr will call this)
            if hasattr(node, 'parent') and isinstance(node.parent, ast.JoinedStr):
                return node
            encoded = self._encode_string(node.value)
            call = ast.Call(
                func=ast.Name(id=self.decryption_func_name, ctx=ast.Load()),
                args=[ast.Constant(value=encoded)],
                keywords=[]
            )
            return ast.copy_location(call, node)
        return node

    def visit_JoinedStr(self, node):
        for value in node.values:
            if isinstance(value, ast.Constant):
                value.parent = node
        return self.generic_visit(node)

    def add_decryption_function(self):
        if not self.encrypt_strings or self.decryption_func_added:
            return []
        self.decryption_func_added = True
        decryption_code = f"""
import base64
def {self.decryption_func_name}(s):
    raw = base64.b64decode(s).decode()
    return ''.join(chr(ord(c) ^ ord("secret"[i % len("secret")])) for i, c in enumerate(raw))
"""
        return ast.parse(decryption_code).body

def obfuscate_file(input_file, output_file, encrypt_strings=False, inject_dummy=False):
    with open(input_file, 'r') as f:
        source = f.read()

    tree = ast.parse(source)

    # Set parent attributes manually
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node

    obfuscator = Obfuscator(encrypt_strings=encrypt_strings, inject_dummy=inject_dummy)
    tree = obfuscator.visit(tree)
    ast.fix_missing_locations(tree)

    if encrypt_strings:
        decrypt_nodes = obfuscator.add_decryption_function()
        tree.body = decrypt_nodes + tree.body

    try:
        obfuscated_code = ast.unparse(tree)
    except AttributeError:
        import astor
        obfuscated_code = astor.to_source(tree)

    with open(output_file, 'w') as f:
        f.write(obfuscated_code)

    print(f"Obfuscated code saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description="PyScramble Obfuscator")
    parser.add_argument('--input', required=True, help='Input Python file')
    parser.add_argument('--output', required=True, help='Output obfuscated file')
    parser.add_argument('--encrypt-strings', action='store_true', help='Encrypt string literals')
    parser.add_argument('--inject-dummy', action='store_true', help='Inject dummy code')
    args = parser.parse_args()

    obfuscate_file(args.input, args.output, args.encrypt_strings, args.inject_dummy)

if __name__ == '__main__':
    main()
