'''Problem Statement
Import the package linalg from the SciPy library and use the solve method to solve
the provided linear equations to find the value of x and y'''

# import required libraries
import numpy as np
from scipy import linalg

#Test has 38 questions and worth 150 marks
#True ond false questions worth 4 marks each
#muLtiple choice questions worth 9 points each

#let x is the number of true false questions
#Let y is the nunber of multiple choice questions

# (x + y = 30)
# (4x + 9y = 150)
testQuestVariable = np.array([[1, 1], [4, 9]])
testQuestValue = np.array([30, 150])

# use linalg function of Scipy
# use solve method to solve the linear equation and final value for x and y
print(linalg.solve(testQuestVariable, testQuestValue))