# This script contains the questions used in this trivia game. 


# Defining questions:

init python:

    """
    A class for questions. 
    """
    class Question(object):

        """
        A constructor for a Question object. 
        @param question         a string containing the question
        @param a1               a string containing the first answer choice
        @param a2               a string containing the second answer choice
        @param a3               a string containing the third answer choice
        @param a4               a string containing the fourth answer choice
        @param explain          string with wxplaination of the answer
        @param correct          a string containing the same text for the correct answer choice
        @param point_value      an integer representing the question's point value (default is 1)
        """
        def __init__(self, question, a1, a2, a3, a4, correct, explain, point_value = 1):
            self.question = question
            self.a1 = a1
            self.a2 = a2
            self.a3 = a3
            self.a4 = a4
            self.correct = correct
            self.explain = explain
            self.point_value = point_value



# Instantiating Question objects:


# Don't forget to append these questions to question_list in question_list.rpy!


define q1 = Question(question = "What does the acronym IoT stand for?",
                        a1 = "Internet of Things",
                        a2 = "Internet of Turtles",
                        a3 = "Internet of Telecommunications",
                        a4 = "Internet of Toasters",
                        correct = "Internet of Things",
                        explain = "IoT stands for the Internet of Things, which is a network of interconnected physical devices that can collect and exchange data over the internet.")


define q2 = Question(question = "How can you enhance security for your Internet of Things (IoT) devices?",
                        a1 = "Keep default passwords unchanged",
                        a2 = "Disable automatic updates",
                        a3 = "Regularly update firmware",
                        a4 = "Share device credentials with your cat",
                        correct = "Regularly update firmware",
                        explain = "Regularly updating the firmware of IoT devices enhances security by patching vulnerabilities, fixing bugs, implementing security improvements, staying ahead of exploits, and ensuring compliance with standards and regulations.")   


define q3 = Question(question = "What is a common security concern with IoT devices?",
                        a1 = "Slow internet speed",
                        a2 = "Short battery life",
                        a3 = "Unauthorized access to personal data",
                        a4 = "Limited device compatibility",
                        correct = "Unauthorized access to personal data",
                        explain = "Unauthorized access to personal information is a common security concern with IoT devices because they collect and transmit sensitive data, such as personal and financial information, making them potential targets for hackers aiming to exploit vulnerabilities and gain unauthorized access.")   


define q4 = Question(question = "What is the primary concern with IoT devices when it comes to security?",
                        a1 = "Physical damage",
                        a2 = "Privacy breaches",
                        a3 = "Battery drainage",
                        a4 = "Network connectivity issues",
                        correct = "Privacy breaches",
                        explain = "Privacy breaches are a security concern with IoT devices because they have the potential to collect and transmit personal data without the user's knowledge or consent, compromising their privacy and potentially exposing sensitive information to unauthorized parties.")   


define q5 = Question(question = "What is the purpose of two-factor authentication in IoT security?",
                        a1 = "To ensure secure physical access to IoT devices",
                        a2 = "To provide multiple options for internet connectivity",
                        a3 = "To establish secure communication channels between devices",
                        a4 = "To add an extra layer of security for user authentication",
                        correct = "To add an extra layer of security for user authentication",
                        explain = "Two-factor authentication (2FA) in IoT security adds an extra layer of protection by requiring users to provide two different forms of authentication, reducing the risk of unauthorized access to IoT devices or systems.")   


define q6 = Question(question = "What is the purpose of regular software updates for IoT devices?",
                        a1 = "To improve device performance",
                        a2 = "To fix security vulnerabilities",
                        a3 = "To extend battery life",
                        a4 = "To increase data storage capacity",
                        correct = "To fix security vulnerabilities",
                        explain = "Regular software updates for IoT devices enhance functionality, performance, and security by providing bug fixes, feature improvements, and patches for vulnerabilities.")  


define q7 = Question(question = "What is the role of user education (such as this game) in IoT security?",
                        a1 = "Avoiding you breaking your IoT devices",
                        a2 = "Ensuring compliance with regulatory requirements",
                        a3 = "Raising awareness about security risks and best practices",
                        a4 = "Enhancing device interoperability",
                        correct = "Raising awareness about security risks and best practices",
                        explain = "The role of user education in IoT security is to increase awareness and knowledge among users about the potential risks, best practices, and appropriate security measures when using IoT devices.")  


define q8 = Question(question = "What is the purpose of a VPN (Virtual Private Network) in IoT security?",
                        a1 = "To encrypt data transmitted between IoT devices",
                        a2 = "To physically protect IoT devices from theft",
                        a3 = "To enhance the processing speed of IoT devices",
                        a4 = "To regulate internet access for IoT devices",
                        correct = "To encrypt data transmitted between IoT devices",
                        explain = "The purpose of a VPN (Virtual Private Network) in IoT security is to establish a secure and encrypted connection between IoT devices and the network they communicate with, ensuring data privacy and protection against unauthorized access.")  



# Don't forget to append these question objects to question_list in question_list.rpy!