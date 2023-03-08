from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
        
    return requirements


setup(
name="ML_Project",
version="0.0.1",
author="Pranay",
author_email="Pranaygurrapu88@gmail.com",
packages=find_packages(),
# install_requires=["pandas,numpy,seaborn"]
intall_requires=get_requirements("requirements.txt")
)