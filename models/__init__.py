# coding: utf-8

from __future__ import absolute_import
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
# import models into model package
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model

class Category(Model, Base):

    __tablename__ = 'Category'
    _id = Column(Integer, primary_key=True)
    _name = Column(String)

    def __init__(self, id: int=None, name: str=None):
        """
        Category - a model defined in Swagger

        :param id: The id of this Category.
        :type id: int
        :param name: The name of this Category.
        :type name: str
        """
        self.swagger_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'Category':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Category of this Category.
        :rtype: Category
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Category.

        :return: The id of this Category.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Category.

        :param id: The id of this Category.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Category.

        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Category.

        :param name: The name of this Category.
        :type name: str
        """

        self._name = name

class Pet(Model, Base):

    __tablename__ = 'Pet'
    _id = Column(Integer, primary_key=True)
    _category_id = Column(Integer, ForeignKey('Category._id'))
    _status = Column(String)
    _name = Column(String)
    _category = relationship("Category")

    def __init__(self, id: int=None, category: Category=None, name: str=None, status: str=None):
        """
        Pet - a model defined in Swagger

        :param id: The id of this Pet.
        :type id: int
        :param category: The category of this Pet.
        :type category: Category
        :param name: The name of this Pet.
        :type name: str
        :param status: The status of this Pet.
        :type status: str
        """
        self.swagger_types = {
            'id': int,
            'category': Category,
            'name': str,
            'status': str
        }

        self.attribute_map = {
            'id': 'id',
            'category': 'category',
            'name': 'name',
            'status': 'status'
        }

        self._id = id
        self._category = category
        self._name = name
        self._status = status

    @classmethod
    def from_dict(cls, dikt) -> 'Pet':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pet of this Pet.
        :rtype: Pet
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Pet.

        :return: The id of this Pet.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Pet.

        :param id: The id of this Pet.
        :type id: int
        """

        self._id = id

    @property
    def category(self) -> Category:
        """
        Gets the category of this Pet.

        :return: The category of this Pet.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category: Category):
        """
        Sets the category of this Pet.

        :param category: The category of this Pet.
        :type category: Category
        """

        self._category = category

    @property
    def name(self) -> str:
        """
        Gets the name of this Pet.

        :return: The name of this Pet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Pet.

        :param name: The name of this Pet.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def status(self) -> str:
        """
        Gets the status of this Pet.
        pet status in the store

        :return: The status of this Pet.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status: str):
        """
        Sets the status of this Pet.
        pet status in the store

        :param status: The status of this Pet.
        :type status: str
        """
        allowed_values = ["available", "pending", "sold"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status
