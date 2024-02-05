Tests were written using the Python `unittest` module, which provides a rich set of commands for running tests. Here are some useful commands and their explanations:

1. **Running all tests**
```sh
python -m unittest discover
```
This command will discover and run all test cases in the current directory and its subdirectories.

2. **Running tests in a specific folder**
```sh
python -m unittest discover -s tests/Term_X/sitting_01
```
The `-s` flag specifies the directory to start discovery (`tests/Term_X/sitting_01` in this case).

3. **Running tests in a specific folder with a specific phrase in the file paths**
```sh
python -m unittest discover -s tests/Term_X -k session_01
```
The `-k` flag is used to specify a keyword (`session_01` in this case) to match against test file paths.

4. **Running tests in a specific folder with a specific phrase in the file paths and a specific filename pattern**
```sh
python -m unittest discover -s tests/Term_X -k "session_01" -p "test*.py"
```
The `-p` flag is used to match test files using shell-style wildcard patterns (`test*.py` in this case).
