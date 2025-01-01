"""
Module to build the local package

Author: Vivien Leclercq
Created: 01/01/2025
"""

import glob
import os
from setuptools import setup, find_packages


class SetupUtils:
    """
    Class containing helpers for creating the package.
    """

    @classmethod
    def read_content_of_file(cls, filename: str) -> str:
        """
        Return the content of a file as str.
        """
        with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
            return f.read()

    @classmethod
    def get_readme_content(cls) -> str:
        """
        Return the content of the readme file.
        """
        return cls.read_content_of_file("README.md")

    @classmethod
    def get_requirements(cls) -> list[str]:
        """
        Return the required requirements for this project.
        """
        return cls.read_content_of_file("requirements.txt").splitlines()

    @classmethod
    def get_extra_requirements(cls):
        """
        Dynamically determine extra dependencies.
        """
        extra_requirements = {}

        extra_requirements_files = glob.glob("requirements-*.txt")
        for extra_requirement_file in extra_requirements_files:
            name = os.path.splitext(extra_requirement_file)[0].replace("requirements-", "", 1)
            extra_requirements[name] = cls.read_content_of_file(extra_requirement_file).splitlines()

    @classmethod
    def get_metadatas(cls) -> dict[str, str]:
        """
        Return the project metadatas.
        """
        metadatas = {}
        exec(cls.read_content_of_file("sudoku_resolver/src/__meta__.py"), metadatas)  # pylint: disable=exec-used
        return metadatas


meta = SetupUtils.get_metadatas()

setup(
    # Project variables
    name=meta["name"],
    version=meta["version"],
    description=meta["description"],
    long_description=SetupUtils.get_readme_content(),
    long_description_content_type="text/markdown",
    url=meta["url"],
    license=meta["license"],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    # Author variables
    author=meta["author"],
    author_email=meta["author_email"],
    # Project packages
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    package_dir={meta["name"]: os.path.join(".", meta["path"])},
    # Project requirments
    python_requires=">=3.7",
    install_requires=SetupUtils.get_requirements(),
    extras_require=SetupUtils.get_extra_requirements(),
)
