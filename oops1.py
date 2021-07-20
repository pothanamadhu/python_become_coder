class Students:
      def __init__(self,roll,sec,clg,per,att):
            self.roll=roll
            self.sec=sec
            self.clg=clg
            self.per=per
            self.att=att
      def display(self):
            print(self.roll,self.sec,self.clg,self.per,self.att)
std1=Students("4n8","ece4","acet",82.38,51)
std1.display()
