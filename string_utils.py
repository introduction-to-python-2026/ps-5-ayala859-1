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
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' → {'H': 2, 'O': 1}"""
    atom_counts = {}
    list=split_before_uppercases(molecular_formula)
    for atom in list:
        atom_name, atom_count = split_at_digit(atom)
        if atom_name in atom_counts:
            atom_counts[atom_name] += atom_count
        else:
            atom_counts[atom_name] = atom_count
    

    return atom_counts

    # Step 1: Initialize an empty dictionary to store atom counts

        # Step 2: Update the dictionary with the atom name and count

    # Step 3: Return the completed dictionary
