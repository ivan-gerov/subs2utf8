
import setuptools

install_requires = [
        'chardet'
        ]

setuptools.setup(
    name="subtitles2utf8",
    version="1.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'sub2utf8 = sub2utf8:main',
        ],
    },
    include_package_data=True,
    )