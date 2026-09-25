# Open-Closed Principle states that : software parts like classes, modules, and functions 
# should be open for new features, but closed for changing old code.

# Example
# Imagine we wrote a payment system , tomorrow we want to add a new payment method
# if we modify existing class or methods we risk breaking old functionality
# so we design a system in a way such that we add new code without touching the old one

class PaymentProcessor:
    def pay(self , amount):
        raise NotImplementedError("Subclass must implement this method")
    
class CreditCardPayment(PaymentProcessor):
    def pay(self , amount):
        print(f'Paid {amount} using Credit Card')
        
class PayPalPayment(PaymentProcessor):
    def pay(self , amount):
        print(f'Paid {amount} using PayPal')    
        
class UPIPayment(PaymentProcessor):
    def pay(self , amount):
        print(f'Paid {amount} using UPI')
        
def complete_payment(payment_method , amount):
    payment_method.pay(amount)
    
complete_payment(CreditCardPayment() , 1000)
complete_payment(PayPalPayment() , 400)
complete_payment(UPIPayment() , 450)