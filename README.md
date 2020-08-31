# OrganicCompoundsParser
### description
Application which counts the number of carbon, oxygen and hydrogen athoms in selected organic compounds. 
Currently application supports:
- alkanes, alkened, alkynes
- alcohols
- cycles and aromatic
### installation
`wget https://raw.githubusercontent.com/PaulinaKomorek/OrganicCompoundsParser/master/OrganicCompoundsParser.py`
### sample usage
```python
from OrganicCompoundsParser import OrganicCompoundsParser

test=OrganicCompoundsParser("benzene")
print(test.parse())
```
