import xml.etree.ElementTree as ET

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def process_file():
    tree=ET.parse(".\Transfers.drawio.xml")
    mxfile=tree.getroot();
    print(mxfile.tag);
    root=mxfile[0][0][0]
    print(mxfile[0][0][0].tag)
    for element in root.iter('object'):
        if 'edge' in element[0].attrib:
            print("Laczenie")

        if 'vertex' in element[0].attrib:
            print("element")

        print(element.tag,element.attrib)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_file();
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
