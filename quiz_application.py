import time
import json
import random
import os

# Questions by category (20 questions for each category)
questions = {
    "Science": [
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "O2", "CO2", "NaCl"],
            "answer": "H2O"
        },
        {
            "question": "What planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Mars"
        },
        {
            "question": "What is the powerhouse of the cell?",
            "options": ["Nucleus", "Mitochondria", "Ribosome", "Endoplasmic Reticulum"],
            "answer": "Mitochondria"
        },
        {
            "question": "What gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide"
        },
        {
            "question": "What is the speed of light?",
            "options": ["300,000 km/s", "150,000 km/s", "1,000,000 km/s", "1,500 km/s"],
            "answer": "300,000 km/s"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "options": ["0", "50", "100", "200"],
            "answer": "100"
        },
        {
            "question": "What is the most abundant gas in Earth's atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
            "answer": "Nitrogen"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Quartz"],
            "answer": "Diamond"
        },
        {
            "question": "What type of bond involves the sharing of electron pairs?",
            "options": ["Ionic bond", "Covalent bond", "Metallic bond", "Hydrogen bond"],
            "answer": "Covalent bond"
        },
        {
            "question": "What is the unit of electric current?",
            "options": ["Volt", "Ohm", "Ampere", "Watt"],
            "answer": "Ampere"
        },
        {
            "question": "What is the primary organ of the circulatory system?",
            "options": ["Brain", "Liver", "Heart", "Lungs"],
            "answer": "Heart"
        },
        {
            "question": "What is the main gas found in the bubbles of soda?",
            "options": ["Nitrogen", "Oxygen", "Carbon Dioxide", "Hydrogen"],
            "answer": "Carbon Dioxide"
        },
        {
            "question": "What is the chemical formula for table salt?",
            "options": ["KCl", "NaCl", "MgCl2", "CaCl2"],
            "answer": "NaCl"
        },
        {
            "question": "What is the basic unit of life?",
            "options": ["Cell", "Atom", "Molecule", "Tissue"],
            "answer": "Cell"
        },
        {
            "question": "What is the most common element in the universe?",
            "options": ["Oxygen", "Hydrogen", "Carbon", "Nitrogen"],
            "answer": "Hydrogen"
        },
        {
            "question": "Which planet is known for its rings?",
            "options": ["Jupiter", "Saturn", "Neptune", "Uranus"],
            "answer": "Saturn"
        },
        {
            "question": "What is the process of converting light energy into chemical energy called?",
            "options": ["Photosynthesis", "Respiration", "Transpiration", "Fermentation"],
            "answer": "Photosynthesis"
        },
        {
            "question": "What is the primary component of the sun?",
            "options": ["Oxygen", "Hydrogen", "Helium", "Carbon"],
            "answer": "Hydrogen"
        },
        {
            "question": "What is the term for the study of living organisms?",
            "options": ["Biology", "Chemistry", "Physics", "Geology"],
            "answer": "Biology"
        },
        {
            "question": "What is the unit of measurement for frequency?",
            "options": ["Hertz", "Watts", "Joules", "Volts"],
            "answer": "Hertz"
        },
    ],
    "History": [
        {
            "question": "Who was the founder of Pakistan?",
            "options": ["Allama Iqbal", "Quaid-e-Azam Muhammad Ali Jinnah", "Liaquat Ali Khan", "Fatima Jinnah"],
            "answer": "Quaid-e-Azam Muhammad Ali Jinnah"
        },
        {
            "question": "In which year was the Lahore Resolution passed?",
            "options": ["1930", "1940", "1947", "1956"],
            "answer": "1940"
        },
        {
            "question": "What is the national poet of Pakistan known for his philosophical poetry?",
            "options": ["Faiz Ahmed Faiz", "Allama Iqbal", "Nusrat Fateh Ali Khan", "Ahmed Faraz"],
            "answer": "Allama Iqbal"
        },
        {
            "question": "Which city was the first capital of Pakistan?",
            "options": ["Karachi", "Islamabad", "Lahore", "Peshawar"],
            "answer": "Karachi"
        },
        {
            "question": "Who was the first Governor-General of Pakistan?",
            "options": ["Quaid-e-Azam Muhammad Ali Jinnah", "Liaquat Ali Khan", "Ghulam Muhammad", "Iskander Mirza"],
            "answer": "Quaid-e-Azam Muhammad Ali Jinnah"
        },
        {
            "question": "What event is commemorated on Pakistan Day?",
            "options": ["Independence Day", "Lahore Resolution", "Eid ul-Fitr", "Defense Day"],
            "answer": "Lahore Resolution"
        },
        {
            "question": "Which was the first province to be created after Pakistan's independence?",
            "options": ["Punjab", "Balochistan", "Sindh", "Khyber Pakhtunkhwa"],
            "answer": "Balochistan"
        },
        {
            "question": "Who was the first female Prime Minister of Pakistan?",
            "options": ["Fatima Jinnah", "Benazir Bhutto", "Khadija Siddiqui", "Nazia Hassan"],
            "answer": "Benazir Bhutto"
        },
        {
            "question": "What is the name of the first constitution of Pakistan?",
            "options": ["Constitution of 1956", "Constitution of 1973", "Constitution of 1962", "Constitution of 1949"],
            "answer": "Constitution of 1956"
        },
        {
            "question": "When did Pakistan become a Republic?",
            "options": ["1947", "1956", "1962", "1973"],
            "answer": "1956"
        },
        {
            "question": "What was the first major war fought by Pakistan?",
            "options": ["Indo-Pak War of 1947", "Indo-Pak War of 1965", "Kargil Conflict", "War on Terror"],
            "answer": "Indo-Pak War of 1947"
        },
        {
            "question": "Who was the leader of the Pakistan Movement?",
            "options": ["Liaquat Ali Khan", "Quaid-e-Azam Muhammad Ali Jinnah", "Allama Iqbal", "Zulfikar Ali Bhutto"],
            "answer": "Quaid-e-Azam Muhammad Ali Jinnah"
        },
        {
            "question": "Which major city was the center of the Pakistan Movement?",
            "options": ["Karachi", "Lahore", "Islamabad", "Quetta"],
            "answer": "Lahore"
        },
        {
            "question": "Which political party was founded by Allama Iqbal?",
            "options": ["Muslim League", "Pakistan Peoples Party", "Awami League", "Pakistan Muslim League"],
            "answer": "Muslim League"
        },
        {
            "question": "What is the title of the national anthem of Pakistan?",
            "options": ["Qaumī Tarānah", "Saeed Jaffri", "Aye Rah-e-Haq", "Dil Dil Pakistan"],
            "answer": "Qaumī Tarānah"
        },
        {
            "question": "When is Pakistan's Independence Day celebrated?",
            "options": ["14th August", "23rd March", "1st January", "6th September"],
            "answer": "14th August"
        },
        {
            "question": "What is the significance of 23rd March in Pakistan?",
            "options": ["Independence Day", "Constitution Day", "Pakistan Resolution Day", "Defense Day"],
            "answer": "Pakistan Resolution Day"
        },
        {
            "question": "Which is the largest province of Pakistan by area?",
            "options": ["Punjab", "Sindh", "Balochistan", "Khyber Pakhtunkhwa"],
            "answer": "Balochistan"
        },
        {
            "question": "Who was the first woman to receive a Nobel Prize from Pakistan?",
            "options": ["Malala Yousafzai", "Benazir Bhutto", "Fatima Jinnah", "Sharmeen Obaid-Chinoy"],
            "answer": "Malala Yousafzai"
        },
        {
            "question": "Which city is known as the City of Gardens in Pakistan?",
            "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
            "answer": "Lahore"
        },
    ],
    "General Knowledge": [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        {
            "question": "Which planet is known as the 'Blue Planet'?",
            "options": ["Mars", "Earth", "Jupiter", "Neptune"],
            "answer": "Earth"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Mark Twain", "Charles Dickens", "William Shakespeare", "Ernest Hemingway"],
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "answer": "Pacific Ocean"
        },
        {
            "question": "Which animal is known as the King of the Jungle?",
            "options": ["Elephant", "Tiger", "Lion", "Giraffe"],
            "answer": "Lion"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Yen", "Won", "Dollar", "Pound"],
            "answer": "Yen"
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1912", "1905", "1920", "1930"],
            "answer": "1912"
        },
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["K2", "Kangchenjunga", "Mount Everest", "Lhotse"],
            "answer": "Mount Everest"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Tomato", "Avocado", "Pepper", "Onion"],
            "answer": "Avocado"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "Thailand", "South Korea"],
            "answer": "Japan"
        },
        {
            "question": "Who is the author of 'Harry Potter' series?",
            "options": ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "George R.R. Martin"],
            "answer": "J.K. Rowling"
        },
        {
            "question": "Which continent is known as the Dark Continent?",
            "options": ["Asia", "Europe", "Africa", "Australia"],
            "answer": "Africa"
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Monaco", "Malta", "Vatican City", "San Marino"],
            "answer": "Vatican City"
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Pb", "Fe"],
            "answer": "Au"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["Helium", "Oxygen", "Hydrogen", "Carbon"],
            "answer": "Hydrogen"
        },
        {
            "question": "Which gas is most abundant in the Earth's atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
            "answer": "Nitrogen"
        },
        {
            "question": "What is the primary language spoken in Brazil?",
            "options": ["Spanish", "English", "Portuguese", "French"],
            "answer": "Portuguese"
        },
        {
            "question": "What is the main purpose of the United Nations?",
            "options": ["To promote world peace", "To control world trade", "To manage global resources", "To conduct wars"],
            "answer": "To promote world peace"
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
            "answer": "Nile River"
        },
        {
            "question": "Which is the largest desert in the world?",
            "options": ["Sahara", "Arabian", "Gobi", "Kalahari"],
            "answer": "Sahara"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Quartz"],
            "answer": "Diamond"
        },
    ]
}


