dejavu
=======

This is a fork from an audio fingerprinting tool called dejavu (see [here](https://github.com/worldveil/dejavu/)). 
I changed the output a little bit so that you don't need a database to extract the fingerprints. They can be extracted as text files directly. 
This tool just supports the extraction of fingerprints but not the recognition anymore.

### Installation: 
See [INSTALLATION.md](INSTALLATION.md)

### Getting Started:
Just use this modified signature of `dejavu.py`:

``` 
usage: dejavu.py [-h] [-f [FINGERPRINT [FINGERPRINT ...]]]

Dejavu: Audio Fingerprinting library

optional arguments:
  -h, --help            show this help message and exit
  -f [FINGERPRINT [FINGERPRINT ...]], 
  --fingerprint [FINGERPRINT [FINGERPRINT ...]]
                        Fingerprint files in a directory
                        Usages:
                        --fingerprint /path/to/directory extension /path/to/fingerprint_directory
                        --fingerprint /path/to/file path/to/fingerprint_directory
```

If you want to fingerprint all files in a specific directory: 

```
./dejavu.py -f /path/to/audio_files wav /path/to/output_dir
```

If you just want to fingerprint one file:

```
./dejavu.py -f /path/to/audio_file /path/to/output_dir
``` 