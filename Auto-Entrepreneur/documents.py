class Document:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.reviews = []

    def review(self, role, review):
        if role.permissions.can_review:
            self.reviews.append((role, review))
        else:
            raise PermissionError(f"{role.name} does not have permission to review documents")

    def approve(self, role):
        if role.permissions.can_approve:
            self.approved = True
        else:
            raise PermissionError(f"{role.name} does not have permission to approve documents")
