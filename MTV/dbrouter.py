import random
from django.db import transaction

class MultiDBRouter(object):
    def db_for_read(self, model, **hints):
        @staticmethod
        def db_for_read(model, **hints):
            transaction.get_autocommit()
            conn = transaction.get_connection('default')
            if conn.in_atomic_block:
                return 'default'
        databases = ['default', 'readonly']
        print("is read traffic")
        return random.choice(databases)

    def db_for_write(self, model, **hints):
        print("is write traffic")
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True