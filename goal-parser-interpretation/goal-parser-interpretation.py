class Solution:
    def interpret(self, command: str) -> str:
        dic = {'()':'o', '(al)':'al'}
        command = command.replace('()',dic['()'])
        command = command.replace('(al)',dic['(al)'])
        return command
