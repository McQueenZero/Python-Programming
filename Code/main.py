from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    class Teacher:
        profession = 'eduction'

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def showName(self):
            print(self.name)

        @classmethod
        def showProfession(cls):
            print(cls.profession)

        @staticmethod
        def showHello():
            print('Hello teacher!')


    Teacher.showProfession()
    Teacher.showHello()
