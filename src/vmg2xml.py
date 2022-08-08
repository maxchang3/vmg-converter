from typing import List
from xml.etree import ElementTree as ET
try:
    from src.vmg import VMG
except:
    from vmg import VMG


def vmg2xml(vmg_list: List, filepath: str) -> None:
    ele = ET.Element("smses", {"count": str(len(vmg_list))})
    status = {
        "DELIVER": "1",
        "SUBMIT": "2",
    }
    for vmg in vmg_list:
        son = ele.makeelement("sms", {
            "protocol": "0",
            "address": vmg['VCARD']['TEL'],
            "date": vmg['VENV']['VBODY']['Date'],
            "type": status[vmg['X-MESSAGE-TYPE']],
            "body": vmg['VENV']['VBODY']['text']
        })
        ele.append(son)
    tree = ET.ElementTree(ele)
    try:
        ET.indent(tree, space="\t", level=0)
    except:
        print("Indent error, ET.indent only for python3.9+, but it *won't* affect use.")
    tree.write(filepath, encoding='utf-8', xml_declaration=True, short_empty_elements=False )
