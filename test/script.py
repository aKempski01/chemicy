import pandas as pd
import numpy as np
import re
import pubchempy as pcp
from rdkit import Chem
from rdkit.Chem import Draw
from PIL import Image
from matplotlib import pyplot as plt

c = pcp.Compound.from_cid(pcp.get_cids('919-30-2'))
print(c.molecular_formula)
print(c.atoms)
print(c.isomeric_smiles)
print(c.canonical_smiles)
# print(c.exact_mass)
# print(c.)
a = Chem.MolFromSmiles(c.isomeric_smiles)
img = Draw.MolToImage(a)
img = np.asarray(img)
print(img)
plt.imshow(img)
plt.show()