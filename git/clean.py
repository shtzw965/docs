#!/bin/python3
# qpdf --qdf --no-original-object-ids --stream-data=uncompress --object-streams=disable
# qpdf --deterministic-id --stream-data=compress --compression-level=9 --object-streams=generate
import pikepdf, sys
def getpages(pages):
  for kid in pages['/Kids']:
    if '/Pages' == kid['/Type']:
      yield from getpages(kid)
    else:
      yield kid
pdf = pikepdf.open(sys.argv[1])
for page in getpages(pdf.trailer['/Root']['/Pages']):
  if b'Restrictions apply' in page['/Contents'][-1].read_bytes():
    del page['/Contents'][-1]
del pdf.trailer['/Info']['/ModDate']
del pdf.trailer['/ID']
pdf.save(sys.argv[2], deterministic_id=True, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
