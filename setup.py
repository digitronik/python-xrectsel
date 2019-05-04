from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="Nikhil Dhandre",
    author_email="nik.digitronik@live.com",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Utilities",
        "Topic:: Software Development:: Libraries",
        "Topic:: Software Development:: User Interfaces",
    ],
    description="Geometry of a rectangular screen region",
    entry_points={"console_scripts": ["xrectsel= xrectsel.console:cli"]},
    install_requires=["python-xlib"],
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    setup_requires=["setuptools_scm"],
    python_requires=">=3.4",
    keywords="xrectsel, python-xrectsel",
    name="python-xrectsel",
    packages=find_packages(include=["python-xrectsel"]),
    url="https://github.com/digitronik/python-xrectsel",
    version="1.0",
    license="GPLv3",
    zip_safe=False,
)
