class Magazine:
    def __init__(self, name=None, category=None):
        self.name = name
        self.category = category

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def set_category(self, new_category):
        if not isinstance(new_category, str) or len(new_category.strip()) == 0:
            raise ValueError("  Invalid category name.")
        self.category = new_category
