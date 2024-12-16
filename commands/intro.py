from commands.base_command import BaseCommand
from prettytable import PrettyTable

class Introduce(BaseCommand):

    def execute(self, args):
        anggotaTable = PrettyTable()
        anggotaTable.field_names =['No', 'Nama', 'Kelas', 'NIM']
        anggotaTable.add_row(['1.', 'Hadi Kurniawan', '15.1D.01', '15240026'])
        anggotaTable.add_row(['2.', 'Teguh Aulia Darmawan', '15.1D.01', '15240026'])
        anggotaTable.add_row(['3.', 'Siti Jeni', '15.1D.01', '15240026'])
        anggotaTable.add_row(['4.', 'Iqbal', '15.1D.01', '15240026'])
        anggotaTable.add_row(['5.', 'Nanda', '15.1D.01', '15240026'])
        anggotaTable.add_row(['6.', 'Akhrulyan', '15.1D.01', '15240026'])
        anggotaTable.align['Nama'] = 'l'
        print(anggotaTable)
    
    def help(self):
        return "Usage: greet [name]\n  Menyapa seseorang dengan nama tertentu."
