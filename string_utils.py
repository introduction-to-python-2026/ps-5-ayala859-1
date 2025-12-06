def split_before_uppercases(formula):
    if formula == "":
        return []

    start = 0
    split_formula = []

    for end in range(1, len(formula)):
        if formula[end].isupper():
            split_formula.append(formula[start:end])
            start = end

    split_formula.append(formula[start:])
    return split_formula


def split_at_digit(formula):
    digit_location = 1
    for char in formula[1:]:
        if char.isdigit():
            break
        digit_location += 1

    if digit_location == len(formula):
        return (formula, 1)
    else:
        prefix = formula[:digit_location]
        numeric = int(formula[digit_location:])
        return (prefix, numeric)

def count_atoms_in_molecule(molecular_formula):
    """Takes a molecular formula (string) and returns a dictionary of atom counts.
    Example: 'H2O' -> {'H': 2, 'O': 1}"""
    dict_atom_counts = {}
    list1 = split_before_uppercases(molecular_formula)
    print(list1)
    for item in list1:
        k = split_at_digit(item)
        dict_atom_counts[k[0]] = k[1]

    return dict_atom_counts


formula = "H2C"
print(count_atoms_in_molecule(formula))
