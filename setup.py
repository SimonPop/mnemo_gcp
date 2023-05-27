import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "src",
    version = "0.0.1",
    author = "Simon Popelier",
    author_email = "simon.popelier@gmail.com",
    description = ("Finding mnemonics."),
    license = "BSD",
    keywords = "example documentation tutorial",
    packages=find_packages(), # ['src', 'src.pairing', 'src.pairing.search', 'src.pairing.utils'],
    package_data={
      'src': ['pairing/training/config.yaml', 'pairing/model/model_dict', 'pairing/dataset/pairing/english.csv'],
   },
    include_package_data=True,
)