# Function to display past scores
def display_scores():
    try:
        with open('scores.json', 'r') as f:
            scores = json.load(f)
        print("\nPast Scores:")
        for score in scores:
            print(f"Player: {score['player']}, Category: {score['category']}, Score: {score['score']}, Date: {score['date']}")
    except FileNotFoundError:
        print("No past scores available.")

# Function to save score
def save_score(player, category, score):
    from datetime import datetime
    data = {
        'player': player,
        'category': category,
        'score': score,
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open('scores.json', 'r+') as f:
            scores = json.load(f)
            scores.append(data)
            f.seek(0)
            json.dump(scores, f)
    except FileNotFoundError:
        with open('scores.json', 'w') as f:
            json.dump([data], f)


# Function to pause the quiz
def pause_quiz():
    input("\nQuiz paused. Press Enter to resume...")

# Function to start the quiz
def start_quiz(player, category):
    score = 0
    questions_list = random.sample(questions[category], 10)  # Select 10 random questions from the category

    total_time_limit = 120  # 2 minutes total
    start_time = time.time()  # Start the timer immediately

    for i, question in enumerate(questions_list, 1):
        elapsed_time = time.time() - start_time
        remaining_time = total_time_limit - int(elapsed_time)

        if remaining_time <= 0:
            print("\nTime's up! The quiz has ended.")
            break

        print(f"\nRemaining time: {remaining_time} seconds")
        print(f"\nQuestion {i}: {question['question']}")
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")

        answer = input("\nEnter the number of your answer (or type 'pause' to pause the quiz): ")

        if answer.lower() == 'pause':
            pause_quiz()
            continue

        # Check if the answer is correct
        if question['options'][int(answer) - 1] == question['answer']:
            score += 1

    print(f"\nQuiz complete! Your score: {score}/10")
    save_score(player, category, score)  # Pass score here

# Main function
def main():
    print("Welcome to the Quiz Application!")

    while True:
        print("\nPlease select an option:")
        print("1. Take a Quiz")
        print("2. View Past Scores")
        print("3. Exit")
        option = input("Enter your choice (1/2/3): ")

        if option == '1':
            player = input("Enter your name: ")

            categories = list(questions.keys())
            print("\nSelect a category:")
            for idx, category in enumerate(categories, 1):
                print(f"{idx}. {category}")

            category_choice = int(input("\nEnter your choice: ")) - 1
            selected_category = categories[category_choice]

            # Inform the user that the quiz will start now and time will begin
            print("\nYou have 2 minutes to attempt 10 MCQs")
            start_quiz(player, selected_category)

        elif option == '2':
            display_scores()  # Display past scores

        elif option == '3':
            print("Thank you for using the Quiz Application. Goodbye!")
            break  # Exit the loop and end the program

        else:
            print("Invalid option. Please select again.")


if __name__ == "__main__":
    main()
