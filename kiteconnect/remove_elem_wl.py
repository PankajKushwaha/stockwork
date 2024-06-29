import pickle

def save_list_to_file(list_name):
    with open("watchlist", 'wb') as handle:
        pickle.dump(list_name, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_list_from_file():
    with open("watchlist", 'rb') as handle:
        lst = pickle.load(handle)
        return lst

lst = load_list_from_file()
for i in lst:
    print(i)

lst.remove("NSE:POLYCAB")
#lst.append()

for i in lst:
    print(i)

save_list_to_file(lst)
