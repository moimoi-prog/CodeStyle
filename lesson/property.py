# プロパティの設定
# 変数の前に_をつける(１つだけだと外部から直接指定できる。２つだと外部から指定できない)
# 変数と同名のメソッドを定義して、returnでその変数を返すようにする。
# 使用方法　条件を満たした場合に、変更可能にするときに使用する。


class Car(object):
    def __init__(self, model = None, passwd = "1234"):
        self._model = model
        self.passwd = passwd

    @property
    def model(self):
        return self.model

    @model.setter
    def model(self, name):
        if self.passwd == "1234":
            model = name
        else:
            ValueError


