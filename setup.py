from setuptools import setup, find_packages

setup(
    name="snoro",
    version="0.1.0",
    description="SNORO simple text processor",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["PyYAML>=6.0"],
    entry_points={
        "console_scripts": [
            "snoro=snoro.cli:main"
        ]
    },
)
