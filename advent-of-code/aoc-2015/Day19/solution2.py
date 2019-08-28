molecule = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'

replacements = list()

for line in open('puzzle_input.txt', encoding='utf-8'):
    if ' => ' in line:
        split_line = line.split(' => ')
        replacements.append((split_line[-1].rstrip(), split_line[0]))
steps = 0
while molecule != 'e':
    for replacement in replacements:
        if replacement[0] in molecule:
            print('Replacing every', replacement[0], 'with', replacement[1] + '.',
                  'Current step:', str(steps) + '.', 'Molecule len:', len(molecule))
            print(molecule, end=' ==> ')
            steps += molecule.count(replacement[0])
            molecule = molecule.replace(replacement[0], replacement[1])
            print(molecule)
print('Total steps:', steps)
