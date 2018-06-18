# Normalizing a CSV file

This solution is written in Python 3.x.  Specifically, I developed and tested using
Python 3.6.5, installed via Homebrew on Mac OS X High Sierra (10.13.5).
It will likely run on earlier versions of Python 3.x, but would need
some additional work to run on Python 2.x.  It should run fine on other Python 3.x
platforms as well.

To simplify the setup, I have only used Python's built-in libraries.

## Setting up Python 3.6.x on Mac OS X

Mac OS X includes Python 2.x by default (even on High Sierra).  The easiest way to
get Python 3.x is to install it via [Homebrew](https://brew.sh).

If you don't already have Homebrew, see the site for
[installation instructions](https://brew.sh).

Once Homebrew is installed, you can install Python 3.x by issuing this command: `brew install python`

Verify that Python 3.x is installed: `python3 --version`
(note the use of `python3` vs. `python` for the command)

If you don't want to use homebrew, you can try a traditional installer from the
[official Python site](https://www.python.org).

## Running the normalize program

After cloning the GitHub repository, simply run `normalize.py` using `python3`, either providing a
the path to an appropriate CSV file as a parameter or using stdin.  Two sample files are included
in the repository.  Any of the following should work:

* `python3 normalize.py < sample.csv`
* `python3 normalize.py sample.csv`
* `python3 normalize.py < sample-with-broken-utf8.csv`
* `python3 normalize.py sample-with-broken-utf8.csv`

By default, output goes to stdout.  Redirect if you'd like to preserve the output to a file instead.
