#tower-builder.py

# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
# Tower block is represented as *

def tower_builder(n_floors):
    list = []
    for i in range(n_floors):
        list.append('{}{}{}'.format((n_floors-1-i)*' ',((i+1)*2-1)*'*', (n_floors-1-i)*' '))
    
    return list