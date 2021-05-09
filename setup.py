import os
from setuptools import setup, find_packages


package_name = "dyndns_updater"


entry_points = {
    'console_scripts': [
        'duckdns = dyndns_updater.__main__:duckdns_cli'
    ],
    'gui_scripts': [
    ]
}


# ------------------------------------------------------------------------------

about = {}
with open(os.path.join(package_name, '__info__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name=package_name,
    version=about['__version__'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=find_packages(),
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points=entry_points,
)
