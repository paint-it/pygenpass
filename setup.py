from setuptools import find_packages
from setuptools import setup


with open("README.rst") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt") as req_file:
    install_requires = req_file.read().split()


setup_requirements = ["setuptools_scm"]

setup(
    name="pygenpass",
    entry_points={"console_scripts": ["pygenpass = genpass.__init__:main"]},
    version="0.1",
    author="Mayuri Lahane",
    author_email="mayurilahane1998@gmail.com",
    description="Genpass - Command Line Password Manager Tool",
    long_description=long_description,
    setup_requires=setup_requirements,
    license="MIT",
    keywords="genpass pygenpass gempass passwordmanager manager encryption",
    url="https://github.com/paint-it/genpass",
    packages=find_packages(include=["genpass"]),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    python_requires=">=3.5",
)
