class RangeLexer:
    def __init__(self, text: str):
        self.__text = text
        self.__pos = 0

    def getNextToken(self) -> dict[str, str]:
        output = { 'Type': 'EOS', 'Value': '' }
        while not self.__eos:
            if self.__current.isdigit():
                output = { 'Type': 'INTEGER', 'Value': self.__integer() }
                break
            elif self.__current == '~':
                self.__advance()
                output = { 'Type': 'TILDE', 'Value': '~' }
                break
            elif self.__current == ',':
                self.__advance()
                output = { 'Type': 'COMMA', 'Value': ',' }
                break
            elif self.__current == '-':
                self.__advance()
                output = { 'Type': 'MINUS', 'Value': '-' }
                break
            elif self.__current == '減' and self.__peek() == '少':
                self.__advance()
                self.__advance()
                output = { 'Type': 'MINUS', 'Value': '-' }
                break
            else:
                self.__advance()
        return output

    def __integer(self) -> str:
        num = ''
        while self.__current.isdigit() and not self.__eos:
            num += self.__current
            self.__advance()
        return num

    def __advance(self):
        self.__pos += 1

    def __peek(self):
        if self.__pos + 1 > len(self.__text) - 1:
            return ''
        else:
            return self.__text[self.__pos + 1]

    @property
    def __current(self) -> str:
        if self.__pos > len(self.__text) - 1:
            return ''
        else:
            return self.__text[self.__pos]

    @property
    def __eos(self) -> bool:
        return self.__current == ''
