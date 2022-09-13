#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on April 25, 2022

@author: Giulio Iannello

acquisizione di record da inserire in un'agenda
versione base in cui il numero di record da acquisire non è
fornito a priori
"""

from json import dump

# acquisisce i record
agenda = []
while True:
    nome = input('Nome: ')
    if nome == 'stop':  # non vi sono altri record da acquisire
        break
    record = {}
    record['nome'] = nome
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
