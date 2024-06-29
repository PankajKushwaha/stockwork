from nsepython import *

def get_fno_list():
    lst=fnolist()
    lst.remove("NIFTYIT")
    lst.remove("IDEA")
    lst.remove("MCX")
    #lst.remove("MCX")
    return lst

def read_text_file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.rstrip('\n') for line in file]
        return lines
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

def create_watchlist():
    niftyfno = get_fno_list()
    watchlist = read_text_file_to_list("watchlist.txt")
    # Continue asking for input until "done" is entered
    while True:
        # Take input from the user
        user_input = input("Enter a search term (or 'done' to exit): ").lower()

        # Check if the user wants to exit
        if user_input == 'done':
            break

        # Traverse niftyfno and check if the user input is a substring of any list element (case-insensitive)
        for item in niftyfno:
            if user_input in item.lower():
                watchlist.append(item)
    
        # Print the current watchlist after each input
        print("Current Watchlist:", watchlist)
    return watchlist

def save_list_to_text_file(data_list, filename):
    try:
        with open(filename, 'w') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"List saved to {filename}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Print the final watchlist
watchlist =  create_watchlist()
print("Final Watchlist:", watchlist)
save_list_to_text_file(watchlist, 'watchlist.txt')

