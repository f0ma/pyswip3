# -*- coding: utf-8 -*-


# pyswip -- Python SWI-Prolog bridge
# Copyright (c) 2007-2012 Yüce Tekol
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#  
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# PySWIP setup script


import sys
import os
import os.path
from distutils.core import setup
from setuptools.command.install import install
from setuptools.command.develop import develop


def check_reqs(command_subclass):
    """Check requirements."""
    orig_run = command_subclass.run
    def modified_run(self):
        try:
            from pyswip.prolog import Prolog
            p = Prolog()
            p.assertz('setup_prolog(1)')
            list(p.query('setup_prolog(1)'))
        except:
            print('----------------------')
            print('There is a problem with SWI-Prolog Installation')
            print('Please, check if you have it installed with shared Libraries')
            print('Installation guide: https://github.com/yuce/pyswip/blob/master/INSTALL')
            print('----------------------')

        orig_run(self)

    command_subclass.run = modified_run
    return command_subclass


@check_reqs
class CustomDevelopCommand(develop):
    action = 'develop'


@check_reqs
class CustomInstallCommand(install):
    action = 'install'


setup(name="pyswip_alt",
      version="0.2.3",
      url="https://github.com/JoaoFelipe/pyswip/",
      author="Yuce Tekol",
      author_email="yucetekol@gmail.com",
      description="PySWIP enables querying SWI-Prolog in your Python programs.",
      long_description="""
PySWIP Alt 0.2.3
================


Disclaimer:

This is a fork from https://github.com/yuce/pyswip
Its only purpose is to publish the most updated version at pypi

-----------------

PySWIP is a Python - SWI-Prolog bridge enabling to query SWI-Prolog
in your Python programs. It features an (incomplete) SWI-Prolog foreign
language interface, a utility class that makes it easy querying with Prolog
and also a Pythonic interface.

Since PySWIP uses SWI-Prolog as a shared library and ctypes to access it,
it doesn't require compilation to be installed.

Note that this version of PySWIP is slightly incompatible with 0.1.x versions.

Requirements:
-------------

* Python 2.3 and higher.
* ctypes 1.0 and higher.
* SWI-Prolog 5.6.x and higher (most probably other versions will also work).
* libpl as a shared library.
* Works on Linux and Win (32 & 64), should work for all POSIX.

News
----

* Importing ``pyswip`` automatically initializes SWI-Prolog.
* Fixed a bug with querying lists with the new interface.

Example (Using Prolog):
-----------------------

    >>> from pyswip import Prolog
    >>> prolog = Prolog()
    >>> prolog.assertz("father(michael,john)")
    >>> prolog.assertz("father(michael,gina)")
    >>> list(prolog.query("father(michael,X)"))
    [{'X': 'john'}, {'X': 'gina'}]
    >>> for soln in prolog.query("father(X,Y)"):
    ...     print soln["X"], "is the father of", soln["Y"]
    ...
    michael is the father of john
    michael is the father of gina

Since version 0.1.3 of PySWIP, it is possible to register a Python function as a
Prolog predicate through SWI-Prolog's foreign language interface.

Example (Foreign Functions):
----------------------------

    from pyswip import Prolog, registerForeign

    def hello(t):
        print "Hello,", t
    hello.arity = 1

    registerForeign(hello)

    prolog = Prolog()
    prolog.assertz("father(michael,john)")
    prolog.assertz("father(michael,gina)")
    list(prolog.query("father(michael,X), hello(X)"))

Outputs:
    Hello, john
    Hello, gina

Since version 0.2, PySWIP contains a 'Pythonic' interface which allows writing
predicates in pure Python (*Note that interface is experimental.*)

Example (Pythonic interface):
-----------------------------

    from pyswip import Functor, Variable, Query

    assertz = Functor("assertz", 2)
    father = Functor("father", 2)

    call(assertz(father("michael","john")))
    call(assertz(father("michael","gina")))

    X = Variable()
    q = Query(father("michael",X))
    while q.nextSolution():
        print "Hello,", X.value

Outputs:
    Hello, john
    Hello, gina
""",
      license="MIT",
      packages=["pyswip"],
      classifiers=[
                   'Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Scientific/Engineering :: Artificial Intelligence',
                   'Topic :: Software Development :: Libraries :: Python Modules'
                   ],
      cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
      },
    )

