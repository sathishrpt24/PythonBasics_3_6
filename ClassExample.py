class ClassExample:
    def __init__(self,name,id):
        self.name =name;
        self.id = id;
    def showDetails(self):
        print("Name is "+self.name);
        print("Id of the student",self.id);


ce = ClassExample("Sathish",25);
ce.showDetails();
