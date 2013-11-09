#!/usr/bin/python

import os, sys
from binwalk import Binwalk

def lzma_callback(offset, results):
    for result in results:
        if result['description'].startswith('LZMA compressed data, properties: 0x5D'):
            with open(sys.argv[1]) as f:
                f.seek(result['offset'])
                lzma_header = f.read(5)
                uncompressed_size = '\x00\x00\x00\x10\x00\x00\x00\x00'
                data = f.read()
                output = open(sys.argv[1]+'.lzma', 'w')
                output.write(lzma_header+uncompressed_size+data)
                f.close()

if __name__ == '__main__':
    nargs = len(sys.argv)

    if nargs != 2:
        print '\
  \nLZMA Unpacker: Extract LZMA sections from firmware images\n\
  \nTested with the following Cable Modems:\n\
  - Cisco DPC3925, DPC2434\n\
  - Motorola SB5100, SB5101, SVG6582, SVG1202\n\
  - Thomson ACG905, DCM425, DHG534, DHG544, DWG850, DWG874\n\
  - Webstar DPC2203\n\
  \nBernardo Rodrigues, http://w00tsec.blogspot.com\n\
  \nUsage: %s firmware_image.bin' % os.path.basename(sys.argv[0])+'\n'

    else:
        with Binwalk() as bw:
            try:
                with open(sys.argv[1], 'rb'):
                    bw.display.header()
                    bw.scan(sys.argv[1], callback=lzma_callback, show_invalid_results=True)
                    try:
                        with open(sys.argv[1]+'.lzma', 'rb'):
                            bw.extractor.add_rule('lzma:7z:7zr e -y %e')
                            bw.scan(sys.argv[1]+'.lzma', callback=bw.display.results)
                    except Exception:
                        print 'LZMA 0x5D signature not found'
                        exit
            except IOError:
                print 'File not found: '+sys.argv[1]

