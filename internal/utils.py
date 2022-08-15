import os
from datetime import datetime
import uuid
from lxml import etree
import lxml.etree as le
from settings import feature_files_dir, keywords_dir
import glob


def get_feature_files():
    try:
        os.chdir(feature_files_dir)
        return glob.glob("*.feature")

    except Exception as e:
        raise Exception(e.args[0])


def get_robot_files():
    try:
        os.chdir(keywords_dir)
        return glob.glob("*.robot")

    except Exception as e:
        raise Exception(e.args[0])


def find_variables(string):
    """
        Variables in string are between '<' '>'
    """

    variables = []

    try:
        splited_string = string.split("<")
        if len(splited_string) > 1:
            splited_string.remove(splited_string[0])

            counter = 0
            while counter < len(splited_string):
                index = splited_string[counter].find('>')
                if index > -1:
                    splited_string[counter] = splited_string[counter][:index]
                counter += 1
            variables = splited_string
    except Exception as e:
        raise Exception(e.args[0])

    return variables


def create_folder(report_dir):
    """
        :param report_dir: directory where folder will be created
    """

    try:
        folder_dir = os.path.join(
        report_dir,
        "run_" + datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + str(uuid.uuid4()).upper())

        os.makedirs(folder_dir)

    except Exception as e:
        raise Exception(e.args[0])

    return folder_dir.replace("\\", "/")


def remove_warnings(file_dir):
    """
       Func to remove error block from xml file
       :param file_dir: report xml file
    """
    try:
        with open(file_dir, 'r+', encoding="utf-8") as xml_file:
            doc = le.parse(xml_file)

            for elem in doc.xpath('//errors/msg[@level="WARN"]'):
                parent = elem.getparent()
                parent.remove(elem)

            xml_file.truncate(0)
            xml_file.seek(0)
            xml_file.write(etree.tostring(doc, pretty_print=True).decode())
    except Exception as e:
        raise Exception(e.args[0])
