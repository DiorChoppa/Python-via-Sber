import importlib

def dynamic_import(module):
    return importlib.import_module(module)

if __name__ == '__main__':
    module = dynamic_import('foo')
    module.main()