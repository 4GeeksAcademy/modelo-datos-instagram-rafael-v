from sqlalchemy import Boolean, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from flask_sqlalchemy import SQLAlchemy

# Si estás usando Flask, necesitarás definir el objeto db
db = SQLAlchemy()  # Esto se crea después de la inicialización de Flask, por ejemplo en app.py

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    post: Mapped[List["Post"]] = relationship("Post", back_populates="user")
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "location": self.location,
            # do not serialize the password, it's a security breach
        }


class Follower(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column(String(100))
    comments: Mapped[str] = mapped_column(String(250))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship("User")
    
    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "comments": self.comments,
            "user_id": self.user_id,
        }


class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column(String(100))
    comments: Mapped[str] = mapped_column(String(250))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship("User", back_populates="post")
    media: Mapped[List["Media"]] = relationship("Media", back_populates="post")
    comment: Mapped[List["Comment"]] = relationship("Comment", back_populates="post")
    
    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "comments": self.comments,
            "user_id": self.user_id,
        }


class Media(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    photo: Mapped[str] = mapped_column(String(100))
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    post: Mapped["Post"] = relationship("Post", back_populates="media")
    
    def serialize(self):
        return {
            "id": self.id,
            "photo": self.photo,
            "post_id": self.post_id,
        }


class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    answers: Mapped[str] = mapped_column(String(250))
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user: Mapped["User"] = relationship("User")
    post_id: Mapped[int] = mapped_column(ForeignKey('post.id'))
    post: Mapped["Post"] = relationship("Post", back_populates="comment")
    
    def serialize(self):
        return {
            "id": self.id,
            "answers": self.answers,
            "user_id": self.user_id,
            "post_id": self.post_id,
        }
