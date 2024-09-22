import csv
import logging

# Logger configuration
logging.basicConfig(filename='question_master.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class QuestionMaster:
    def __init__(self, csv_file='questions.csv'):
        self.csv_file = csv_file
        self.questions = self.load_questions()

    def load_questions(self):
        questions = []
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    questions.append(row)
            logging.info("Questions loaded successfully")
        except FileNotFoundError:
            logging.error("File not found")
        return questions

    def save_questions(self):
        fieldnames = ['num', 'question', 'option1', 'option2', 'option3', 'option4', 'correctoption']
        try:
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.questions)
            logging.info("Questions saved successfully")
        except Exception as e:
            logging.error(f"Error saving questions: {e}")

    def add_question(self):
        num = len(self.questions) + 1
        question = input("Enter the question: ")
        option1 = input("Enter option 1: ")
        option2 = input("Enter option 2: ")
        option3 = input("Enter option 3: ")
        option4 = input("Enter option 4: ")
        correctoption = input("Enter the correct option (op1, op2, op3, or op4): ")
        new_question = {
            'num': num, 'question': question, 'option1': option1, 'option2': option2,
            'option3': option3, 'option4': option4, 'correctoption': correctoption
        }
        self.questions.append(new_question)
        self.save_questions()
        logging.info(f"Added question: {question}")

    def search_question(self, num):
        for question in self.questions:
            if question['num'] == str(num):
                return question
        logging.warning(f"Question {num} not found")
        return None

    def delete_question(self, num):
        question = self.search_question(num)
        if question:
            self.questions.remove(question)
            self.save_questions()
            logging.info(f"Deleted question {num}")

    def modify_question(self, num):
        question = self.search_question(num)
        if question:
            question['question'] = input(f"Enter new question (old: {question['question']}): ")
            question['option1'] = input(f"Enter new option 1 (old: {question['option1']}): ")
            question['option2'] = input(f"Enter new option 2 (old: {question['option2']}): ")
            question['option3'] = input(f"Enter new option 3 (old: {question['option3']}): ")
            question['option4'] = input(f"Enter new option 4 (old: {question['option4']}): ")
            question['correctoption'] = input(f"Enter new correct option (old: {question['correctoption']}): ")
            self.save_questions()
            logging.info(f"Modified question {num}")
    
    def display_questions(self):
        for question in self.questions:
            print(f"{question['num']}. {question['question']}")
            print(f"  op1) {question['option1']}")
            print(f"  op2) {question['option2']}")
            print(f"  op3) {question['option3']}")
            print(f"  op4) {question['option4']}")
            print(f"  Answer: {question['correctoption']}")
    
    def menu(self):
        while True:
            print("1. Add Question")
            print("2. Search Question")
            print("3. Delete Question")
            print("4. Modify Question")
            print("5. Display All Questions")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_question()
            elif choice == '2':
                num = input("Enter question number to search: ")
                question = self.search_question(num)
                if question:
                    print(question)
            elif choice == '3':
                num = input("Enter question number to delete: ")
                self.delete_question(num)
            elif choice == '4':
                num = input("Enter question number to modify: ")
                self.modify_question(num)
            elif choice == '5':
                self.display_questions()
            elif choice == '6':
                break
            else:
                print("Invalid choice")

if __name__ == "__main__":
    qm = QuestionMaster()
    qm.menu()
