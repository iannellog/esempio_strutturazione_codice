#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 25, 2022

@author: Giulio Iannello

acquisizione di record da inserire in un'agenda
versione che introduce un generator per acquisire più record
e utilizza una comprehension per creare la lista dei record acquisiti
"""

from json import dump


def get_record():
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
    agenda = [record for record in records(get_record)]

    display_records(agenda)

    save_json(agenda, '../temp/agenda.json')
