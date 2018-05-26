from setuptools import setup

setup(
    name="buggyrank",
    packages=["buggyrank"],
    version="0.0.1",    
    scripts=['buggyrank/buggyrank.py'],
    entry_points={
        "console_scripts": ["buggyrank=buggyrank:main"]
    },
    author=("Henrique Linhares"),
    author_email="hlinhares@id.uff.br",
    description="",
    keywords=[""],
    url="https://github.com/",
    python_requires='>=3.5',
    classifiers=[
    	'Development Status :: 3 - Alpha',
    	'License :: OSI Approved :: MIT License',
    	'Programming Language :: Python :: 3.5',
    	'Programming Language :: Python :: 3.6',
    ],

)