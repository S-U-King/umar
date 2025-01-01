# quiz_game.py

def ask_question(question, options, correct_answer):
    print(f"\n{question}")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    try:
        answer = int(input("\nEnter the number of your answer: "))
        if options[answer - 1] == correct_answer:
            print("Correct!\n")
            return True
        else:
            print("Incorrect. The correct answer is:", correct_answer, "\n")
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please select a valid option.\n")
        return False

def main():
    print("Welcome to the Quiz Game!\n")

    questions = [
        {
            "question":"1 What is the capital of France?",               
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question":"2 Which programming language is used to create this quiz?",                 
            "options": ["Python", "Java", "C++", "Ruby"],
            "correct_answer": "Python"
        },
        {
            "question":"3 What is 533 + 327?",                       
            "options": ["845", "860", "875", "810"],
            "correct_answer": "860"
        },
        {
            "question":"4 which planet as known is red planet?",                 
            "options":["Earth","Mars","Venus","Jupiter"],
            "correct_answer":"Mars"
        },
        {
            "question":"5 who man is gone first time to moon?",                                    
            "options":["Neil armstrong","Colombus","Edwin aldrin","Micheal collins"],
            "correct_answer":"Neil armstrong"
        },
        {
            "question":"6 who is the smallist planet in the solar system?",                         
            "options":["Venus","Satrun","Mercury","Uranus"],
            "correct_answer":"Mercury"
        },
        {
            "question":"7 Cornea is a transparent spherical structure which?",                    
            "options":["Scatters light","None","Reflects light","Refracts light"],
            "correct_answer":"None"
        },
        {
            "question":"8 what is 34 * 52?",                                  
            "options":["1,534","1,675","1,768","1,876"],
            "correct_answer":"1,768"
        },
        {
            "question":"9 What is the largest ocean on Earth?",                          
            "options":["Atlantic", "Indian", "Arctic", "Pacific"],
            "correct_answer": "Pacific"
        },
        {
            "question":"10 who is the largest planet in the solar system?",
            "options":["Neptune","Jupiter","Uranus","Mercury"],
            "correct_answer":"Jupiter"
        },
        {
            "question":"11 who is the coldest planet in the solar system?",
            "options":["Mercury","Venus","Uranus","Jupiter"],
            "correct_answer":"Uranus"
        },
        {
            "question":"12 who is the brigthest planet in the solar system?",
            "options":["Neptune","Uranus","Mercury","Venus"],
            "correct_answer":"Venus"
        },
        {
            "question":"13 who is the second largest planet in the solar system?",
            "options":["Venus","Satrun","Mercury","Uranus"],
            "correct_answer":"Satrun"
        },
        {
            "question":"14 who is the third smallest planet in the solar system?",
            "options":["Venus","Satrun","Mercury","Uranus"],
            "correct_answer":"Venus"
        },
        {
            "question":"15 who is the hottest planet in the solar system?",
            "options":["Satrun","Mercury","Venus","Uranus"],
            "correct_answer":"Venus"
        },
        {
            "question":"16 who is the oldest planet in the solar system?",
            "options":["Satrun","Mercury","Venus","Jupiter"],
            "correct_answer":"Jupiter"
        },
        {
            "question":"17 which planet as known is blue planet?",                 
            "options":["Earth","Mars","Venus","Jupiter"],
            "correct_answer":"Earth"
        },
        {
            "question":"18 which planet has diamond rain?",                 
            "options":["Earth & Satrun","Neptune & Uranus","Mars & Mercury","Venus & Jupiter"],
            "correct_answer":"Neptune & Uranus"
        },
        {
            "question":"19 Satrun has how many moons?",
            "options":["128","137","146","152"],
            "correct_answer":"146"
        },
        {
            "question":"20 Uranus has how many moons?",
            "options":["49","16","36","28"],
            "correct_answer":"16"
        },
        {
            "question":"21 Jupiter has how many moons?",
            "options":["89","116","76","95"],
            "correct_answer":"95"
        },
        {
            "question":"22 which planet has no moon?",
            "options":["Neptune","Jupiter","Uranus","Mercury"],
            "correct_answer":"Neptune"
        },
        {
            "question":"23 which planet has the shortest day?",
            "options":["Neptune","Uranus","Jupiter","Mercury"],
            "correct_answer":"Jupiter"
        },
        {
            "question":"24 which planet has the longest day?",
            "options":["Venus","Satrun","Mercury","Uranus"],
            "correct_answer":"Venus"
        },
        {
            "question":"25 what is the highest temperature of Venus?",
            "options":["894 °F","876 °F","860 °F","900 °F"],
            "correct_answer":"900 °F"
        },
        {
            "question":"26 who wrote 'Romeo & Juliet'?",
            "options":["Charles dinkens","Mark twain","William shakespeare","Jane austen"],
            "correct_answer":"William shakespeare"
        },
        {
            "question":"27 who developed the theory of relativity?",
            "options":["Albert einstein","Nekola tesla","Galileo galilie","Isaac newton"],
            "correct_answer":"Albert einstein"
        },
        {
            "question":"28 what is the boiling temperature of water?",
            "options":["70 °C","80 °C","100 °C","90 °C"],
            "correct_answer":"100 °C"
        },
        {
            "question":"29 which planet has two moons?",
            "options":["Venus","Satrun","Mercury","Mars"],
            "correct_answer":"Mars"
        },
        {
            "question":"30 what is the lowest temperature of Uranus?",
            "options":["-224℃","-267℃","-278℃","-245℃"],
            "correct_answer":"-224℃"
        },
        {
            "question":"31 who is find the theory of gravity?",
            "options":["Albert einstein","Nekola tesla","Galileo galilie","Isaac newton"],
            "correct_answer":"Isaac newton"
        },
        {
            "question":"32 what is the capital of Pakistan in 1947?",
            "options":["Islamabad","Karachi","Lahore","Punjab"],
            "correct_answer":"Karachi"
        },
        {
            "question":"33 what is the capital of Pakistan in 2024?",
            "options":["Islamabad","Karachi","Lahore","Punjab"],
            "correct_answer":"Islamabad"
        },
        {
            "question":"34 what is 34 * 253?",
            "options":["9,982","8,609","8,904","8,602"],
            "correct_answer":"8,602"
        },
        {
            "question":"35 what is 52 * 253?",
            "options":["12,867","13,856","14,786","13,786"],
            "correct_answer":"13,856"
        },
        {
            "question":"36 What is the capital of England?",
            "options": ["London","Bermingham","Nottingham","Cambrigde"],
            "correct_answer": "London"
        },
        {
            "question":"37 What is the capital of Canada?",
            "options": ["Toronto","Calgary","Ottawa","Victoria"],
            "correct_answer": "Ottawa"
        },
        {
            "question":"38 What is the capital of USA?",
            "options": ["Los angles","Washington .D.C","Mecsico","New york"],
            "correct_answer": "Washington .D.C"
        },
        {
            "question":"39 What is the capital of Japan?",
            "options": ["Tokyo","Osaka","Kawasaki","Kobe"],
            "correct_answer": "Tokyo"
        },
        {
            "question":"40 What is the capital of China?",
            "options": ["Chongqing","Beijing","Boston","Hong kong"],
            "correct_answer": "Beijing"
        },
        {
            "question":"41 What is the capital of Russia?",
            "options": ["Novosibirsk","Saint Petersburg","Moscow","Yekaterinburg"],
            "correct_answer": "Moscow"
        },
        {
            "question":"42 who is the largest mountain on Earth?",
            "options":["Everest","K2","Nanga perbat","Dhaulagiri"],
            "correct_answer":"Everest"
        },
        {
            "question":"43 who is the largest Continents on Earth?",
            "options":["North America","Asia","Africa","South America"],
            "correct_answer":"Asia"            
        },
        {
            "question":"44 who is the largest Country on Earth?",
            "options":["America","Asia","Africa","Russia"],
            "correct_answer":"Russia"            
        },
        {
            "question":"45 First world war in which years?",
            "options":["1928 to 1932","1947 to 1956","1914 to 1918","1932 to 1936"],
            "correct_answer":"1914 to 1918"
        },
        {
            "question":"46 Second world war in which years?",
            "options":["1928 to 1932","1939 to 1945","1914 to 1918","1932 to 1936"],
            "correct_answer":"1939 to 1945"            
        },
        {
            "question":"47 What is the capital of Australia?",
            "options": ["Canberra","Melbrourne","Perth","Sydney"],
            "correct_answer": "Canberra"            
        },
        {
            "question":"48 What is the capital of Indonesia?",
            "options": ["Bandung","Surabaya","Bekasi","Jakarta"],
            "correct_answer": "Jakarta"            
        },
        {
            "question":"49 What is the capital of Ukrain?",
            "options": ["Dnipro","Kyiv","Kharkiv","Odesa"],
            "correct_answer": "Kyiv"             
        },
        {
            "question":"50 What is the capital of India?",
            "options": ["Bangalore","Delhi","New dehli","Mumbai"],
            "correct_answer": "New delhi"                    
        }
    ]

    score = 0
    i = 0
    while i < len(questions):
        question = questions[i]
        if ask_question(question["question"], question["options"], question["correct_answer"]):
            score += 1
        i += 1

    print(f"\nYour final score is {score}/{len(questions)}.")
    
    if score == len(questions):
        print("Congratulations, you got all answers right!")
    elif score > len(questions) / 2:
        print("Good job, you got more than half right!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()      