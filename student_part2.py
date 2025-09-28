"""
File: student.py
Resources to manage a student's name and test scores.
"""

import random

class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))

    # Comparison methods
    def __eq__(self, other):
        """Tests for equality based on student names."""
        if isinstance(other, Student):
            return self.name == other.name
        return NotImplemented

    def __lt__(self, other):
        """Tests for less than based on student names."""
        if isinstance(other, Student):
            return self.name < other.name
        return NotImplemented

    def __ge__(self, other):
        """Tests for greater than or equal to based on student names."""
        if isinstance(other, Student):
            return self.name >= other.name
        return NotImplemented

def main():
    # Objects
    students = [
        Student("Zoe", 3),
        Student("Alice", 3),
        Student("Mike", 3),
        Student("David", 3),
        Student("Sarah", 3),
        Student("Bob", 3),
        Student("Charlie", 3),
    ]

    # Sample scores
    students[0].setScore(1, 85)
    students[0].setScore(2, 90)
    students[0].setScore(3, 88)
    
    students[1].setScore(1, 95)
    students[1].setScore(2, 92)
    students[1].setScore(3, 89)
    
    students[2].setScore(1, 78)
    students[2].setScore(2, 85)
    students[2].setScore(3, 82)
    
    students[3].setScore(1, 88)
    students[3].setScore(2, 91)
    students[3].setScore(3, 86)
    
    students[4].setScore(1, 92)
    students[4].setScore(2, 88)
    students[4].setScore(3, 95)
    
    students[5].setScore(1, 75)
    students[5].setScore(2, 80)
    students[5].setScore(3, 78)
    
    students[6].setScore(1, 90)
    students[6].setScore(2, 87)
    students[6].setScore(3, 93)
    
    print("=" * 50)
    print("Original order:")
    print("=" * 50)
    for i, student in enumerate(students, 1):
        print(f"\nStudent {i}:")
        print(student)

    random.shuffle(students)

    print("\n" + "=" * 50)
    print("After shuffling:")
    print("=" * 50)
    for i, student in enumerate(students, 1):
        print(f"\nStudent {i}:")
        print(student)
    
    students.sort()

    print("\n" + "=" * 50)
    print("After sorting (alphabetical by name):")
    print("=" * 50)
    for i, student in enumerate(students, 1):
        print(f"\nStudent {i}:")
        print(student)
        print(f"Average score: {student.getAverage():.2f}")
        print(f"Highest score: {student.getHighScore()}")

if __name__ == "__main__":
    main()