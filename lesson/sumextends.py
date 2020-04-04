# 多重継承 (バグに繋がったりするので、しないほうがいい)
# 同名メソッドは引数の若い順に優先される。

# クラス変数
# クラスそのものに属している変数

# クラス変数は、インスタンス化しなくてもアクセスできる。

# クラスメソッドの生成方法
# propertyでclassmethodを指定する(引数はself出なくてcls)

# staticmethodの生成方法
# propertyでstaticethodを指定する(引数は不要)　← あまり使わない

# 特殊メソッド
# __str__ .. 文字列として扱いたい場合に呼び出される。
# __len__ .. 長さを取得したい場合に使用する
# __add__ .. クラス同士の足し算を行いたいときに使用する
# __equal__ .. 比較したいときに使用する

class Person(object):
    kind = "human"

    def talk(self):
        print("talk")

    @classmethod
    def what_kind(cls):
        print(cls.kind)

class Car(object):
    def run(self):
        print("run")

class PersonCarRobot(Person, Car):
    def fly(self):
        print("fly")

carrobot = PersonCarRobot()

carrobot.talk()
carrobot.run()
carrobot.fly()

Person.what_kind()

