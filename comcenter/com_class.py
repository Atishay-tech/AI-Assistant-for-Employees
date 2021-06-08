from comcenter.com_dict import com_dict

class Command:
    com_dict = com_dict

    def __init__(self, text: str='default') -> None:
        keyword, query = self._format_command(text)
        self.set_keyword(keyword)
        self.set_query(query)
    

    def _format_command(self, text: str) -> tuple:
        """Returns text in proper command format keyword, query

        text: query to be executed
        """
        if isinstance(text, str):
            try:
                keyword, query = text.split(maxsplit=1)
                if keyword.lower() not in Command.com_dict.keys():
                    keyword, query = 'google', text

            except:
                if text.lower() in Command.com_dict.keys():
                    keyword, query = text, None
                else:
                    keyword, query = 'google', text

            return keyword.lower(), query

        else:
            print('Not a valid command!')
            return 'default', None


    def set_keyword(self, keyword: str) -> None:
        """Setter for the attribute keyword"""
        if keyword in Command.com_dict:
            self.keyword = keyword.lower()
        else:
            self.keyword = 'default'
            print('Not a valid keyword!')
    

    def get_keyword(self) -> str:
        """Getter for the attribute keyword"""
        return self.keyword
    

    def set_query(self, query: str) -> None:
        """Setter for the attribute query"""
        if isinstance(query, str):
            self.query = query
        else:
            self.query = None
            print('Not a valid query!')
    

    def get_query(self) -> str:
        """Getter for the attribute query"""
        return self.query


    def execute(self):
        """Executes the command"""
        self.com_dict[self.keyword](self.query)


if __name__ == '__main__':
    command = Command()
    command.execute()