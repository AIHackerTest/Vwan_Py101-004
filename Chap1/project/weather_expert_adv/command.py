class Command(object):
    commands = ['help','quit','history']
    def __init__(self):
        pass

    def help(self):
        help_doc = """
        - 输入城市名，返回该城市的天气数据；
        - 输入指令 h 或 help，打印帮助文档；
        - 输入指令 quit 或 exit，退出本程序；
        - 输入指令 history，打印查询过的所有城市。
        """
        print(help_doc)

    def quit(self):
        from sys import exit
        self.history()
        exit(0)

    def history(self,user):
        return user.history.show_records()
