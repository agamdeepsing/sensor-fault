from setuptools import find_packages,setup

from typing import List

REQUIREMENT_FILENAME = "requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILENAME) as requirement_file:
        reqirements_list = requirement_file.readlines()
    reqirements_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list



setup(
    name= "sensor",
    version= "0.0.1",
    author= "agamdeep",
    author_email= "agamdeep8467@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()
)