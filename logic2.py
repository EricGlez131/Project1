from PyQt6.QtWidgets import *
from gui2 import *
import csv


class Logic2(QMainWindow, Ui_Gui2):
    def __init__(self, mainWindow):
        """
        creates the window and connects all the buttons
        :param mainWindow: this param is the previous window it is used so that i can re call it
        """
        super().__init__()
        self.setupUi(self)
        self.scoreList = []
        self.mainWindow = mainWindow


        self.SubPush.clicked.connect(lambda: self.submit2())
        self.ClearPush.clicked.connect(lambda: self.clear2())
        self.ConvertPush.clicked.connect(lambda: self.convertCSV())
        self.EditPush.clicked.connect((lambda: self.edit()))

    def submit2(self):
        """
        this method does all the function after the button is pressed it checks for exceptions and also does all the
        labels
        :return: nothing
        """
        TotalScores = int(self.studentsLabelNum.text())

        self.scoreList = []
        try:
            score_input = self.gradeBox.text()
            scores = list(map(int, score_input.split()))
            if len(scores) != TotalScores:
                self.BigLabel.setText(f'Please enter exactly {TotalScores} scores.')
                return

            self.scoreList = scores

            bestScore = max(self.scoreList)
            word = ''
            for i in range(len(self.scoreList)):
                word = word + f'Student {i + 1} score is {self.scoreList[i]} and grade is {self.PrintScores(int(self.scoreList[i]), bestScore)}\n'
            self.BigLabel.setText(word)
            self.AverageScore(self.scoreList, bestScore)
            self.SubPush.setHidden(True)


        except:
            self.BigLabel.setText('Please Enter Integer Numbers ex. 50 60 70')

    def PrintScores(self, score, HighScore):
        """
        this method takes in a score and the high scores as well as the highest score and give it letter grade returning a letter
        :param score: one single score
        :param HighScore: This is the highest score of the list
        :return:none
        """
        if score >= HighScore - 10:
            return 'A'
        if score >= HighScore - 20:
            return 'B'
        if score >= HighScore - 30:
            return 'C'
        if score >= HighScore - 40:
            return 'D'
        else:
            return 'F'

    def AverageScore(self, ScoreList, bestScore):
        """
        this method takes in a list and the best score and finds the average of the scores that were types in

        :param ScoreList: List of all the score
        :param bestScore: the max score on the list that was find before it was sent here
        :return: it does not return anything but changes the AvgLabel to display the average
        """
        AverageTestScore = 0
        for i in range(len(ScoreList)):
            AverageTestScore += int(ScoreList[i])
        Average = AverageTestScore / len(ScoreList)
        self.AvgLabel.setText(f'The average score is {Average :.2f}, a grade {self.PrintScores(Average, bestScore)}')

    def clear2(self):
        """
        this method clears out all the labels and sets everything back to normal
        :return:none
        """
        self.BigLabel.setText('Example to Type 30 40 50 60\nONLY Integers no commas')
        self.scoreList.clear()
        self.SubPush.setHidden(False)
        self.AvgLabel.clear()
        self.gradeBox.clear()
        self.gradeBox.setFocus()

    def convertCSV(self):
        """
        this method convert the information and test scores into a simple csv file
        :return: none
        """
        score_list = self.scoreList

        with open('results.csv', 'w') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(['Student', 'Score'])

            for i in range(len(score_list)):
                csv_writer.writerow([f'students{i}', score_list[i]])
        self.BigLabel.setText('Close Both Window For File to Save')
        self.AvgLabel.clear()

    def edit(self):
        """
        this method hides the current Window and shows to main to Edit
        :return: none
        """
        self.mainWindow.show()
        self.hide()
