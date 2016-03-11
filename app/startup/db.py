# -*- coding: utf-8 -*-

from flask_script import Manager, prompt_bool
from app import db

manager = Manager(usage="Perform database operations")

@manager.command
def drop():
    "Drops database tables"
    if prompt_bool("Are you sure you want to lose all your data"):
        print 'Droping Tables ...'
        try:
            db.drop_all()
        except Exception as e:
            print 'Failed due to exception:{ex}'.format(ex=e)
        else:
            print 'Done'


@manager.command
def create(default_data=True, sample_data=False):
    "Creates database tables from sqlalchemy models"
    print 'Initializing Tables ...'
    try:
        db.create_all()
    except Exception as e:
        print 'Failed due to exception:{ex}'.format(ex=e)
    else:
        print 'Done'


@manager.command
def recreate(default_data=True, sample_data=False):
    "Recreates database tables (same as issuing 'drop' and then 'create')"
    drop()
    create(default_data, sample_data)


@manager.command
def dump(output='./db_schema/raw.sql'):
    "Dump SQL statement for creating database tables. (default output: ./db_schema/raw.sql)"

    from sqlalchemy.schema import CreateTable

    tables = db.Model.metadata.tables

    print 'Dumping table statement ...'
    l = [str(CreateTable(tables[i]).compile(db.engine)) for i in tables]
    if not l:
        print 'Empty'
    else:
        with open(output, 'wb') as fout:
            fout.write("\n".join(l))
        print 'Done on "{p}"'.format(p=output)

