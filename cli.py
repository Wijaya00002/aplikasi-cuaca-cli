import cmd
import argparse
from commands.greet import GreetCommand
from commands.intro import Introduce
import os

class App(cmd.Cmd):
    prompt = 'cuaca-app>'
    intro = 'Selamat datang di aplikasi Ramalan Cuaca CLI. Made by : Kelompok Pemograman Dasar 1\n'

    def __init__(self):
        super().__init__()
        self.commands = {
            "greet" : GreetCommand(),
            "introduction" : Introduce()
        }

    def parse_and_execute(self, command_name, arg_string):
        print(command_name, arg_string)
        command = self.commands.get(command_name)
        if not command:
            print(f"Unknown command: {command_name}")
            return
        parser = argparse.ArgumentParser(prog=command_name)
        command.add_arguments(parser)
        try:
            args = parser.parse_args(arg_string.split())
            print(command.execute(args))
        except SystemExit:
            pass

    def do_help(self, arg):
        if arg in self.commands:
            print(self.commands[arg].help())
        else:
            print("commands yang tersedia:")
            for command in self.commands:
                print(f"  {command}")
        
    def do_exit(self, args):
        return True

    def do_clear(self, args):
        os.system('cls' if os.name == 'nt' else 'clear')

    def do_greet(self, args):
        self.parse_and_execute("greet", args)

    def default(self, line):
        print(f"command tidak di ketahui: {line}")

    def do_intro(self, args):
        self.commands["introduction"].execute(args)


class StartApplication(App):
    def __init__(self, app : str):
        parser = argparse.ArgumentParser()
        parser.add_argument('command', choices=['start'])
        args = parser.parse_args()
        self.cmd = args.command
        self.app = app
        if args.command == 'start':
            App().cmdloop(self.app)
        else:
            print("arguments required")

