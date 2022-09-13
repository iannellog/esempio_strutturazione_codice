#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 25, 2022

@author: Giulio Iannello

acquisizione di record da inserire in un'agenda
- versione che usa il pattern "strategy" per rendere trasparente al client
l'algoritmo di acquisizione della lista di record e allo stesso tempo
rendere tale algoritmo indipendente dalla natura della sorgente dei dati
- viene inoltre sfruttata una factory realizzata tramite metodo statico
della classe Record_Reader per eliminare la dipendenza del client dalle
classi concrete che leggono record
"""

from json import dump
from record_readers import Record_Reader


class Context():
    """
    interfaccia per ottenere una lista di record da diverse sorgenti
    """

    def __init__(self, source: Record_Reader):
        self._source = source

    @property
    def source(self) -> Record_Reader:
        return self._source

    @source.setter
    def source(self, source: Record_Reader):
        self._source = source

    def get_list_of_records(self):
        """
        acquisisce records e li organizza in una lista
        l'algoritmo è del tutto indipendente dalla natura della sorgente
        dei dati

        Returns
        -------
        list
            lista di record acquisiti
        """

        def records():
            """
            generatore di record

            Parameters
            ----------

            Yields
            ------
            record : dict
                il successivo record se esiste

            """
            while True:
                record = self._source.get_record()
                if record == {}:  # non vi sono altri record da acquisire
                    break
                yield record

        return [record for record in records()]


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


# client
if __name__ == "__main__":
    # acquisisce la lista di record da un file JSON
    context = Context(
        Record_Reader.create_instance(source_type='json file',
                                      fname='../data/agenda_old.json'))
    agenda = context.get_list_of_records()
    # acquisisce la lista di record da una GUI Qt
    context.source = Record_Reader.create_instance(source_type='Qt dialog')
    agenda += context.get_list_of_records()

    display_records(agenda)

    save_json(agenda, '../temp/agenda.json')
