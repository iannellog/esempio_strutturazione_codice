#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 25, 2022

@author: Giulio Iannello

acquisizione di record da inserire in un'agenda
versione che importa varie classi che implementano l'acquisizione
di un record da varie sorgenti
"""

from json import dump
from record_readers import Record_Stdin_Reader, \
     Record_JSONfile_Reader, Record_Qt_Dialog_Reader


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
    indnt : int, optional
        indentazione da usare per il formato json; il default è 3.

    Returns
    -------
    None.

    """
    fout = open(fname, 'w')
    dump(obj, fout, indent=indnt)
    fout.close()


if __name__ == "__main__":
    # acquisisce le liste di record
    agenda = [record for record in records(
        Record_JSONfile_Reader('../data/agenda_old.json').get_record)]
    agenda += [record for record in records(Record_Qt_Dialog_Reader().get_record)]
    agenda += [record for record in records(Record_Stdin_Reader().get_record)]

    display_records(agenda)

    save_json(agenda, '../temp/agenda.json')
