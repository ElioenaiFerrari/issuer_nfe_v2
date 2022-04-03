from setuptools import setup, find_packages

setup(
    name='issuer_nfe',
    version='2.0',
    description='Issuer NFE',
    author='Elioenai Ferrari',
    author_email="elioenaiferrari@gmail.com",
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[
        'flask',
    ]
)
