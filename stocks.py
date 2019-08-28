stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE":"German Emen"
}
purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

for purchase in purchases:
    purchase_amount = purchase[1]*purchase[3]
    for k, v in stockDict.items():
        if purchase[0] == k:
            print(f"I bought {v} stock for ${purchase_amount}")

for key in stockDict.keys():
    print(f"---{key}---")
    for purchase in purchases:
        if purchase[0] == key:
            print(purchase)