import xml.etree.ElementTree as ET
from Edge import Edge
from Vertex import Vertex

edges = []
vertexes = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def loadxml():
    tree = ET.parse("d:\\trash\\Transfers.drawio")
    mxfile = tree.getroot();
    print(mxfile.tag);
    root = mxfile[0][0][0]
    print(mxfile[0][0][0].tag)
    for element in root.iter('object'):
        if 'edge' in element[0].attrib:
            #print(element.attrib["TransferDay"])
            #print(element.attrib["Value"])
            edge = Edge(element.attrib["TransferDay"],element.attrib["Value"], element[0].attrib["source"], element[0].attrib["target"])
            edges.append(edge)
            #print(element.attrib)
            #print("edge")

        if 'vertex' in element[0].attrib:
            vertex=Vertex(element.attrib["Name"],10,element.attrib["id"])
            vertexes.append(vertex)
            #vertexes.append(vertex)
            #print("element")
            print(element.tag, element.attrib)

def build_dependency_from_root(name):
    root=[element for element in vertexes if element.name == name]
    print(root)

def process_file():
    loadxml()
    print("amount of vertexes")
    print(len(vertexes))

    print("amount of edges")
    print(len(edges))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_file();
    build_dependency_from_root("Pensja")
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
