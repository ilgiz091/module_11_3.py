import sys
def introspection_info(obj):
    info = {}
    info["type"] = type(obj)
    info["module"] = getattr(obj, "__module__", None)

    try:
        info["attributes"] = [attr for attr in dir(obj) if not attr.startswith("__")]
    except TypeError:  # Некоторые объекты не поддерживают dir()
        info["attributes"] = "Недоступно"

    try:
        methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
        info["methods"] = methods
    except TypeError:
        info["methods"] = "Недоступно"


    # Дополнительная информация в зависимости от типа объекта
    if isinstance(obj, (int, float, complex)):
        info["value"] = obj
    elif isinstance(obj, str):
        info["length"] = len(obj)
    elif isinstance(obj, list):
        info["length"] = len(obj)
    elif isinstance(obj, dict):
        info["length"] = len(obj)

    return info

# Примеры использования
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello, world!")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)

dict_info = introspection_info({"a": 1, "b": 2})
print(dict_info)

class MyClass:
  """Это класс для тестирования"""
  def my_method(self):
    pass

class_info = introspection_info(MyClass)
print(class_info)

instance_info = introspection_info(MyClass())
print(instance_info)

none_info = introspection_info(None)
print(none_info)
