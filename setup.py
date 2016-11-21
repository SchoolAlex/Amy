from setuptools import setup, find_packages

# General Variables
AUTHORS = [
            "Alexander J. Van Matre",
            "Adeus D. Claid",
            "Aerius L. Anima"
          ]
BASIC_DESCRIPTION = "An artificial intelligence system for general, and all, purposes."
CONTACT = "tryamyai@gmail.com"
# 'Whole rewrites / Major Updates'.'Features'.'Bug fixes versions'
CURRENT_VERSION = "0.0.1"
LICENSE_TYPE = "Apache"
GITHUB_LINK = "https://github.com/alexjvan/Amy"
PROJECT_NAME = "Amy"
PROJECT_COMPANY = "TryAmyAI"

setup(
        name = PROJECT_NAME,
        author = AUTHORS,
        author_email = CONTACT,
        version = CURRENT_VERSION,
        description = BASIC_DESCRIPTION,
        long_description = open('README.rst').read(),
        packages = find_packages(),
        install_requires = [''],
        license = LICENSE_TYPE,
        url = GITHUB_LINK
)
