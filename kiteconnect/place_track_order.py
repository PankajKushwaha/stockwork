

#               symbol , quantiy , ordertype , entry , sl, target , trigger 
order_list =[ 
                ["hcltech", 10 , "limit" , 1000 , 990, 1050 , None ], 
                ["wipro", 10 , "sl" , 550 , 540, 570 , 552 ] 
            ]


print (order_list)

def execute_order():
        for order in order_list:
            symbol,quantity,otype,entry,sl,target,trigger = order[0],order[1],order[2],order[3],order[4],order[5]

            if otype == "limit":
                print(otype)
            else if otype == "sl":
                print(otype)
                #if reject then add to list

     #launch new thread for pending order

def trail_sl():
    for order in kite.orders():
        # symbol , order_id , price , ltp
        if status == s_open:
        if is_modify_needed(price,ltp) == True:
            price = get_new_price(ltp)
            #modify order
        else
            continue


'''
def execute_order():


def per_profit():


def get_trail_sl_percent():


def get_new_sl():


def is_sl_skip():

def monitor_order():
'''
