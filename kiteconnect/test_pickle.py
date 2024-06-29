import pickle

test = ['NFO:INDUSINDBK21NOV1100CE', 'NFO:CANBK21NOV230CE', 'NFO:TATAMOTORS21NOV520CE', 'NFO:APOLLOHOSP21NOV5200CE', 'NFO:TATACONSUM21NOV850CE', 'NFO:ICICIPRULI21NOV670CE', 'NFO:BHARATFORG21NOV800CE', 'NFO:RECLTD21NOV145CE', 'NFO:PAGEIND21NOV41000CE', 'NFO:PFC21NOV140CE']

def save_list_to_file(listname,filename):
    with open(filename, 'wb') as handle:
        pickle.dump(listname, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_list_from_file(filename):
    with open(filename, 'rb') as handle:
        lst = pickle.load(handle)
        return lst

#save_list_to_file(test,"pankaj.pkl")
print(load_list_from_file("bear_option_list.pkl"))

