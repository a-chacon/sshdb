"""setup.py: setuptools control."""

from setuptools import setup


setup(
    name="sshme-taurus95",
    packages=["sshme"],
    entry_points={
        "console_scripts": ["sshme = sshme.manager:main"]
    },
    version="0.0.1",
    description="Linux command-line ssh data conection manager",
    author="taurus95",
    author_email="andres.ch@protonmail.com",
    license="GPLv3",
    url="https://github.com/Taurus95/sshme",
    install_requires=[
        "PyInputPlus",
        "termcolor",
        "tabulate"
    ],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
