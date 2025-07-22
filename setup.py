from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME_RECOMMENDER",
    version="0.1.0",
    author="ofysar",
    packages=find_packages(),
    install_requires=requirements,
)
