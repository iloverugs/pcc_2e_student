# import function imports module
# from module_name import function_name for specific function in module
# "as" used for giving alias to function or a module
# from module_name import function_name as fn
# import module_name as mn
# "*" used to import every function in module- be careful with larger modules
# from module_name import *

# import pizza as p
#from pizza import make_pizza as mp
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')