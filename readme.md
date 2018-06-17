Buggyrank
==========
Copyright (c) 2018 Universidade Federal Fluminense (UFF). All rights reserved.

Buggyrank is a tool that perform bug prediction by analyzing git repositories. It uses a simple heuristic presented by Rahman et al. in the paper <a href="https://scholar.google.com/scholar?q=Bug+Cache+for+inspections%3A+hit+or+miss%3F">BugCache for inspections: hit or miss?</a><br>
<br><br>
This heuristic prediction is also in a Google blog post: <a href="http://google-engtools.blogspot.com/2011/12/bug-prediction-at-google.html">Bug Prediction at Google</a>
<br><br>

This application was developed and testes with Python version 3.6  

Developers:<br>
<a href="https://github.com/linharesh">Henrique Linhares</a> (UFF)<br>

Install
------------------

1) Clone the repository from https://github.com/linharesh/buggyrank.git
```
git clone https://github.com/linharesh/buggyrank.git
``` 

2) Enter the 'buggyrank' directory
```
cd buggyrank
``` 

3) Call 'python setup.py install' 
```
python setup.py install
``` 

Basic Usage
------------------

1) Open the terminal and get inside the project that you want to analyzed
The project must be versioned by a git repository
```
cd my_projec
``` 

2) Type 'buggyrank' in the console
```
buggyrank
``` 

3) View the results presented in the console 


License Terms
-------------

The MIT License (MIT)

Copyright (c) 2018 Universidade Federal Fluminense (UFF). All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
