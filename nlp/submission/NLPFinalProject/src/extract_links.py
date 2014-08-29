#!/usr/bin/python

import sys
import wikipedia

"""
input file is $1, outputfile $2

input file contains the named entities from a particular wikipedia article
"""
def main():
    usage = 'extract_links.py <infile>'
    if len(sys.argv) < 2:
        print usage
        sys.exit(1)


    surface_file = sys.argv[1]

    entity_links = {}
    entity_text = {}

    for entity in open(surface_file):
        entity = entity.strip()
        print 'getting info for: ', entity
        try:
            page = wikipedia.page(entity)
            # get the outgoing links from this page
            entity_links[entity] = page.links 
            # get the text on this page
            entity_text[entity] = page.content
        except Exception as e:
            print e
            continue

    
    links_out = open(surface_file + '_links.out', 'w')
    for (entity, links) in entity_links.items():
        links_out.write(entity + ' :: ' + str(links) + '\n')

        
    text_out = open(surface_file + '_text.out', 'w')
    for (entity, text) in entity_text.items():
        text_out.write(entity + ' :: ' + text.encode('utf-8') + '\n')



main()
