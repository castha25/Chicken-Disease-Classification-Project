import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.1"

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "castha25"
AUTHOR_EMAIL = "castha012@gmail.com"
SRC_REPO = "cnnClassifier"


setuptools.setup(
    name=SRC_REPO,  
    version="0.0.1",
    author="Astha",
    author_email="castha012@gmail.com",
    description="A small python package for CNN-based image classification", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/castha25/Chicken-Disease-Classification-Project",
    project_urls={
        "Bug Tracker": "https://github.com/castha25/Chicken-Disease-Classification-Project/issues",

    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)