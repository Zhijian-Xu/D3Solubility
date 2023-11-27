#Filter the data set for compounds containing halogens and store them in csv format
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import pandas as pd
import numpy as np
df = pd.read_csv("./D3Solubility-data.csv")  #change the dataset to your own dataset
smiles = df['smiles']                                  
logS = df["logS"]
print(len(smiles))

filter_results = []
el = []
patt=Chem.MolFromSmarts('[F,Cl,Br,I]')
for n in range(len(smiles)):
    mol = Chem.MolFromSmiles(smiles[n])
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
df.to_csv('halide.csv')

e = np.array(el)
df = pd.DataFrame(e)
df.to_csv('non-halide.csv')

