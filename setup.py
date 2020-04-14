# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in authorizenet/__init__.py
from authorizenet import __version__ as version

setup(
	name='authorizenet',
	version=version,
	description='gateway',
	author='DigiThinkIT',
	author_email='sajid.erpnext@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
