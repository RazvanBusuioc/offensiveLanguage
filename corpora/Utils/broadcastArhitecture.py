
class Comment:
    def __init__(self, sender, text, timestamp, numberOfReacts) -> None:
        self.sender = sender
        self.text = text
        self.timestamp = timestamp
        self.numberOfReacts = numberOfReacts
    
    # def __init__(self, list) -> None:
    #     self.sender = list[0]
    #     self.text = list[1]
    #     self.numberOfReacts = list[2]
    
    def setNumberOfReacts(self, numberOfReacts) -> None:
        self.numberOfReacts = numberOfReacts

    def __eq__(self, __o: object) -> bool:
        return self.sender == __o.sender and self.text == __o.text
    
    def __hash__(self) -> int:
        return hash((self.sender, self.text))

class FacebookBroadcast:

    def __init__(self) -> None:
        self.comments = []

    def addComment(self, comment):
        if comment not in self.comments:
            self.comments.append(comment)
        else:
            idx = self.comments.index(comment)
            if self.comments[idx].numberOfReacts != comment.numberOfReacts:
                self.comments[idx].setNumberOfReacts(comment.numberOfReacts)

    def setTitle(self, title):
        self.title = title
    
    def setDescription(self, description):
        self.description = description
    
    def setNumberOfReacts(self, numberOfReacts):
        self.numberOfReacts = numberOfReacts

    def setURL(self, URL):
        self.URL = URL
    
    def getTitle(self):
        return self.title