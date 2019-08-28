def replacing(repl1, repl2):
    molecule = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'
    molecule_split = molecule.split(repl1)
    molecule_set = set()
    for i in range(1, len(molecule_split)):
        molecule = repl1.join(molecule_split[:i]) + repl2 + repl1.join(molecule_split[i:])
        molecule_set.add(molecule)
    return molecule_set


replacements = list()
unique_replacements = set()

for line in open('puzzle_input.txt', encoding='utf-8'):
    if ' => ' in line:
        split_line = line.split(' => ')
        replacements.append((split_line[0], split_line[-1].rstrip()))

for replacement in replacements:
    unique_replacements.update(replacing(*replacement))
print(len(unique_replacements))
