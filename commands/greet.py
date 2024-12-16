from commands.base_command import BaseCommand

class GreetCommand(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", type=str, required=True, help="nama user")

    def execute(self, args):
        if args.name:
            print(f"Hello, {args.name}!")
        else:
            print("Hello, World!")
    
    def help(self):
        return """Usage: greet\n  
                Menyapa seseorang dengan nama tertentu.
                Parameter: -n [nama]"""
