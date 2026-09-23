# YAGNI - You Aren't gonna need it
# Means don't build features you don't need right now
# Implement only features what is required for current requirements - Not hypothetical future ones

## Without YAGNI
def compute_total_with_points(qty , unit_price , loyalty_points = False):
    sub = qty * unit_price
    tax = sub * 0.18
    total = sub + tax
    if loyalty_points:
        points = int(total // 10) # This is not needed now , just adding more complexity
        print(f'Loyalty Service : {points}')
    return total


## With YAGNI
def compute_total(qty , unit_price):
    sub = qty * unit_price
    tax = sub * 0.18
    return sub + tax


## Usage

t1 = compute_total(3 , 100)
t2 = compute_total(15 , 100)

print(f'Order 1 : {t1}')
print(f'Order 2 : {t2}')