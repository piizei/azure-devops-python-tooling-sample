import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='utility',
    version='0.1',
    scripts=['utlity'],
    author="Petteri Johansson",
    description="Python package example for azure devops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/piizei/azure-devops-python-tooling-sample",
    install_requires=[],
    packages=['src'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)