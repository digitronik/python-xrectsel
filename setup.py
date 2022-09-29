from setuptools import find_packages
from setuptools import setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Nikhil Dhandre",
    author_email="nik.digitronik@live.com",
    classifiers=[
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Software Development :: User Interfaces",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Geometry of a rectangular screen region",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    install_requires=["python-xlib", "click"],
    long_description=readme,
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["xrectsel= xrectsel.console:cli"]},
    include_package_data=True,
    python_requires=">=3.4",
    keywords="xrectsel, python-xrectsel",
    name="python-xrectsel",
    packages=find_packages(include=["xrectsel"]),
    url="https://github.com/digitronik/python-xrectsel",
    license="GPLv3",
    zip_safe=False,
)
