#LZMA Unpacker

Extract LZMA sections from cable modem firmware images

For more information: http://w00tsec.blogspot.com/2013/11/unpacking-firmware-images-from-cable.html

Tested with the following Cable Modems:
  - Cisco DPC3925, DPC2434
  - Motorola SB5100, SB5101, SVG6582, SVG1202
  - Thomson ACG905, DCM425, DHG534, DHG544, DWG850, DWG874
  - Webstar DPC2203
  
#Prerequisites:
- [Binwalk](https://code.google.com/p/binwalk/)

#Screenshots

![Screenshot](http://4.bp.blogspot.com/-nXdE3Riusdw/Un5ICQNw93I/AAAAAAAAAIU/BZYzsoT3Les/s640/screenshot.png)

#Usage
    python lzma-unpacker.py firmware_image.bin
