import sys, time, subprocess, argparse, logging
from os import remove, listdir, makedirs
from os.path import isfile, join, exists
from PIL import Image
from time import sleep


# @author vladignatyev https://gist.github.com/vladignatyev/
# print a progress bar for Loading
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def main():
    parser = argparse.ArgumentParser(description='Convert .webp files in .gif')

    # INPUT ARGUMENT DEFINITION
    parser.add_argument('-i', '--source_folder', help='Source from which to take .webp files')
    parser.add_argument('-o', '--destination_folder', help='Destination where to save .gif files')
    parser.add_argument('-d', '--delete_after_run', help='Choose if delete after conversion [y/n], DEFAULT: n',
                        default="n")

    args = parser.parse_args()

    # PARSING ARGS
    if args.source_folder is None or args.destination_folder is None:
        logging.error("Missing arguments! You must write source and destination folder")
        sleep(5)
        sys.exit(2)

    inputfolder = args.source_folder
    outputfolder = args.destination_folder
    deletion = True if args.delete_after_run in ("y", "Y") else False

    # Destination folder. Create if does not exist
    if not exists(outputfolder):
        makedirs(outputfolder)

    i = 0
    progress(i, 100, status="\nExtracting images from: " + inputfolder)

    # Extracting files that ends with ".webp" characters from input folder
    images = [inputfolder + "/" + image for image in listdir(inputfolder) if
              (isfile(join(inputfolder, image)) and (".webp" in image))]

    if len(images) != 0:
        jump = 100 / len(images)
    else:
        logging.info("No file FOUND")
        sys.exit("No file FOUND")

    # for each image finded in source folder
    for image in images:
        # progress bar
        i += jump
        progress(i, 100, status='\nConverting: ' + image)

        # open the image and save it with ".gif" extension in output folder keeping original name
        with Image.open(image) as im:
            im.info.pop('background', None)
            name = image.replace(inputfolder, outputfolder)[:]
            name = name.replace(".webp", ".gif")
            try:
                im.save(name, save_all=True)
                if deletion:
                    remove(image)
            except Exception as e:
                logging.error(e)

    logging.info("\nDONE!")
    subprocess.Popen('explorer ' + outputfolder.replace("/", "\\"))
    sleep(5)


if __name__ == "__main__":
    main()
