#!/usr/bin/env python
import os
import unittest

from flask_script import Manager

from app import create_app

app=create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

@manager.command
def test():
    """Run the unit tests"""
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()