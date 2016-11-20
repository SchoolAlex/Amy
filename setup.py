from setuptools import setup, find_packages

CURRENT_VERSION = "0.0.1"
LICENSE_TYPE = "Apache"

setup(
    name = "Amy",
    version = CURRENT_VERSION,
    packages = find_packages(),
    scripts = [''],

    install_requires = [''],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst'],
        # And include any *.msg files found in the 'Amy' package, too:
        'Amy': ['*.msg'],
    }

    # metadata for upload to PyPI
    author = "Alexander, \'Adeus D. Claid, Aerius L. Anima\' J. Van Matre",
    author_email = "tryamyai@gmail.com",
    description = "This is a custom built, general-use, all-around artificial intelligence system.",
    license = LICENSE_TYPE,
    keywords = "Amy ai",
    url = "",   # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
