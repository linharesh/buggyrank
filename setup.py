from setuptools import setup, find_packages

setup(
    name="buggyrank",
    version="0.0.1",    
    packages=["buggyrank"],
    author=("Henrique Linhares"),
    author_email="hlinhares@id.uff.br",
    description="",
    keywords=[""],
    entry_points={
	    'console_scripts' : [
		    'buggyrank = buggyrank:main'
	    ]
    },
    url="https://github.com/",
    python_requires='>=3.5',
    classifiers=[
    	'Development Status :: 3 - Alpha',
    	'License :: OSI Approved :: MIT License',
    	'Programming Language :: Python :: 3.5',
    	'Programming Language :: Python :: 3.6',
    ],

)