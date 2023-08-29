#!/usr/bin/python3

def raise_exception_msg(message=""):
    class CustomNameError(Exception):
        pass

    raise CustomNameError(message)
