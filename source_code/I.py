# The Interface segregation principle (ISP) states that a client should not be forced 
# to depend on interfaces it does not use. Instead of creating one big interface 
# with many methods we should split it into smaller , more specific interfaces. 
# For example - If we create a machine interface with methods like , print() , scan() 
# , and fax() , then a simple printer would be forced to implement , scan() , 
# and fax() even if it dosen't support them. 
# ISP says : "Break large interfaces into smaller, role specific ones"


from abc import ABC , abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_doc(self , doc):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self , doc):
        pass

class SimplePrinter(Printer):
    def print_doc(self, doc):
        print(f'Printing : {doc}')
        
class MultiFunctionPrinter(Printer , Scanner):
    def print_doc(self, doc):
        print(f'Printing : {doc}')
        
    def scan_doc(self, doc):
        print(f'Scanning : {doc}')
        
## Usage

sp = SimplePrinter()
sp.print_doc('Report.pdf')

mfp = MultiFunctionPrinter()
mfp.print_doc('Invoice.pdf')

mfp.scan_doc('Contract.pdf')