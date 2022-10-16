from setuptools import setup
from typing import List,OrderedDict


#Deckaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Vinayak Gaikar"
DESCRIPTION="This is the first FSDS Nov batch Machine Learning Project"
PACKAGES=["housing"]
REQUIREMENT_FILEE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirenents.txt file

    return This function is going to return a list which contain name of 
    libraries mentioned in requirments.txt file

    """


    with open(REQUIREMENT_FILEE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()

)



