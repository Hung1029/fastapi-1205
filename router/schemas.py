from pydantic import BaseModel
from typing import List


class ArticleRequestSchema(BaseModel):
    title: str
    sku: str
    description: str
    description_long: str
    owner_id: int


class ArticleResponseSchema(ArticleRequestSchema):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class OnlyArticleResponseSchema(ArticleRequestSchema):
    pass

    class Config:
        orm_mode = True


class UserRequestSchema(BaseModel):
    username: str
    email: str


class UserResponseSchema(UserRequestSchema):
    id: int
    created_article: List[ArticleResponseSchema] = []

    class Config:
        orm_mode = True


class OnlyUserResponseSchema(UserResponseSchema):
    pass

    class Config:
        orm_mode = True


class CommentRequestSchema(BaseModel):
    username: str
    content: str
    article_id: int
    user_id: int


class CommentResponseSchema(CommentRequestSchema):
    id: int
    article_id: int
    user_id: int

    class Config:
        orm_mode = True


class OnlyCommentResponseSchema(CommentResponseSchema):
    pass

    class Config:
        orm_mode = True


class LikeRequestSchema(BaseModel):
    username: str
    article_id: int
    user_id: int


class LikeResponseSchema(LikeRequestSchema):
    id: int
    article_id: int
    user_id: int

    class Config:
        orm_mode = True


class ArticleResponseWithUserSchema(ArticleRequestSchema):
    id: int
    owner_id: int
    owner: OnlyUserResponseSchema
    comment_article: List[OnlyCommentResponseSchema] = []
    like_article: List[LikeResponseSchema] = []

    class Config:
        orm_mode = True


class UserResponseWithArticleSchema(UserRequestSchema):
    id: int
    created_articles: List[OnlyArticleResponseSchema] = []
    comment_user:  List[OnlyCommentResponseSchema] = []
    like_user:  List[LikeResponseSchema] = []

    class Config:
        orm_mode = True
