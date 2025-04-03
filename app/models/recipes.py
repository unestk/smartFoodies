import datetime
from typing import List

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship
from sqlalchemy.testing.schema import mapped_column, Table


class Base(DeclarativeBase):
    pass


association_table = Table(
    "association_table",
    Base.metadata,
    Column("recipes_id", ForeignKey("recipes.id"), primary_key=True),
    Column("components_id", ForeignKey("components.id"), primary_key=True),
    Column("ingredients_id", ForeignKey("ingredients.id"), primary_key=True),
)


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    type: Mapped[str] = mapped_column()  # Default selectable types
    preparation_time: Mapped[int] = mapped_column()
    servings: Mapped[int] = mapped_column()
    api_id: Mapped[int] = mapped_column()
    image_link: Mapped[str] = mapped_column()
    rating: Mapped[float] = mapped_column()
    suggestions: Mapped[bool] = mapped_column()
    recipe_link: Mapped[str] = mapped_column()
    components: Mapped[List["Component"]] = relationship(
        secondary=association_table, back_populates="recipes"
    )
    ingredients: Mapped[List["Ingredient"]] = relationship(
        secondary=association_table, back_populates="recipes"
    )


class Component(Base):
    __tablename__ = "components"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    type: Mapped[str] = mapped_column()  # Default selectable types
    weight: Mapped[float] = mapped_column()
    quantity: Mapped[float] = mapped_column()
    unit: Mapped[str] = mapped_column()  # Default selectable types
    recipes: Mapped[List["Recipe"]] = relationship(
        secondary=association_table, back_populates="components"
    )
    ingredients: Mapped[List["Ingredient"]] = relationship(
        secondary=association_table, back_populates="components"
    )


class Ingredient(Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    type: Mapped[str] = mapped_column()  # Default selectable types
    weight: Mapped[float] = mapped_column()
    quantity: Mapped[float] = mapped_column()
    unit: Mapped[str] = mapped_column()  # Default selectable types
    expiration: Mapped[datetime.date] = mapped_column()
    recipes: Mapped[List["Recipe"]] = relationship(
        secondary=association_table, back_populates="ingredients"
    )
    components: Mapped[List["Component"]] = relationship(
        secondary=association_table, back_populates="ingredients"
    )
