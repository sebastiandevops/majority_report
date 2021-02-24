#!/usr/bin/python3
import typer
reader = __import__('data_reader').data_reader

def main(name:str):
    data = reader(name)
    print(data.dtypes)
    print('--------------------------------')
    print(data.head())
    print('--------------------------------')
    print(data['día'].value_counts())
    print('--------------------------------')
    print(data.info())

if __name__ == '__main__':
    typer.run(main)
