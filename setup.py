from setuptools import setup, find_packages

setup(
    name="kestra-ion",
    version="0.1.0",
    author="Anna Geller",
    author_email="hello@kestra.io",
    packages=find_packages(),
    url="https://github.com/anna-geller/kestra-ion",
    license="LICENSE.txt",
    description="A simple package to read Ion data into a list of dictionaries suitable for use in dataframes.",
    long_description=open("README.md").read(),
    install_requires=[
        "amazon.ion",
        "python-dateutil",
    ],
    tests_require=["pytest"],
    extras_require={"test": ["pytest"]},
)
