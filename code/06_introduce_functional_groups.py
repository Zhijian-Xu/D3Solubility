#Find functional groups/H MMPs
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import numpy as np

df = pd.read_csv("../total_else_hydrogen.csv") 
smiles = df["smiles"]
logS = df["logS"]
print(len(smiles))

#Standardize SMILEs and find functional group/H pairs
canon = []
for x in smiles:
    smi = Chem.CanonSmiles(x)
    canon.append(smi)
results = []
patt = Chem.MolFromSmarts('[H]')
repl = Chem.MolFromSmiles('O')
for m in range(len(smiles)):
    mol = Chem.MolFromSmiles(smiles[m])
    mol = Chem.AddHs(mol)
    f = mol.HasSubstructMatch(patt)
    if f:
        rpl = AllChem.ReplaceSubstructs(mol, patt, repl, replacementConnectionPoint=0)
        for i in range(len(rpl)):
            smi = Chem.RemoveHs(rpl[i])
            smi = Chem.MolToSmiles(smi)
            try:
                smi1 = Chem.CanonSmiles(smi)
            except:
                print(smiles[m])
#Text comparison smiles, if they are the same, save them
            for n in range(len(smiles)):
                smi2 = canon[n]
                if smi1 == smi2:
                    results.append([smiles[m], logS[m], smiles[n], logS[n]])

r = np.array(results)
df = pd.DataFrame(r)
df.to_csv('H_OH.csv')
