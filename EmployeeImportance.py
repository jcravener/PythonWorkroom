
# LeetCode: 690. Employee Importance
class Employee:
    def __init__(self, id: int, importance: int, subordinates: [int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

def getImportance(employees: [Employee], id: int) -> int:
    
    imp = 0

    for e in employees:
        imp += e.importance
        if len(e.subordinates) > 0:
            imp += getImportance(e.subordinates, e.id)
        else:
            return imp

def importance(emp: Employee):
    return emp.importance



emp = [[Employee(1,5,[2,3]), Employee(2,3,[])], Employee(3,3,[])]

print(getImportance(emp, 1))

#print(getsubordinates(emp))