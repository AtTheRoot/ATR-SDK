from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()


setup(
    name='atr-sdk',
    description='A python package for building antiracist and inclusive systems.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Dawn Wages with Volunteer Engineers for The Movement"
    author_email="contact@theroot.dev",
    url="https://github.com/VE4TM/ATR-SDK",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    version='0.0.1',
    packages=['mypackage'],
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
)