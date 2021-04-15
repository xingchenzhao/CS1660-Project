import tkinter as tk
import os
import webbrowser
import subprocess


class GUIApp(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.root.title("Data Science Tool Box")
        self.main_frame = tk.Frame(root)
        self.main_frame.pack()
        self.make_gui()

    def make_gui(self):
        self.rstudio = tk.Button(self.main_frame)
        self.rstudio['text'] = 'RStudio'
        self.rstudio['command'] = self.RStudio
        self.rstudio.pack()

        self.spyder = tk.Button(self.main_frame)
        self.spyder['text'] = 'Spyder'
        self.spyder['command'] = self.Spyder
        self.spyder.pack()

        self.ibmsas = tk.Button(self.main_frame)
        self.ibmsas['text'] = 'IBM SAS'
        self.ibmsas['command'] = self.IBMSAS
        self.ibmsas.pack()

        self.git = tk.Button(self.main_frame)
        self.git['text'] = 'Git'
        self.git['command'] = self.Git
        self.git.pack()

        self.jupyterNotebook = tk.Button(self.main_frame)
        self.jupyterNotebook['text'] = 'Jupyter Notebook'
        self.jupyterNotebook['command'] = self.JupyterNotebook
        self.jupyterNotebook.pack()

        self.orange = tk.Button(self.main_frame)
        self.orange['text'] = 'Orange'
        self.orange['command'] = self.Orange
        self.orange.pack()

        self.vscode = tk.Button(self.main_frame)
        self.vscode['text'] = 'VS Code'
        self.vscode['command'] = self.VSCode
        self.vscode.pack()

        self.hadoop = tk.Button(self.main_frame)
        self.hadoop['text'] = 'Hadoop'
        self.hadoop['command'] = self.Hadoop
        self.hadoop.pack()

        self.spark = tk.Button(self.main_frame)
        self.spark['text'] = 'Spark'
        self.spark['command'] = self.Spark
        self.spark.pack()

        self.tableau = tk.Button(self.main_frame)
        self.tableau['text'] = 'Tableau'
        self.tableau['command'] = self.Tableau
        self.tableau.pack()

        self.sonarcloud = tk.Button(self.main_frame)
        self.sonarcloud['text'] = 'Sonar Cloud'
        self.sonarcloud['command'] = self.SonarCloud
        self.sonarcloud.pack()

        self.tensorflow = tk.Button(self.main_frame)
        self.tensorflow['text'] = 'TensorFlow'
        self.tensorflow['command'] = self.TensorFlow
        self.tensorflow.pack()

        self.markdown = tk.Button(self.main_frame)
        self.markdown['text'] = 'Markdown'
        self.markdown['command'] = self.Markdown
        self.markdown.pack()

    def RStudio(self):
        webbrowser.open('http://host.docker.internal:8787')
        print('Open RStudio')

    def Spyder(self):
        os.system("xterm spyder")
        print('Open Spyder')

    def IBMSAS(self):
        webbrowser.open('https://welcome.oda.sas.com/login')
        print('Open IBM SAS')

    def Git(self):
        os.system("xterm bash")
        print('Open Git')

    def JupyterNotebook(self):
        webbrowser.open('http://host.docker.internal:8888?token=1660')
        print('Open Jupyter Notebook')

    def Orange(self):
        webbrowser.open('http://host.docker.internal:6901')
        print('Open Orange')

    def VSCode(self):
        webbrowser.open('http://host.docker.internal:8080')
        print('Open VSCode')

    def Hadoop(self):
        webbrowser.open('http://host.docker.internal:50070')
        print('Open Hadoop')

    def Spark(self):
        webbrowser.open('http://host.docker.internal:8887?token=spark')
        print('Open Spark')

    def Tableau(self):
        webbrowser.open('https://sso.online.tableau.com/public/idp/SSO')
        print('Open Tableau')

    def SonarCloud(self):
        webbrowser.open('https://sonarcloud.io/sessions/new')
        print('Open SonarCloud')

    def TensorFlow(self):
        webbrowser.open('http://host.docker.internal:8383?token=tensorflow')
        print('Open TensorFlow')

    def Markdown(self):
        webbrowser.open('http://host.docker.internal:12345')
        print('Open Markdown')


root = tk.Tk()
# root.geometry("300x350")
gui = GUIApp(root=root)
gui.mainloop()
