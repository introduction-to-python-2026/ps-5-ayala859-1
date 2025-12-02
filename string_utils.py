


def split_before_uppercases(formula):
    start = 0
    split_formula = []
    
    for end in range(1, len(formula)):
        if formula[end].isupper():     
            x = formula[start:end]     
            split_formula.append(x)
            start = end                
    
    if formula != "":
        split_formula.append(formula[start:])
        return split_formula
    else:
        return []
        
def split_at_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1
    if digit_location == len(formula):
        return (formula, 1)
    else:
        perfix = formula[:digit_location]
        numeric = int(formula[digit_location:])
        return (perfix, numeric)
def count_atoms_in_molecule(molecular_formula):

    atom_counts = {}
    list=split_before_uppercases(molecular_formula)
    for atom in list:
        atom_name, atom_count = split_at_digit(atom)
        

        atom_counts[atom_name] = atom_count
    

    return atom_counts


def parse_chemical_reaction(reaction_equation):
    """Takes a reaction equation (string) and returns reactants and products as lists.  
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])"""
    reaction_equation = reaction_equation.replace(" ", "")  # Remove spaces for easier parsing
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """Takes a list of molecular formulas and returns a list of atom count dictionaries.  
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]"""
    molecules_atoms_count = []
    for molecule in molecules_list:
        molecules_atoms_count.append(count_atoms_in_molecule(molecule))
    return molecules_atoms_count
