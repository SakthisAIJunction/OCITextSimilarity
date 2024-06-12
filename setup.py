from setuptools import setup, find_packages

setup(
    name = "OCITextSimilarity",
    version = "0.1.0",
    packages = find_packages(),
    install_requires =  [ 'langchain_community', 'oci' ],
    author = "Sakthivel Thangaraj",
    author_email = "sakthiveltvt.thangaraj@gmail.com",
    description =  'A package for calculating the text similarity using OCI embeddings',
    url = '',
    classifiers = [ ' programming language:: python :: 3.12 ',
                    'License :: OSI Approved :: MIT License',
                    'Operating System :: Independent',
                    ],
    python_requires = '>=3.9',

)