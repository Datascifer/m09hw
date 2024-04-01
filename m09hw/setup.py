from setuptools import setup, find_packages

setup(
    name="booklover",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # pandas
    ],
    # Pytest integration
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
