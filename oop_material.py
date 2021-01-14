molecule_name = "water molecule"
molecule_charge = 0.0
molecule_symbols = ['O', 'H', 'H']

molecule_name2 = 'He'
molecule_charge2 = 0.0
molecule_symbols2 = ['He']

class Molecule:
    def __init__(self, name, charge, symbols):
        self.name = name
        self.charge = charge
        self.symbols = symbols
        #self._num_atoms = len(symbols)

    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, symbols):
        self._symbols = symbols
        self._num_atoms = len(symbols)

    def my_algorithm(self, parameter_list):
        #first stage
        self._first_stage(parameter_list)
        #second stage
        self._second_stage(parameter_list)
        #third stage
        self._third_stage(parameter_list)
    
    def _first_stage(self, parameter_list):
        #performs the first stage of the algorithm
        print("First stage")

    def _second_stage(self, parameter_list):
        #performs the second stage of the algorithm
        print("Second stage")
    
    def _third_stage(self, parameter_list):
        #performs the third stage of the algorithm
        print("Third stage")

    def __str__(self):
        return f'name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}'

water_molecule = Molecule('water molecule', 0.0, ['O', 'H', 'H'])
he_molecule = Molecule('He', 0.0, ['He'])

print(water_molecule.symbols)
print(water_molecule._num_atoms)
#water_molecule.my_algorithm([1,2,3])
water_molecule.symbols = ['O', 'O', 'H', 'H']
print(water_molecule.symbols)
print(water_molecule._num_atoms)
#print(water_molecule)
#print(he_molecule)