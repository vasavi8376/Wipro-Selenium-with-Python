import xml.etree.ElementTree as ET

#read xml file

#parse xml file
tree = ET.parse("C:\Users\vasav\PycharmProjects\PythonAdvancedProgramming\filehandling\XMLhandling.py")
root = tree.getroot()

#fisrt child
print(root[0].tag)
print(root[1].tag)

#get the attribute
print(root[0].attrib)

#fetch all the attributes
for employee in root.findall("employee"):
    emp_id= employee.get("id")
    print(emp_id)

for emp in root.findall("employee"):
    name= emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name, role, exp)

#root--->child notes--->attributes of the child notes--->text of the child notes

#create the child notes
#create the root element
root = ET.Element("employees")

#create the child elements
emp1 = ET.SubElement(root, "employee",id="101")
ET.SubElement(emp1,"name").text= "Harsha"
ET.SubElement(emp1,"role").text= "Tester"
ET.SubElement(emp1,"name").text= "5"

emp2 = ET.SubElement(root, "employee",id="102")
ET.SubElement(emp1,"name").text= "Amit"
ET.SubElement(emp1,"role").text= "Developer"
ET.SubElement(emp1,"name").text= "3"

#
tree=ET.ElementTree(root)
tree.write("C:\Users\vasav\PycharmProjects\PythonAdvancedProgramming\Dataformats\writexml.xml",encoding="UTF-8",xml_declaration=True)


#updating the xml
tree = ET.parse("C:\Users\vasav\PycharmProjects\PythonAdvancedProgramming\Dataformats\updatexml.xml")
root = tree.getroot()

for emp in root.findall("employee"):
    if emp.get ("id")=="101":
        emp.find("experience").text = "16"


ET.indent(tree, space="    ",level=0)

tree.write("C:\Users\vasav\PycharmProjects\PythonAdvancedProgramming\Dataformats\updatexml.xml",encoding="UTF-8",xml_declaration=True)