import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_create_author(self):
        # Arrange
        author_name = "John Doe"
        
        # Act
        author = Author(author_name)
        
        # Assert
        self.assertEqual(author.name, author_name)

    def test_create_article(self):
        # Arrange
        article_title = "Test Title"
        article_content = "Test Content"
        author_name = "John Doe"  # Assuming the author exists
        
        # Act
        author = Author(author_name)
        article = Article(title=article_title, content=article_content, author=author)
        
        # Assert
        self.assertEqual(article.title, article_title)
        self.assertEqual(article.content, article_content)
        self.assertEqual(article.author.name, author_name)

    def test_create_magazine(self):
        # Arrange
        magazine_name = "lidya"
        
        # Act
        magazine = Magazine(name=magazine_name)
        
        # Assert
        self.assertEqual(magazine.name, magazine_name)

if __name__ == "__main__":
    unittest.main()
