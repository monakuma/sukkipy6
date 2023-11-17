class Hero:
    name="松田"
  
    def __init__(self,name="松田",hp=35) -> None:
        self.name=name
        self.hp=hp
    
    def sleep(self,hours):
        print(f'{self.name}は{hours}時間寝た！')
        self.hp +=hours


print('スッキリファンタジーXⅡ ～金色の理想郷～')
h=Hero()
h.sleep(3)
print(f'{h.name}のHPは現在{h.hp}です')

