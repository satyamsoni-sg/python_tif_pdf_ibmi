# TIF to PDF Python Script

# Setup

Run the below commands to install pipenv

```bash
python -m pip install pipenv==2022.10.11
```

Installing dependencies

```bash
python -m pipenv install
python -m pipenv shell
```

---

## running the script

To check for available options 

```bash
python main.py -h
```

to run for all the `tif` files in the directory.


```bash
pdf_utils ~/Documents/pdf_utils/ [main] python main.py

Looking for files with extension: *.tif
Files found: [PosixPath('2807D7B_4.tif'), PosixPath('2807D7B_2.tif'), PosixPath('2807D7B_3.tif'), PosixPath('2807D7B_1.tif')]
2807D7B_4.tif
2807D7B_2.tif
2807D7B_3.tif
2807D7B_1.tif
Saving to output.pdf
```

To run only for selected files.

```bash

pdf_utils ~/Documents/pdf_utils/ [main] python main.py --files 2807D7B_4.tif,2807D7B_3.tif  

Looking for files with extension: *.tif
Files found: ['2807D7B_4.tif', '2807D7B_3.tif']
2807D7B_4.tif
2807D7B_3.tif
Saving to output.pdf

```

To run for multiple extensions. If You want to run for `tif`, `png` or any other extensions.

```bash

pdf_utils ~/Documents/pdf_utils/ [main] python main.py --extension tif,png

Looking for files with extension: *.tif,png
Files found: [PosixPath('2807D7B_4.tif'), PosixPath('2807D7B_2.tif'), PosixPath('2807D7B_3.tif'), PosixPath('2807D7B_1.tif'), PosixPath('profile_pic.png')]
2807D7B_4.tif
2807D7B_2.tif
2807D7B_3.tif
2807D7B_1.tif
profile_pic.png
Saving to output.pdf
```

You can also override `output` filename.

```bash

pdf_utils ~/Documents/pdf_utils/ [main] python main.py --filename foo.pdf

Looking for files with extension: *.tif
Files found: [PosixPath('2807D7B_4.tif'), PosixPath('2807D7B_2.tif'), PosixPath('2807D7B_3.tif'), PosixPath('2807D7B_1.tif')]
2807D7B_4.tif
2807D7B_2.tif
2807D7B_3.tif
2807D7B_1.tif
Saving to foo.pdf

```

---

Thanks