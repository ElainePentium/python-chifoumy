from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='chifoumy',
      version="0.1",
      description="Chifoumi Model Detection",
      author="Chifouteam",
      author_email="gentil.stephanie@gmail.com",
      url="https://github.com/ElainePentium/chifoumy",
      packages=find_packages(),
      install_requires=requirements,
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      # scripts=['scripts/chifoumy-run'],
      zip_safe=False)
