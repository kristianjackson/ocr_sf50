import os
from pdf2image import convert_from_path

for filename in os.listdir('scans\SF-50'):
    print('Processing {}'.format(filename))
    if (filename.split('.')[1] == "pdf"):
        print('Converting {}'.format(filename))
        prefix = filename.split(".pdf")[0]
        pages = convert_from_path(filename, 1)
        for page in pages:
            page.save(prefix + '.png', 'PNG')