#Find the halogen/H MMPs
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import numpy as np

df = pd.read_csv("./halide.csv")
smiles = df["smiles"]
logS1 = df["logS"]
print(len(smiles))
el = pd.read_csv("./non-halide.csv")
else_smiles = el["smiles"]
logS2 = el["logS"]
print(len(else_smiles))

#Remove halogen and standardize its smiles format
results = []
patt=Chem.MolFromSmarts('[F,Cl,Br,I]')
for m in range(len(smiles)):
    mol = Chem.MolFromSmiles(smiles[m])
    rm = Chem.DeleteSubstructs(mol, patt)
    rm = Chem.MolToSmiles(rm)
    smi1 = Chem.CanonSmiles(rm)
#Text comparison smiles, if they are the same, save them
    for n in range(len(else_smiles)):
        smi2 = else_canon[n]
        if smi1 == smi2:
            results.append([smiles[m], logS1[m], else_smiles[n], logS2[n]])
print(results)
r = np.array(results)
df = pd.DataFrame(r)
df.to_csv('halogen-H_MMPs.csv')
