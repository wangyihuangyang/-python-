


class student:
    def __init__(self,name,xuehao,score):#保存信息
        self.name=name
        self.xuehao=xuehao
        self.score=score
    #定义打印信息方法
    def printinfo(self):
        print(f"姓名：{self.name}")
        print(f"学号：{self.xuehao}")
        print(f"成绩：{self.score}")

class stumanager:
    def __init__(self):
        self.list=[]
        self.totalscore=0
        self.stusum=0
    #添加学生的方法
    def addstu(self,name,xuehao,score):
        try:
            xuehao=int(xuehao)
            score=float(score)
            newstu=student(name,xuehao,score)
            self.list.append(newstu)
            self.totalscore+=newstu.score
            self.stusum+=1
        except ValueError:
            print("格式错误")
    #平均学生的方法
    def average(self):
        if self.stusum>0:
            return float(self.totalscore/self.stusum)
        return 0
    #查找分最高的学生
    def maxstu(self):
        if self.stusum==0:
            return None
        max=self.list[0]
        for stu in self.list:
            if stu.score>max.score:
                max=stu
        return max
    #查找分最低的学生
    def minstu(self):
        if self.stusum==0:
            return None
        min=self.list[0]
        for stu in self.list:
            if stu.score<min.score:
                min=stu
        return min
    def generatereport(self):
        print("==" * 20)
        print(' ' * 8 + "学生成绩统计报告")
        print("==" * 20)
        print("\n")
        print("所有学生信息：")
        for stu in self.list:
            print(f"姓名：{stu.name}")
            print(f"学号：{stu.xuehao}")
            print(f"成绩：{stu.score}")
            print("-"*20)
        print("\n")
        print(f"学生总人数：{self.stusum}")
        print(f"平均成绩：{round(self.average(),2)}")
        print(f"最高分：{round(self.maxstu().score,1)} - {self.maxstu().name}({self.maxstu().xuehao})")
        print(f"最低分：{round(self.minstu().score, 1)} - {self.minstu().name}({self.minstu().xuehao})")
        print("=" * 40)
def main():
    stu_manager=stumanager()
    while True:
        name=input("请输入学生姓名(输入”结束“结束输入)：")
        if name=="结束":break
        xuehao=input("请输入学生学号：")
        score=input("请输入学生成绩：")
        stu_manager.addstu(name,xuehao,score)
    if stu_manager.minstu()==None:
        print("你还没输入东西，就输入结束了？")
    else:
        stu_manager.generatereport()

if __name__=="__main__":
    main()





