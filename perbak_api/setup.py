from setuptools import setup, find_packages

setup(
    name='perbak_api',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'flask-sqlalchemy',
        'psycopg2-binary',
    ],
)
