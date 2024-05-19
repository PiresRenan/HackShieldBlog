from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


# Modelo para o usuário
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)

    # Relacionamento com posts (um usuário pode ter vários posts)
    posts = relationship("BlogPost", back_populates="author")
    # Relacionamento com comentários (um usuário pode ter vários comentários)
    comments = relationship("Comment", back_populates="comment_author")

    def __repr__(self):
        return f"<User: {self.name} - {self.email}>"


# Modelo para o post do blog
class BlogPost(Base):
    __tablename__ = "blog_posts"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(250), unique=True, nullable=False)
    subtitle = Column(String(250), nullable=False)
    date = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)
    img_url = Column(String(250), nullable=False)

    # Relacionamento com o autor (um post pertence a um usuário)
    author = relationship("User", back_populates="posts")
    # Relacionamento com comentários (um post pode ter vários comentários)
    comments = relationship("Comment", back_populates="parent_post")

    def __repr__(self):
        return f"<BlogPost: {self.title} - {self.author.name}>"


# Modelo para o comentário
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("blog_posts.id"), nullable=False)

    # Relacionamento com o autor do comentário (um comentário pertence a um usuário)
    comment_author = relationship("User", back_populates="comments")
    # Relacionamento com o post (um comentário pertence a um post)
    parent_post = relationship("BlogPost", back_populates="comments")

    def __repr__(self):
        return f"<Comment: {self.text} - {self.comment_author.name}>"
