General
Why Python programming is awesome
What’s an interactive test
Why tests are important
How to write Docstrings to create tests
How to write documentation for each module and function
What are the basic option flags to create tests
How to find edge cases

Resources
Read or watch:

doctest — Test interactive Python examples (until “26.2.3.7. Warnings” included)
doctest – Testing through documentation
Unit Tests in Python
Unittest module
Interactive and Non-interactive tests

Python Test Cases
All your test files should be inside a folder tests
All your test files should be text files (extension: .txt)
All your tests should be executed by using this command: python3 -m doctest ./tests/*
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
