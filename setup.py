'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more

find_packages--this function will scan through all the folders and when there is __init__ file 
it will consider that folder as a package
-e . -- it is going to refer the setup.py file and run the entire setup.py code 
where it is going to setup entire project as a package 

'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() ->List[str]:
    """
    This function will return list of requirements
    """

    requirements_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # read lines from the file
            lines=file.readlines()
            # Process each line
            for line in lines:
                requirements=line.strip()
                # ignore empty lines and -e.
                if requirements and requirements!='-e .':
                    requirements_list.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_list

print(get_requirements())

setup(
    name="NetworkSecurityProject",
    version="0.0.1",
    author="Sri Nidhi",
    author_email="nidhisrikankanala@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)

