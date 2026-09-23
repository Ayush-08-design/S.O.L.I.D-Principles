# DRY - Means avoid duplicating code or logic in a program


## Without DRY - Bad Way
def price_small_order(qty : int , unit_price : float):
    sub = qty * unit_price
    tax = sub * 0.18
    return sub + tax

def price_bulk_order(qty , unit_price):
    sub = qty * unit_price
    disc = sub * 0.05 if qty >= 10 else 0
    tax = (sub - disc) * 0.18
    return sub - disc + tax

## Wiht DRY - Good Way
def compute_total(qty , unit_price):
    sub = qty * unit_price
    disc = sub * 0.05 if qty >= 10 else 0
    tax = (sub - disc) * 0.18
    return sub , disc , tax , sub - disc + tax


## Usage

o1 = compute_total(3 , 100)
o2 = compute_total(15 , 100)

for sub , disc , tax , total in (o1 , o2):
    print(f'Subscribe = {sub:.2f} , Discount = {disc:.2f} , Tax = {tax:.2f} , Total = {total:.2f}')