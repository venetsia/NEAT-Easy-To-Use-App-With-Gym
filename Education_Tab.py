import random
import time
import tkinter as tk
from tkinter import END

import numpy as np
from PIL import ImageTk
import pyautogui
import CreateHelpMessage
import StickyNote

import train_chat_BOT
import enum
import NEAT_Single_Processing
import train_chat_BOT


education_mode_labels = ["label1", "label2", "chat_bot_dynamic_learn"]
AI_tab = ["label1"]
AI_categories_tab = ["label2"]
label1 =""
label2 =""
agent_label1 =""
clicks = 0
chat_bot_dynamic_learn =""
response_enter =""
chatbot_next =""
neuron_tab_pic = ""
neuron_tab_label =""
perceptron_image = ""
perceptron_label = ""
check_answer = ""
Introduction_tab = False
Artificial_intelligence_tab = False
AI_Categories_tab = False
Intelligent_Agents_tab = False
Neuron_tab = False
Perceptron_tab = False
class Education_tab(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0



    def hide_old_widgets(self, widget):
        widget.grid_remove()
        return
    def next_button(self, chat_bot_dynamic_learn, response_enter, educatuin_tab):
        global agent_label1
        input = response_enter.get("1.0", tk.END)
        response_enter.delete('1.0', tk.END)
        results = train_chat_BOT.model.predict([train_chat_BOT.bag_of_words(input, train_chat_BOT.words)])[0]
        results_index = np.argmax(results)
        tag = train_chat_BOT.classes[results_index]
        if results[results_index] > 0.7:
            for tg in train_chat_BOT.intents["intents"]:
                if tg["tag"] == tag:
                    responses = tg["responses"]
            if tag =="evaluate":
                image_agent = ImageTk.PhotoImage(file="agent.png")
                agent_label1 = tk.Label(educatuin_tab, image=image_agent)
                agent_label1.image = image_agent
                agent_label1.grid(row=1, column=1)
                agent_label1.config(fg="grey75", bg="grey75")
            elif tag != "evaluate":
                if agent_label1 != "":
                    self.hide_old_widgets(agent_label1)
                    #chat_bot_dynamic_learn.window_create(tk.END, window = tk.Label(chat_bot_dynamic_learn, image = img_agent))
            chat_bot_dynamic_learn.insert(tk.END,"You: " + input + "Agent: " + random.choice(responses) + "\n")
        else:
            chat_bot_dynamic_learn.insert(tk.END,"I didn't get that, try again please.")
    def check_answer(self,value,widget):
        input = widget.get("1.0", tk.END)
        input = input.lower()
        if value == "Neural Network":
            if input in "hidden layer" or input.lower() in "hidden-layer" or input.find("hidden-layer") == 0 or input.find("hidden layer") == 0:
                widget.config(bg="green")
            else:
                widget.config(bg="red")
        elif value == "Learning Types":
            if input.find("reinforcement learning (rl)") == 0 or input.find("reinforcement learning (rl)") == 0 or input.find("reinforcement learning") == 0 or input.find("reinforcement learning") == 0 or input.find("rl") == 0 or input.find("rl") == 0 or input.find("reinforcement") == 0 or input.find("reinforcement") == 0 :
                widget.config(bg="green")
            else:
                widget.config(bg="red")
    def nada(self):
       return
    def automate(self, hidden_level_text,educatuin_tab):
        hidden_level_value = hidden_level_text.get(1.0, tk.END)
        if hidden_level_value == "False\n":
            # Locate Neat Icon
            window_icon = pyautogui.locateOnScreen("NeatConfigImage.PNG")
            print(window_icon)
            # Click Windows Icon
            pyautogui.click(window_icon)
            hidden_level_text.delete(1.0, tk.END)
            print(hidden_level_text.get(1.0, tk.END))
            hidden_level_text.insert(tk.END, "False")
            print(hidden_level_text.get(1.0, tk.END))
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0, "Lets start with the basics. Each learning algorithm will need a variation of these values.\n"
                               "If we select a game we will see that input and output are automatically generated for us based on the game."
                               "\nNeat section:"
                               "\n-fitness_criterion - how our score is calculated (max, min, etc)"
                               "\n-fitness_threshold - how fit we want the agent to become"
                               "\n-pop_size - how many genomes do we want to start with"
                               "\nGenome Section:"
                               "\n-num_inputs - what can the agent see "
                               "\n-num_outputs - actions agent can perform"
                                        "\nThe values are filled out automatically so you can see."
                                        "\nSo the game is CartPole.\nIt has 4 valid observations for input."
                                        "\nFor output we have 2 valid actions (0 or 1) - move left or right"
                                        "\nBecause of fitness_criterion being max we will look for the best genome."
                                        "\nOur agent will stop learning when a genome reaches a score of 500")
            hidden_level_text.delete(1.0, tk.END)
            print(hidden_level_text.get(1.0, tk.END))
            hidden_level_text.insert(tk.END, "ExampleLevel1")
            print(hidden_level_text.get(1.0, tk.END))
        elif hidden_level_value == "LoadWinnerExample\n":
            window_icon = pyautogui.locateOnScreen("Load_Winner.PNG")
            # Click Windows Icon
            pyautogui.click(window_icon)
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0,
                                   "Okey now that we know how can we run NEAT, we will see an example of the previous NEAT configurations we have chosen."
                                   "\nWe have to choose the game we the winner is trained on."
                                   "\nWe also need to specify the name of the winner file"
                                   "\nNumber of episodes per genomes means how many times/episodes do we want to test our winner on."
                                   "\nWe can also view the checkpoints that our algorithm has made. We can change the directory so the software can detect in different directory for checkpoints."
                                   "\n(they have to be marked as 'neat-checkpoint' in order for the software to detect it.)"
                                   "\nWe will look into the network type later but we should choose the same one we have trained it on."
                                   "\nThe config file can be either saved from editor or chosen from directory"
                                   "\nWhen you are ready you can click 'Load Genomes and winner' and you will observe the checkpoints. They load howeever many genomes (population) the generation has. "
                                   "\nYou can see which one is loaded from the below text field.")
        elif hidden_level_value == "LoadWinnerExample2\n":
            window_icon = pyautogui.locateOnScreen("Load_Winner.PNG")
            # Click Windows Icon
            pyautogui.click(window_icon)
            sticky = StickyNote.StickyNotes(educatuin_tab)
            sticky.mainarea.insert(1.0,"Lets see another game example. The game we will see is Lunar Lander and we have 8 inputs and 4 outputs.\n"
                                       "Here it took a little longer for NEAT to figure out how to reach the threshold (goal) so we will see checkpoints 10 generations apart and then we will see the winner.")
    def load_content(self,education_option_selected,educatuin_tab, hidden_level_text):
        selected_indices = education_option_selected.curselection()
        value = education_option_selected.get(selected_indices[0])
        global label1
        global label2
        global chat_bot_dynamic_learn
        global response_enter
        global chatbot_next
        global  Artificial_intelligence_tab
        global AI_Categories_tab
        global Intelligent_Agents_tab
        global neuron_tab_pic
        global neuron_tab_label
        global perceptron_image
        global perceptron_label
        global Neuron_tab
        global check_answer
        if value == "Artificial Intelligence":
            Artificial_intelligence_tab = True
            if label2 != "":
                self.hide_old_widgets(label2)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if neuron_tab_label != "":
                self.hide_old_widgets(neuron_tab_label)
            image1 = ImageTk.PhotoImage(file = "AI-Intro.png")
            label1 = tk.Label(educatuin_tab, image=image1)
            label1.image = image1
            label1.grid(row=1,column = 0)
            label1.config(fg="grey75", bg="grey75")
        elif value == "AI categories":
            if Artificial_intelligence_tab == True:
                AI_Categories_tab = True
                if label1 != "":
                    self.hide_old_widgets(label1)
                if label2 != "":
                    self.hide_old_widgets(label2)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                image2 = ImageTk.PhotoImage(file="AI_second.png")
                label1 = tk.Label(educatuin_tab, image=image2)
                label1.image = image2
                label1.grid(row=1, column=0)
                label1.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text = "Please refer to Artificial Intelligence lesson first", font = ("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Intelligent Agents":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True:
                Intelligent_Agents_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if neuron_tab_pic != "":
                    self.hide_old_widgets(neuron_tab_pic)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                chat_bot_dynamic_learn = tk.Text(educatuin_tab, name="chat_bot_dynamic_learn", height=50, width=70)
                chat_bot_dynamic_learn.grid(row=1, column=0, sticky=tk.W)
                response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
                response_enter.grid(row=2, column=0, sticky=tk.W)
                chat_bot_dynamic_learn.bind('<Key>', lambda e: 'break')
                chat_bot_dynamic_learn.insert(tk.END, "Welcome, I am a chat bot and I am here to answer some questions.\nFor this specific tab you may want to ask questions such as:"
                                                      "\n\"What is an agent?\"\n\"How and when do we evauate an agent?\"\nYou can refer back to this whenever you would like to ask a question. I am trained in answering a few questions.\n")

                # Run button for Neat using a thread
                chatbot_next = tk.Button(educatuin_tab, text="Send",
                                         command=lambda : self.next_button(chat_bot_dynamic_learn, response_enter, educatuin_tab),
                                         justify=tk.LEFT, anchor="w")
                chatbot_next.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
                CreateHelpMessage.CreateToolTip_For_Education_Mode(response_enter, "Dear User, Welcome to intelligent agents lessen. This chat bot is an intelligent agent trained by a neural network. We will look into this next. For now we will see what an agent is by answering two questions. You can refer back to this chat as it was trained to recognise some topics and answer some questions.")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text = "Please refer to AI categories lesson first", font = ("Courier", 20, "bold") )
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Neuron":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True:
                Neuron_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                neuron_tab_pic = ImageTk.PhotoImage(file="biological_neuron.png")
                neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
                neuron_tab_label.image = neuron_tab_pic
                neuron_tab_label.grid(row=1, column=1)
                neuron_tab_label.config(fg="grey75", bg="grey75")
            else:
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if perceptron_label != "":
                    self.hide_old_widgets(perceptron_label)
                if check_answer != "":
                    self.hide_old_widgets(check_answer)
                label2 = tk.Label(educatuin_tab, text="Please refer to AI categories lesson first",
                                  font=("Courier", 20, "bold"))
                label2.config(bg="grey75")
                label2.grid(row=1, column=0)
        elif value == "Neural Network":
            if Artificial_intelligence_tab == True and AI_Categories_tab == True and Intelligent_Agents_tab == True and Neuron_tab == True:
                Perceptron_tab = True
                if label2 != "":
                    self.hide_old_widgets(label2)
                if label1 != "":
                    self.hide_old_widgets(label1)
                if chat_bot_dynamic_learn != "":
                    self.hide_old_widgets(chat_bot_dynamic_learn)
                if response_enter != "":
                    self.hide_old_widgets(response_enter)
                if chatbot_next != "":
                    self.hide_old_widgets(chatbot_next)
                if neuron_tab_label != "":
                    self.hide_old_widgets(neuron_tab_label)
                perceptron_image = ImageTk.PhotoImage(file="percepron.png")
                perceptron_label = tk.Label(educatuin_tab, image=perceptron_image)
                perceptron_label.image = perceptron_image
                perceptron_label.grid(row=1, column=0)
                perceptron_label.config(fg="grey75", bg="grey75")
                response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
                response_enter.grid(row=2, column=0, sticky=tk.W)
                # Run button for Neat using a thread
                check_answer = tk.Button(educatuin_tab, text="Check answer",
                                         command=lambda: self.check_answer(value,response_enter),
                                         justify=tk.LEFT, anchor="w")
                check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        elif value == "Learning Types":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            neuron_tab_pic = ImageTk.PhotoImage(file="Types_of_learning.png")
            neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
            neuron_tab_label.image = neuron_tab_pic
            neuron_tab_label.grid(row=1, column=0)
            neuron_tab_label.config(fg="grey75", bg="grey75")
            response_enter = tk.Text(educatuin_tab, name="response_enter", height=1.5, width=70)
            response_enter.grid(row=2, column=0, sticky=tk.W)
            # Run button for Neat using a thread
            check_answer = tk.Button(educatuin_tab, text="Check answer",
                                     command=lambda: self.check_answer(value,response_enter),
                                     justify=tk.LEFT, anchor="w")
            check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        elif value == "Components of a neural network":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            neuron_tab_pic = ImageTk.PhotoImage(file="Components_of_Neural_Network.png")
            neuron_tab_label = tk.Label(educatuin_tab, image=neuron_tab_pic)
            neuron_tab_label.image = neuron_tab_pic
            neuron_tab_label.grid(row=1, column=0)
            neuron_tab_label.config(fg="grey75", bg="grey75")
        elif value == "NEAT Config File":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            check_answer = tk.Button(educatuin_tab, text="Start",
                                     command=lambda: self.automate(hidden_level_text,educatuin_tab),
                                     justify=tk.LEFT, anchor="w")
            check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        elif value == "Load Winner/Checkpoints E1":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            check_answer = tk.Button(educatuin_tab, text="See Winner/Checkpoint(s)",
                                     command=lambda: self.automate(hidden_level_text, educatuin_tab),
                                     justify=tk.LEFT, anchor="w")
            check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        elif value == "'Load Winner/Checkpoints E2":
            if label2 != "":
                self.hide_old_widgets(label2)
            if label1 != "":
                self.hide_old_widgets(label1)
            if chat_bot_dynamic_learn != "":
                self.hide_old_widgets(chat_bot_dynamic_learn)
            if response_enter != "":
                self.hide_old_widgets(response_enter)
            if chatbot_next != "":
                self.hide_old_widgets(chatbot_next)
            if perceptron_label != "":
                self.hide_old_widgets(perceptron_label)
            if check_answer != "":
                self.hide_old_widgets(check_answer)
            check_answer = tk.Button(educatuin_tab, text="See Winner/Checkpoint(s)",
                                     command=lambda: self.automate(hidden_level_text, educatuin_tab),
                                     justify=tk.LEFT, anchor="w")
            check_answer.grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)

def Activate_Content(education_option_selected, educatuin_tab, hidden_level_text):
    toolTip = Education_tab(education_option_selected)
    widget_name = education_option_selected._name
    def load_content(event):
        toolTip.load_content(education_option_selected,educatuin_tab, hidden_level_text)

    education_option_selected.bind('<<ListboxSelect>>', load_content)
def DarkMode():
    for education_label in education_mode_labels:
        try:
            exec(education_label + '.config(bg = "grey75")')
        except:
            pass