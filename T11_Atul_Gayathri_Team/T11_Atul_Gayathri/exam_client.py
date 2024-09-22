import datetime
import logging
from question_master import QuestionMaster

# Logger configuration
logging.basicConfig(filename='exam_client.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class ExamClient:
    def __init__(self):
        self.qm = QuestionMaster()
        self.score = 0
        self.total_questions = len(self.qm.questions)

    def conduct_exam(self, student_name, university):
        logging.info(f"Exam started for {student_name} from {university}")
        for question in self.qm.questions:
            print(f"{question['num']}. {question['question']}")
            print(f"  op1) {question['option1']}")
            print(f"  op2) {question['option2']}")
            print(f"  op3) {question['option3']}")
            print(f"  op4) {question['option4']}")
            answer = input("Enter your choice (op1, op2, op3, op4): ")
            if f"op{answer}" == question['correctoption']:
                self.score += 1
        self.display_result(student_name, university)

    def display_result(self, student_name, university):
        print(f"\nStudent Name: {student_name}")
        print(f"University: {university}")
        print(f"Marks Scored: {self.score} out of {self.total_questions}")
        logging.info(f"Exam completed. {student_name} scored {self.score} out of {self.total_questions}")

if __name__ == "__main__":
    current_time = datetime.datetime.now().strftime("%d/%b/%Y %H:%M:%S")
    print(f"Today's date and time: {current_time}")
    student_name = input("Enter student name: ")
    university = input("Enter university: ")
    
    exam = ExamClient()
    exam.conduct_exam(student_name, university)
