# We try to extract data from xml or json.
# To achieve that, factory function is used.
# It returns extractor based on the extension of the file.

import json
import xml.etree.ElementTree as etree


# json extractor class
class JSONDataExtractor:
    def __init__(self, filepath: str):
        with open(filepath, 'r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self) -> dict:
        return self.data


# xml extractor class
class XMLDataExtractor:
    def __init__(self, filepath: str):
        self.tree = etree.parse(filepath)


# factory function
def dataextraction_factory(filepath: str):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError(f'Unsupported extraction format of file [{filepath}].')
    return extractor(filepath)


# === TESTS ===

def test_json():
    json_extractor = dataextraction_factory("assets/book.json")
    json_data = json_extractor.parsed_data
    assert len(json_data.items()) == 3
    assert json_data["name"] == "The Hitchhiker's Guide to the Galaxy"
    assert json_data["author"] == "Douglas Adams"
    assert json_data["year"] == 1979


def test_xml():
    xml_extractor = dataextraction_factory("assets/book.xml")
    xml_data = xml_extractor.tree
    assert xml_data.find("name").text == "The Hitchhiker's Guide to the Galaxy"
    assert xml_data.find("author").text == "Douglas Adams"
    assert int(xml_data.find("year").text) == 1979
