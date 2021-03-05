# Given an api which returns an array of chemical names and an array of chemical symbols, display the chemical names with their symbol surrounded by square brackets:



chemical_names= ['Amazon', 'Microsoft', 'Google']
 chemical_names = ['I', 'Am', 'cro', 'le', 'abc']

def match_symbol(chemical_names, chemical_symbols):
    import re
    combined = []
    
    for s in chemical_symbols:
        for c in chemical_names:
            r = re.search(s, c)
            if r:
                combined.append(re.sub(s, "[{}]".format(s), c))

    return combined		    
    

print match_symbol(chemical_names, chemical_names)
