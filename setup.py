from setuptools import setup, find_packages

setup(
    name="puruxzi",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "puruxzi = builder_tool.core.cli:main",
        ],
    },
)
