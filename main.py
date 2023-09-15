import xml.etree.ElementTree as ET
from Edge import Edge
from Vertex import Vertex
import os
import json
import api_caller
import master_configuration_provider

edges = []
nodes = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def loadxml():
    tree = ET.parse("d:\\trash\\Transfers.drawio.xml")
    mxfile = tree.getroot();
    #print(mxfile.tag);
    root = mxfile[0][0][0]
    #print(mxfile[0][0][0].tag)
    for element in root.iter('object'):
        if 'edge' in element[0].attrib:
            #print(element.attrib["TransferDay"])
            #print(element.attrib["Value"])
            #print(element.attrib["Value"])
            edge = Edge(element.attrib["TransferDay"],element.attrib["Value"], element[0].attrib["source"], element[0].attrib["target"])
            edges.append(edge)
            #print(element.attrib)
            #print("edge")

        if 'vertex' in element[0].attrib:
            vertex=Vertex(element.attrib["Name"],10,element.attrib["id"])
            nodes.append(vertex)
            #vertexes.append(vertex)
            #print("element")
            #print(element.tag, element.attrib)

def build_dependency_recursive_nodes(edge):
    for node in nodes:
        if node.id==edge.target:
            edge.add_node(node)

def build_dependency_recursive_edges(node):
    for edge in edges:
        if edge.source == node.id:
            node.add_edge(edge)
            build_dependency_recursive_nodes(edge)
            #print("source found")
    return node


def build_dependency_from_root(name):
    root=[element for element in nodes if element.name == name]
    #print('rootname')
    if len(root)>1:
        raise Exception("Two nodes with the same name")
    sourceNode=root[0]
    result=build_dependency_recursive_edges(sourceNode)
    return result


def print_transfer_for_edge(vertex):
    sum=0
    for edge in vertex.edges:
        sum+=edge.value
        print(f'{edge.targetNode.name:30} {edge.value:10}')
    print(sum)
    print("========")


def process_for_category(category):
    node = build_dependency_from_root(category)
    print_transfer_for_edge(node)

def get_categories():
    categories=master_configuration_provider.get_master_configuration_value("TransfersCategories")
    return categories;

    #categories=data["TransfersCategories"]
    #print(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loadxml()
    categories=get_categories();
    categories_array=categories.split(',');
    for category in categories_array:
        print(category)
        process_for_category(category)
    #process_for_category("Pensja")
    #print("============")
    #process_for_category("ProxyKomorska")
    #print("============")
    #process_for_category("ProxyKameralne")

    api_caller.print_hi('lololol')
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
