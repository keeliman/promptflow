import os
import re
from io import open
from typing import Any, List, Match, cast

from setuptools import find_namespace_packages, setup

PACKAGE_NAME = "promptflow-tools"
PACKAGE_FOLDER_PATH = "promptflow"


def parse_requirements(file_name: str) -> List[str]:
    with open(file_name) as f:
        return [
            require.strip() for require in f
            if require.strip() and not require.startswith('#')
        ]


# Version extraction inspired from 'requests'
with open(os.path.join(PACKAGE_FOLDER_PATH, "version.txt"), "r") as fd:
    version_content = fd.read()
    print(version_content)
    version = cast(Match[Any], re.search(r'^VERSION\s*=\s*[\'"]([^\'"]*)[\'"]', version_content, re.MULTILINE)).group(1)
if not version:
    raise RuntimeError("Cannot find version information")

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=PACKAGE_NAME,
    version=version,
    description="Prompt flow built-in tools",
    long_description_content_type="text/markdown",
    long_description=readme,
    author="Microsoft Corporation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires="<4.0,>=3.8",
    install_requires=parse_requirements('requirements.txt'),
    packages=find_namespace_packages(include=[f"{PACKAGE_FOLDER_PATH}.*"]),
    entry_points={
        "package_tools": ["builtins = promptflow.tools.list:list_package_tools"],
    },
    include_package_data=True,
    extras_require={
        "azure": [
            "azure-ai-ml>=1.11.0,<2.0.0"
        ]
    },
    project_urls={
        "Bug Reports": "https://github.com/microsoft/promptflow/issues",
        "Source": "https://github.com/microsoft/promptflow",
    },
)
