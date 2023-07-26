"""def fun(*args, **kwargs):
    tuple_my = tuple(arg for arg in args)
    dict_my = {key: value for key, value in kwargs.items()}
    return (tuple_my, dict_my)


res = fun(
    1,
    2,
    3,
    4.2,
    "Python",
    [5, 6, 7],
    None,
    ("Hello", 25),
    name="Anna",
    age=30,
    cite="Kharkiv",
    country="Ukraine",
)
print(f"args: {res[0]}, \nkwargs: {res[1]}")
"""

"""
x = [i*++i for i in range(5)]
print(x)
"""
"""
from django.utils.translation import gettext as _

month = _("April")
day = "14"
output = _("Today is %(month)s %(day)s") % {"month": month, "day": day}
print(output)
"""
