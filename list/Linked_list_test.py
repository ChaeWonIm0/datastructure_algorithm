# 제약조건
# 뭐 어쨋든 20글자 이하. idx(step)는 100 이하
# lower case

## 사이트에서 기본 제공
# class BrowserHistory:
#     def __init__():
    
#     def visit():

#     def back():

#     def forward():
class Node:
    def __init__(self, url=0,next=None,preview=None):
        self.url=url
        self.next=next
        self.preview=preview
class BrowserHistory(object):
    def __init__(self,homepage:str):
        self.head=self.current=Node(url=homepage)
    def visit(self,url:str):
        self.current.next = Node(url=url,preview=self.current)
        self.current=self.current.next
        return None
    def back(self,steps:int):
        while steps>0 and self.current.preview!=None:
            steps-=1
            self.current=self.current.preview
        return self.current.url

    def forward(self,steps:int):
        while steps>0 and self.current.next!=None:
            steps-=1
            self.current=self.current.next
        return self.current.url
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.back(1)
# browserHistory.back(1)
# browserHistory.forward(1)
# browserHistory.visit("linkedin.com")
# browserHistory.forward(2)
# browserHistory.back(2)
# browserHistory.back(7)


