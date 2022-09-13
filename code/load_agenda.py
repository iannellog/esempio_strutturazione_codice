#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 25, 2022

@author: Giulio Iannello

acquisizione di record da inserire in un'agenda
versione base in cui il numero di record da acquisire è fornito a priori
"""

from json import dump

n = int(input('Dammi il numero di record: '))

# acquisisce n record
agenda = []
for i in range(n):
    record = {}
    record['nome'] = input('Nome: ')
    record['cognome'] = input('Cognome: ')
    record['telefono'] = input('Telefono: ')
    record['email'] = input('Email: ')    
    agenda.append(record)

# visualizza i record acquisiti
for record in agenda:
    print('-----------')
    for key in record:
        print(f'{key}: {record[key]}')
print('-----------')

# salva i record acquisiti in formato json
fout = open('../temp/agenda.json', 'w')
dump(agenda, fout, indent=3)
fout.close()
