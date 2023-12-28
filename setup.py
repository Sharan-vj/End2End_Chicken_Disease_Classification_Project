import setuptools

with open("README.MD", "r", encoding="utf-8") as f:
    long_description = f.read()

__VERSION__ = "0.0.0"

REPO_NAME = "Chicken_Disease_Classification_System"
AUTHOR_USER_NAME = "Sharan-vj"
SRC_REPO = "cnnClassifer"
AUTHOR_EMAIL = "sharanvj678@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__VERSION__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for cnn app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "module"},
    packages=setuptools.find_packages(where="module")
)