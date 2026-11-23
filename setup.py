
from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path, "r", encoding="utf-8-sig") as file_obj:
        requirements = file_obj.readlines()

        requirements = [
            req.strip()
            for req in requirements
            if req.strip() and not req.strip().startswith("#")
        ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Ayush Raj",
    author_email="aayuraj7164@mail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)
