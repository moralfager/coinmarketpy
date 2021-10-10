import setuptools

setuptools.setup(
    name='coinmarket',
    version='2.2.0',
    license='MIT',
    description = 'Coinmarket scrapper',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Zhumakhan Kuatbekov',
    author_email = 'teen.blood@mail.ru',
    install_requires=['requests'],
    url = 'https://github.com/moralfager/coinmarketpy/',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )