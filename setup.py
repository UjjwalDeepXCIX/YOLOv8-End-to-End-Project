from setuptools import find_packages, setup
from typing import List

e_dot = "e ."
def requirement(path:str)->List[str]:
    ''' return requirements'''
    requirements=[]
    with open(path) as fileobj:
        requirements=fileobj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if e_dot in requirements:
            requirements.remove(e_dot)
    
    return requirements
    
setup(
    Name = '</>YOLOv8',
    version= "0.0.1",
    author= "Ujjwal Deep",
    author_email="ujjwaldeep429@gmail.com",
    packages=find_packages(),
    install_requires=requirement("requirements.txt")
)