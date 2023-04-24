from distutils.util import strtobool

# пример строки, которую нужно преобразовать в булево значение
input_string = "yes"

# вызов функции strtobool для преобразования строки в булево значение
# boolean_value = strtobool(input_string)

boolean_value = bool(strtobool(input_string))
# вывод результата
print(boolean_value)
