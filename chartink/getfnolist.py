from nsepython import *

def get_fno_list():
    lst=fnolist()
    lst.remove("NIFTYIT")
    lst.remove("IDEA")
    lst.remove("MCX")
    return lst

print(get_fno_list())


