from setuptools import find_packages, setup

setup(
    name='drfapikey',
    version=__import__('rest_framework_api_key').__version__,
    author="Emmanouil Konstantinidis",
    author_email="hello@manos.im",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/manosim/django-rest-framework-api-key",
    license='BSD',
    description="Authenticate Web APIs made with Django REST Framework",
    long_description=open("README.md").read(),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
    ],
)
