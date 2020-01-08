from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    long_description = readme_file.read()

install_requires = ["setuptools", "click>=5.0", "diceware>=0.9.5"]

setup_requirements = ["setuptools_scm"]

setup(
    name="pygenpass",
    packages=find_packages(),
    entry_points={"console_scripts": ["pygenpass = genpass.__init__:main"]},
    version="v0.1",
    author="Mayuri Lahane",
    author_email="mayurilahane1998@gmail.com",
    description="Genpass - Command Line Password Manager Tool",
    long_description=long_description,
    setup_requires=setup_requirements,
    license="MIT",
    keywords="genpass pygenpass gempass passwordmanager manager encryption",
    url="https://github.com/paint-it/genpass",
    py_modules=["genpass.__init__"],
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,)
