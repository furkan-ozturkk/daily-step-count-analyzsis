import xml.etree.ElementTree as ET
import json
import os

xml_file = "C:/Users/furka/Desktop/DSA/expo.xml"

try:
    # read the xml file
    with open(xml_file, "r", encoding="utf-8") as file:
        content = file.read()
    
    tree = ET.ElementTree(ET.fromstring(content))
    root = tree.getroot()

    step_data = []

    for record in root.findall("Record"):
        if record.attrib.get("type") == "HKQuantityTypeIdentifierStepCount":
            step_data.append({
                "startDate": record.attrib.get("startDate"),
                "endDate": record.attrib.get("endDate"),
                "value": record.attrib.get("value")
            })

    # find the adress of the xml
    output_directory = os.path.dirname(xml_file)
    json_file = os.path.join(output_directory, "step_count_data.json")
    
    # JSON to same location
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(step_data, f, indent=4)

    print(f"Veriler başarıyla '{json_file}' dosyasına kaydedildi.")

except FileNotFoundError:
    print(f"Error: '{xml_file}' file couldn't found.")
except ET.ParseError as e:
    print(f"Error: XML file has a problem: {e}")
except Exception as e:
    print(f"Unknown error: {e}")




