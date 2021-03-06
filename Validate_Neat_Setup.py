import re
import sys
import gym

games_available = ['SpaceInvaders-v0', "Berzerk-v0", "Boxing-v0", 'Freeway-v0', 'Frostbite-v0', "Kangaroo-v0",
                            "KungFuMaster-v0",
                            "Pong-v0", "Alien-v0", "Asterix-v0", "Asteroids-v0",
                            "Amidar-v0", "Assault-v0", "Atlantis-v0", "BattleZone-v0",
                            "Carnival-v0", "Centipede-v0", "DemonAttack-v0",
                            "JourneyEscape-v0", "Phoenix-v0",
                            "Pooyan-v0", "StarGunner-v0",
                            "TimePilot-v0", "UpNDown-v0",  "LunarLander-v2", "CartPole-v1"
                            ]
game_evaluation_choice = ["Single-Processing"] #, "Multi-Processing"]
network_type_choice = ["Feed-forward", "Recurrent"]
render_window_choice = ["True", "False"]
choose_config_file_choice = ["From Text Editor", "Choose file from directory"]
game_list_2D = [ "LunarLander-v2", "CartPole-v1"]

class Validate_Neat(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def validate_spinbox(self,widget_name,label, style, widget):
        sys.__stdout__
        sys.__stderr__
        text = widget.get()
        bg = style.lookup('TFrame', 'background')
        if widget_name == "game_selection" or widget_name == "game_selection_winner":
            if str(text) in games_available:
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "game_evaluation":
            if str(text) in game_evaluation_choice:
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "network_type" or widget_name == "network_type_winner":
            if text in network_type_choice:
                if str(bg) == "grey75":
                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "render_window":
            if text in render_window_choice:
                if str(bg) == "grey75":
                    #print(bg)
                    label.config(fg="black")
                else:
                    #print(bg)
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "choose_config_file" or widget_name == "choose_config_file_winner":
            if text in choose_config_file_choice:
                if str(bg) == "grey75":
                    #print(bg)
                    label.config(fg="black")
                else:
                    #print(bg)
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
        if widget_name == "game_checkpoint":
            if text.find("-") == 0:
                text = text.replace("-", "")
            if text == "":
                label.config(fg="red")
                return
            if re.search('[a-zA-Z]', text):
                widget.set("")
                label.config(fg="red")
                return
            if text.isdigit():
                if int(text) > 0:
                    widget.set(int(text))
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        #print(bg)
                        label.config(fg="white")
                elif int(text) == 0:
                    widget.set("0")
                else:
                    widget.set("")
                    label.config(fg="red")
            else:
                if float(text) or text == "0.0":
                    widget.set(int(float(text)))
                else:
                    widget.set("")
                    label.config(fg="red")
        if widget_name == "num_generations" or widget_name == "number_of_genomes" or widget_name == "ep_per_genome":
            try:
                if text.find("-") == 0:
                    text = text.replace("-", "")
                if text == "":
                    widget.set("1")
                    return
                if re.search('[a-zA-Z]', text):
                    widget.set("1")
                    return
                if text.isdigit():
                    if int(text) > 0:
                        widget.set(int(text))
                        if str(bg) == "grey75":
                            label.config(fg="black")
                        else:
                            #print(bg)
                            label.config(fg="white")
                    elif int(text) == 0:
                        widget.set("1")
                    else:
                        widget.set("1")

                else:
                    if float(text) or text == "0.0":
                        widget.set("1")
                    else:
                        widget.set("1")

            except:
                widget.set("1")
        if widget_name == "runs_per_network":
            try:
                if text == "0.0" or text == "0":
                    widget.set("1")
                if int(text):
                    if str(bg) == "grey75":
                        label.config(fg="black")
                    else:
                        #print(bg)
                        label.config(fg="white")
                else:
                    widget.set("1")
            except ValueError:
                try:
                    if float(text):
                        widget.set(int(text))
                except:
                    widget.set("1")


    def validate_spinbox_game(self, widget_name, label, style, widget, input, output):
        text = widget.get()
        if widget_name == "game_selection_config":
            try:
                env = gym.make(text)
                outputs = env.action_space
                env_ob_space = env.observation_space
                string_space = str(env_ob_space)
                output.set(int(re.search(r'\d+', str(outputs)).group()))
                if text in games_available:
                    if text in game_list_2D:
                        start = ', ('
                        end = ',)'
                        input.set(string_space[str(string_space).find(start)+len(start):str(string_space).rfind(end)])
                    else:
                        input.set("1092")
            except:
                print("Error")


    def validate_Game_selection(self, widget_name,label,style,widget,runs_per_network_l, runs_per_network):
        text = widget.get()
        if widget_name == "game_selection":
            if text in game_list_2D:
                runs_per_network_l.grid()
                runs_per_network.grid()
            else:
                runs_per_network_l.grid_remove()
                runs_per_network.grid_remove()
        bg = style.lookup('TFrame', 'background')
        if widget_name == "game_selection":
            if str(text) in games_available:
                if str(bg) == "grey75":

                    label.config(fg="black")
                else:
                    label.config(fg="white")
            else:
                widget.set("")
                label.config(fg="red")
def ValidateInputNEAT(widget, label, style):
    toolTip = Validate_Neat(widget)
    widget_name = widget._name

    def leave(event):
        toolTip.validate_spinbox(widget_name,label, style, widget)

    widget.bind('<FocusOut>', leave)
def Validate_Gym_Game(widget, label, style, input, output):
    toolTip = Validate_Neat(widget)
    widget_name = widget._name

    def leave(event):
        toolTip.validate_spinbox_game(widget_name, label, style, widget, input, output)

    widget.bind('<FocusOut>', leave)

def Validate_Game_Selection(widget,label,style,runs_per_network_l, runs_per_network):
    toolTip = Validate_Neat(widget)
    widget_name = widget._name

    def leave(event):
        toolTip.validate_Game_selection(widget_name,label,style,widget,runs_per_network_l, runs_per_network)

    widget.bind('<FocusOut>', leave)



