from setuptools import setup, find_packages

# 'Whole rewrites / Major Updates'.'Features'.'Bug fixes versions'
CURRENT_VERSION = "0.0.1"
LICENSE_TYPE = "Apache"

setup(
    name = "Amy",
    author = "Alexander, \'Adeus D. Claid, Aerius L. Anima\' J. Van Matre",
    author_email = "tryamyai@gmail.com",
    version = CURRENT_VERSION,
    description = "This is a general-use artificial intelligence system.",
    long_description = open('README.rst').read(),
    packages = find_packages(),
    install_requires = [''],
    license = LICENSE_TYPE,
    keywords = "Amy AI artificial intelligence Alexander Van Matre Adeus Claid Aerius Anima",
)
