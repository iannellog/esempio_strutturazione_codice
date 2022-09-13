#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 25, 2022

@author: Giulio Iannello

acquisizione di record da inserire in un'agenda
versione che introduce una seconda classe che implementa l'acquisizione
di un record da una lista memorizzata in un file in formato JSON
"""

from json import dump, load


class Record_Stdin_Reader():
    """
    reader of records from standard input
    """

    def __init__(self):
        pass

    def get_record(self):
        """
        acquisisce un record e lo restituisce sotto forma di dizionario
        restituisce un dizionario vuoto per indicare che non vi sono altri
        record da acquisire

        Returns
        -------
        dict
            il record sotto forma di dizionario
            restituisce un dizionario vuoto per indicare che non vi sono altri
            record da acquisire
        """
        nome = input('Nome: ')
        if nome == 'stop':
            return {}
        record = {}
        record['nome'] = nome
        record['cognome'] = input('Cognome: ')
        record['telefono'] = input('Telefono: ')
        record['email'] = input('Email: ')
        return record


class Record_JSONfile_Reader():
    """
    reader of records from standard input
    """

    def __init__(self, fname):
        self.fin = open(fname)
        self.data = load(self.fin)
        self.fin.close()
        self.next_record = 0

    def get_record(self):
        """
        acquisisce un record e lo restituisce sotto forma di dizionario
        restituisce un dizionario vuoto per indicare che non vi sono altri
        record da acquisire

        Returns
        -------
        dict
            il record sotto forma di dizionario
            restituisce un dizionario vuoto per indicare che non vi sono altri
            record da acquisire
        """
        if self.next_record < len(self.data):  # there is another record
            self.next_record += 1
            return self.data[self.next_record - 1]
        else:
            return {}


def records(get_record):
    """
    generatore di record

    Yields
    ------
    record : dict
        il successivo record se esiste


    """
    while True:
        record = get_record()
        if record == {}:  # non vi sono altri record da acquisire
            break
        yield record


def display_records(agenda):
    """
    visualizza i record in agenda

    Parameters
    ----------
    agenda : list
        lista di record da visualizzare
        ogni record è un dizionario

    Returns
    -------
    None.

    """
    for record in agenda:
        print('-----------')
        for key in record:
            print(f'{key}: {record[key]}')
    print('-----------')


def save_json(obj, fname, indnt=3):
    """
    salva un oggetto python (lista o dizionario) in formato json

    Parameters
    ----------
    obj : list o dict
        oggetto python da salvare in formato json
    fname : str
        path del file in cui salvare obj
    indent : int, optional
        indentazione da usare per il formato json; il default è 3.

    Returns
    -------
    None.

    """
    fout = open(fname, 'w')
    dump(obj, fout, indent=indnt)
    fout.close()


if __name__ == "__main__":
    # acquisisce la lista di record
    agenda = [record for record in records(Record_Stdin_Reader().get_record)]
    agenda += [record for record in records(
        Record_JSONfile_Reader('../data/agenda_old.json').get_record)]

    display_records(agenda)

    save_json(agenda, '../temp/agenda.json')
