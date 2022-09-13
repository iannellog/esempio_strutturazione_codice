#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 14:36:19 2022

@author: iannello

acquisizione di record da inserire in un'agenda
introduzione di decorator per la classe Record_Reader
"""

from record_readers import Record_Reader

from abc import ABC, abstractmethod


class Record_Reader_Decorator(Record_Reader, ABC):
    """
    classe astratta
    """
    
    def __init__(self, component: Record_Reader):
        self._component = component
    
    @abstractmethod
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
        
        pass
    
    @staticmethod
    def create_instance(component, **kwargs):
        """
        crea un istanza di una sottoclasse concreta

        Parameters
        ----------
        component : Record_Reader
            oggetto della classe Record_Reader da decorare
        
        **kwargs : dict
            parametri opzionali per controllare quale decoratore
            concreto creare

        Raises
        ------
        ValueError
            genera un'eccezione se non viene indicato quale sottoclasse
            creare o se viene indicata una sottoclasse inesistente

        Returns
        -------
        Record_Reader
            un'istanza della sottoclasse richiesta

        """
        
        if 'decorator_type' not in kwargs.keys():
            raise ValueError('missing type of record reader decorator')
        if kwargs['decorator_type'] == 'capitalize':
            return Record_Reader_Capitalize(component)
        else:
            raise ValueError(f'unknown source type {kwargs["source_type"]}')
        
    
class Record_Reader_Capitalize(Record_Reader_Decorator):
    """
    decoratore che acquisisce nome e cognome come stringhe le lettere
    minuscole iniziate da lettere maiuscole
    """
    
    def __init__(self, component):
        super().__init__(component)
        
    def get_record(self):
        record = self._component.get_record()
        if record == {}:
            return record
        record['nome'] = ' '.join([word.capitalize() \
                                    for word in record['nome'].split(' ')]) 
        record['cognome'] = ' '.join([word.capitalize() \
                                      for word in record['cognome'].split(' ')]) 
        return record