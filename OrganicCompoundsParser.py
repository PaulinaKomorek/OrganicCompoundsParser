class OrganicCompoundsParser(object):
    name: str
    radicals = ["meth", "eth", "prop", "but",   "pent",  "hex",  "hept",  "oct",  "non",  "dec",  "undec",
                "dodec",  "tridec",  "tetradec",  "pentadec",  "hexadec",  "heptadec",  "octadec",  "nonadec"]
    mutlipliers = ["di",  "tri",  "tetra", "penta", "hexa", "hepta", "octa", "nona", "deca", "undeca",
                   "dodeca", "trideca", "tetradeca", "pentadeca", "hexadeca", "heptadeca", "octadeca", "nonadeca"]

    suffixes = {"ane": lambda c: {"C":c, "H":2*c+2} , "benzene": lambda c: {"C": 6, "H": 12}, "ene": lambda c: {"C":c, "H":2*c}, "yne": lambda c: {"C":c, "H":2*c-2}, "yl": lambda c: {"C": c, "H":2*c+1}, "anol": lambda c:{"C":c, "H":2*c+2, "O":1}}
    cyclosuffixes = {"ane": lambda c: {"C":c, "H":2*c} , "ene": lambda c: {"C":c, "H":2*c-4}, "yne": lambda c: {"C":c, "H":2*c-8}, "yl": lambda c: {"C": c, "H":2*c-1}, "anol": lambda c:{"C":c, "H":2*c, "O":1}}
    
    def __init__(self, name):
        self.name = name

    def parse(self):
        chain=self.name.split("yl")
        main_chain=chain[-1]
        self.name="yl".join(chain[0:-1])+"yl"
        name_fragments=[]
        if len(chain)>1:
            for x in self.mutlipliers:
                self.name = self.name.replace(x, "")
            elements=self.name.split("-")
            for i in range(0, len(elements), 2):
                group_type=elements[i+1]
                for j in range(0, len(elements[i].split(","))):
                    name_fragments.append(group_type)
        name_fragments.append(main_chain)
        sum=list(map(lambda x: self.parse_element(x), name_fragments))
        output={"C":0, "H":0, "O":0}
        for i in sum:
            output["C"]=output["C"]+i["C"]
            output["H"]=output["H"]+i["H"]
            output["O"]=output["O"]+i.get("O", 0)
        if output["O"]==0:
            output.pop("O", None)
        output["H"]= output["H"]-(len(name_fragments)-1)
        return output
        


    def parse_element(self, name):
        sufix=""
        for i in self.suffixes:
            if name.endswith(i):
                sufix=i
                break

        for i in range(0, len(self.radicals)):
            if self.radicals[i]+sufix==name:
                return self.suffixes[sufix](i+1)
            elif "cyclo" + self.radicals[i]+sufix==name:
                return self.cyclosuffixes[sufix](i+1)
        return self.suffixes[sufix](0)
