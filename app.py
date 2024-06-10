from database.setup import create_tables
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def create_author(name="mimi"):
    try:
        author = Author(name=name)
        author.save()
        print(f"Author created: ID - {author.id}, Name - {author.name}")
        return author
    except Exception as e:
        print(f"Error creating author: {str(e)}")
        return None

def create_magazine(category):
    try:
        magazine = Magazine(name="Movies", category=category)
        magazine.save()
        print(f"Magazine created: ID - {magazine.id}, Name - {magazine.name}, Category - {magazine.category}")
        return magazine
    except Exception as e:
        print(f"Error creating magazine: {str(e)}")
        return None

def create_article(author, magazine):
    try:
        title = "Romantic Movies in 2024"
        content = "Content about romantic movies released in 2024."
        article = Article(title=title, author=author, magazine=magazine, content=content)
        article.save()
        print(f"Article created: ID - {article.id}, Title - {article.title}, Author - {article.author.name}, Magazine - {article.magazine.name}")
    except Exception as e:
        print(f"Error creating article: {str(e)}")

def main():
    try:
        create_tables()

      
        author = create_author()

        
        magazine_category = input("Input the magazine category: ").strip()
        magazine = create_magazine(magazine_category)

        
        if author and magazine:
            create_article(author, magazine)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
