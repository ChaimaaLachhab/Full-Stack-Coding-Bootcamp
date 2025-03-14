class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items is not None else []
        self.pageSize = int(pageSize)
        self.totalPages = max(1, -(-len(self.items) // self.pageSize))
        self.currentPage = 1

    def getVisibleItems(self):
        start_index = (self.currentPage - 1) * self.pageSize
        end_index = start_index + self.pageSize
        return self.items[start_index:end_index]

    def prevPage(self):
        self.currentPage = max(1, self.currentPage - 1)
        return self

    def nextPage(self):
        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        self.currentPage = max(1, min(self.totalPages, int(pageNum)))
        return self

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
print(p.getVisibleItems())

p.nextPage()
print(p.getVisibleItems())

p.lastPage()
print(p.getVisibleItems())
