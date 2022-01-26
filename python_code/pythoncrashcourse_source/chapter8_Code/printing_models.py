# Start with some designs that need to be printed.
#unprinted_designed = ['phone case', 'robot peendant', 'dodecahedron']
#completed_models = []

#Simulate printing each design, until none are left
#Move each design to completed_models after printing
#while unprinted_designed:
    #current_design = unprinted_designed.pop()
    #print(f"Printing model: {current_design}")
    #completed_models.append(current_design)

# Display all completed models.
#print("\nThe following models have been printed:")
#for completed_model in completed_models:
    #print(completed_model)

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each desgin, until none are left.
    Move each desgin to completed_models after printing
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designed = ['phone case', 'robot peendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designed[:],completed_models)
show_completed_models(completed_models)