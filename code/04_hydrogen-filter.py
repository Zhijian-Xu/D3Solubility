#Filter out hydrogen-containing compounds
import rdkit
from rdkit import Chem
import pandas as pd
import numpy as np

#read file
df = pd.read_csv("./halide.csv")  #Use non-halide.csv to find non-halogen compounds containing H
smiles = df["smiles"]
logS = df["logS"]
print(len(smiles))
#Find the compounds containing hydrogen
filter_results = []
el = []
patt = Chem.MolFromSmarts('[H]')                   
for n in range(len(smiles)):
    mol = Chem.MolFromSmiles(smiles[n])
    mol = Chem.AddHs(mol)
    f = mol.HasSubstructMatch(patt)                     
    if f:
        filter_results.append([smiles[n], logS[n]])     
    else:
        el.append([smiles[n], logS[n]])
print(len(filter_results))
print(len(el))
#Store in csv format
r = np.array(filter_results)
df = pd.DataFrame(r)
df.to_csv('halide_hydrogen.csv')

e = np.array(el)
df = pd.DataFrame(e)
df.to_csv('halide_no-hydrogen.csv')

