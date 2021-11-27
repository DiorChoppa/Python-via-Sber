#Проверка на возможность импорта модуля осуществляется следующим образом:

import importlib.util as util
def check_module(module_name):
    module_spec = util.find_spec(module_name)
    if module_spec is not None:
        print("Module: {} could be imported!".format(module_name))
        return module_spec

def import_module_from_spec(module_spec):
    module = util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    return module

if __name__ == '__main__':
    module_spec = check_module('collections')
    if module_spec:
        module = import_module_from_spec(module_spec)
        print(dir(module))

"""Если, используя importlib.import_module, на вход мы передавали строку, то тут мы сначала, используя importlib.util.find_spec, пробуем найти спецификацию модуля, а затем, если она найдена, используя importlib.util.module_from_spec, загружаем модуль и в module_spec.loader.exec_module исполняем его.

Так же importlib поддерживает загрузку спецификации модуля по пути и имени.

module_spec = importlib.util.spec_from_file_location(
    module_name, module_file_path
)

"""