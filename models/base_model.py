#!/usr/bin/python3
from datetime import datetime
import uuid
import models


class BaseModel:
    """The base class for all storage objects in this project"""
    def __init__(self, *args, **kwargs):
        """
        initialize class object

        **Arguments**
           none: a unique user id and timestamp will be created
           args: a sequence, this should not be used, please pass a dictionary
                 as **dictionary
           kwargs: a dictionay, if the id and timestamp are missing they will
                   be created
        """
        fix = {}
        if args: # this is not the right way to handle kwargs
            fix = args[0]
        if kwargs or fix:
            if fix:
                kwargs = fix
            flag_id = False
            flag_created_at = False
            for k in kwargs.keys():
                if k == "created_at" or k == "updated_at":
                    if k == "created_at":
                        flag_created_at = True
                    if not isinstance(kwargs[k], datetime):
                        kwargs[k] = datetime(*self.__str_to_numbers(kwargs[k]))
                elif k == "id":
                    flag_id = True
                setattr(self, k, kwargs[k])
            if not flag_created_at:
                self.created_at = datetime.now()
            if not flag_id:
                self.id = str(uuid.uuid4())
        elif not args:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())

    def __str_to_numbers(self, s):
        """
        Prepares a string for datetime

        **Arguments**
           s: a string of numbers
        """
        tmp = ''.join([o if o not in "T;:.,-_" else " " for o in s]).split()
        res = [int(i) for i in tmp]
        return res


    def save(self):
        """method to update self"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """edit string representation"""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_json(self):
        """convert to json"""
        dupe = self.__dict__.copy()
        dupe["created_at"] = dupe["created_at"].isoformat()
        if ("updated_at" in dupe):
            dupe["updated_at"] = dupe["updated_at"].isoformat()
        dupe["__class__"] = type(self).__name__
        return dupe
