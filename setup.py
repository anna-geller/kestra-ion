from setuptools import setup, find_packages

setup(
    name="kestra-ion",
    version="0.0.0",
    author="Anna Geller",
    author_email="hello@kestra.io",
    packages=find_packages(),
    url="https://github.com/anna-geller/kestra-ion",
    license="LICENSE.txt",
    description="A simple package to read Ion data into a list of dictionaries suitable for use in dataframes.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "amazon.ion",
        "python-dateutil",
    ],
    tests_require=["pytest"],
    extras_require={"test": ["pytest"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
