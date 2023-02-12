from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self,category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self,topic:Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self,document:Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self,category_id: int, new_name:str):
        for category in self.categories:
            if category_id == category.id:
                category.name = new_name

    def edit_topic(self,topic_id: int, new_topic: str, new_storage_folder: str):
        for topic in self.topics:
            if topic_id == topic.id:
                topic.topic = new_topic
                topic.storage_folder = new_storage_folder

    def edit_document(self,document_id: int, new_file_name: str):
        for document in self.documents:
            if document_id == document.id:
                document.file_name = new_file_name

    def delete_category(self, category_id):
        self.categories.remove([c for c in self.categories if c.id == category_id][0])

    def delete_topic(self, topic_id):
        self.topics.remove([c for c in self.topics if c.id == topic_id][0])

    def delete_document(self, document_id):
        self.documents.remove([c for c in self.documents if c.id == document_id][0])

    def get_document(self,document_id):
        for document in self.documents:
            if document.id == document_id:
                return document

    def __repr__(self):
        output = ""
        for document in self.documents:
            output += f"{document}\n"
        return output


# class Storage:
#     def __init__(self):
#         self.categories = []
#         self.topics = []
#         self.documents = []
#
#     def add_category(self, category: Category):
#         if category not in self.categories:
#             self.categories.append(category)
#
#     def add_topic(self, topic: Topic):
#         if topic not in self.topics:
#             self.topics.append(topic)
#
#     def add_document(self, document: Document):
#         if document not in self.documents:
#             self.documents.append(document)
#
#     def edit_category(self, category_id: int, new_name: str):
#         category = [c for c in self.categories if c.id == category_id][0]
#         category.edit(new_name)
#
#     def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
#         topic = [c for c in self.topics if c.id == topic_id][0]
#         topic.edit(new_topic, new_storage_folder)
#
#     def edit_document(self, document_id: int, new_file_name: str):
#         document = [c for c in self.documents if c.id == document_id][0]
#         document.edit(new_file_name)
#
#     def delete_category(self, category_id):
#         self.categories.remove([c for c in self.categories if c.id == category_id][0])
#
#     def delete_topic(self, topic_id):
#         self.topics.remove([c for c in self.topics if c.id == topic_id][0])
#
#     def delete_document(self, document_id):
#         self.documents.remove([c for c in self.documents if c.id == document_id][0])
#
#     def get_document(self, document_id):
#         document = [c for c in self.documents if c.id == document_id][0]
#         return document
#
#     def __repr__(self):
#         return "\n".join([str(d) for d in self.documents])
#