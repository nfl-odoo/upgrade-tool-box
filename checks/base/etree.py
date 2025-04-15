import xml.etree.ElementTree as ET

from .base import BaseCheck


class EtreeCheck(BaseCheck):
    parser_ttype = 'etree'

    def node_filter(self, elem):
        if self.ttype == 'tag':
            return elem.tag == self.keywords.get('tag')
        elif self.ttype == 'attribute':
            attr_name = self.keywords.get('attribute')
            attr_value = self.keywords.get('value')
            return attr_name in elem.attrib and elem.attrib[attr_name] == attr_value
        return False

    def get_nodes(self, root):
        return filter(self.node_filter, root.iter())

    def process(self, xml_string, filename):
        root = ET.fromstring(xml_string)
        return [
            {
                'type': self.ttype,
                'message': self.message,
                'filename': filename,
                'tag': elem.tag,
                'attributes': elem.attrib
            }
            for elem in self.get_nodes(root)
        ]
