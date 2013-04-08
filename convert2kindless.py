import Image, ImageOps
import re, os, sys, errno

SIZE = 600,800
IMAGEEXT = re.compile(".*\.(jpg|jpeg)", re.IGNORECASE)

def ensuredirs(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST:
            pass
        else:
            raise

try:
    image_dir = sys.argv[1]
except:
    print "Please specify a directory"
    exit(1)

files = os.listdir(image_dir)
for file in files:
    if IMAGEEXT.match(file):
        f = os.path.join(image_dir, file)
        print f
        img = Image.open(f)

        # rotate landscape images
        if img.size[0] > img.size[1]:
            img = img.rotate(90)

        # resize and crop the image to fit in 600x800 screen
        img = ImageOps.fit(img, SIZE, Image.ANTIALIAS)

        # convert to grayscale
        img = img.convert('L')

        # save to ./ss directory
        ensuredirs(os.path.join(image_dir,'ss'))
        fout = os.path.join(image_dir, 'ss', file)
        img.save(fout, "JPEG")
