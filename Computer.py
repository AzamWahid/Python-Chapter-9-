class Hardware():
    def __init__(self,name,installed_date):
        self.name = name
        self.installed_Date = installed_date

class Software():
    def __init__(self,software_name,version,installed_date):
        self.software_name = software_name
        self.version = version
        self.installed_date = installed_date



class Computer():
    def __init__(self,name,manufacture,location,hard= [],soft=[]):
        self.name = name
        self.manufacture = manufacture
        self.location = location
        self.hardware = []
        self.software = []

    def set_software(self,soft):
        self.software.append(soft)

    def set_hardware(self,hard):
        self.hardware.append(hard)

    def show_hardware(self):
        for hards in self.hardware:
            print(hards)

    def show_software(self):
        for softs in self.software:
            print(softs)

    def set_comp(self):
        print(self.name+self.manufacture,self.location)

comp = Computer('Dell','2015','usa',[],[])
comp.set_hardware(['harddisk','2018-01-12'])
comp.set_software(['adobe','2018-09-02'])
comp.show_hardware()
comp.show_software()
comp.set_comp()

