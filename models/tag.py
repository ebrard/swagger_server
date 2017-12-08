# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref

Base = declarative_base()

association_table = Table('PetTags', Base.metadata,
    Column('pet_id', Integer, ForeignKey('Pet._id')),
    Column('tag_id', Integer, ForeignKey('Tag._id'))
)

class Tag(Model, Base):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    __tablename__ = 'Tag'
    _id = Column(Integer, primary_key=True)
    _name = Column(String)

    pet = relationship("pet", back_populates="tag", secondary=association_table)

    def __init__(self, id: int=None, name: str=None):
        """
        Tag - a model defined in Swagger

        :param id: The id of this Tag.
        :type id: int
        :param name: The name of this Tag.
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
    def from_dict(cls, dikt) -> 'Tag':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tag of this Tag.
        :rtype: Tag
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this Tag.

        :return: The id of this Tag.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this Tag.

        :param id: The id of this Tag.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this Tag.

        :return: The name of this Tag.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Tag.

        :param name: The name of this Tag.
        :type name: str
        """

        self._name = name

