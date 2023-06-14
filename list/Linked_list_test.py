# 제약조건
# 뭐 어쨋든 20글자 이하. idx(step)는 100 이하
# lower case

# 사이트에서 기본 제공
class Node:
    def __init__(self, url = 0, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev
     
class BrowserHistory(object):

    def __init__(self, homepage):
        # self.head = None
        # self.tail = None
        self.head = self.current = Node(url = homepage)
        # self.head = new_node        

    def visit(self, url) -> None:
        # new_node = Node(url)
        # self.head = None
        # self.tail = None
        # alist = []
        # alist.append(new_node)
        # if self.head is None:
        #     self.head = new_node
        #     self.tail = new_node
        # else:
        #     self.tail.next = new_node
        #     self.tail = self.tail.next
        self.current.next = Node(url=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.url

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.url
browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.back(1)
browserHistory.back(1)
browserHistory.forward(1)
browserHistory.visit("linkedin.com")
browserHistory.forward(2)
browserHistory.back(2)
browserHistory.back(7)


