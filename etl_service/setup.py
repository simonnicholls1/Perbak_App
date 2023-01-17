from setuptools import setup, find_packages

setup(
    name='etl_service',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'perbak_shared_library'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'etl_service = etl_service.main:main'
        ]
    }
)
