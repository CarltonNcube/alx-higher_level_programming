#!/usr/bin/python3

class LockedClass:
    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(attr))
        super().__setattr__(attr, value)
