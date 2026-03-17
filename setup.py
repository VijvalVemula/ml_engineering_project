from setuptools import find_packages, setup
from typing import List

from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of requirements.

    param: file_path: The path to the requirements file (e.g., 'requirements.txt') as a string.
    return: A list of strings, where each string is a required package (newlines stripped).

    """
    requirements = []
    with open(file_path, "r") as file_handle:
        requirements = file_handle.read().splitlines()
        requirements = [req.replace("\n", "").strip() for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="ml_engineering_project",
    version="0.0.1",
    author="Vijval Vemula",
    author_email="vemulavijval1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("./requirements.txt")
)