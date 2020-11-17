# webp_to_gif 
---
Simply converter from webp to gif. 
This script takes all the images in _source_ folder, convert them and save the result in _destination_ folder.
_Source_ and _destination_ are mandatory. You can also choose if delete the elements from source after the conversion.

## Requirements 
---
To use this script you must install the following modules
```bash
pygifsicle==1.0.1
Pillow==8.0.1
```

## Usage 
---
The script was built to being used from terminal/cmd.
A simple usage example is:
```bash
main.py -i <source> -o <destination>
```

Other options are:
```bash
-i, --source_folder      'Source from which to take .webp files'
-o, --destination_folder 'Destination where to save .gif files'
-d, --delete_after_run   'Choose if delete after conversion [y/n], DEFAULT: n, default="n"'
```

## License 
---
[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)