__author__ = 'Mj'
class node(object):
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

tree = node("grandmother", [node("daughter", [node("grandson"), node("granddaughter")]), ])