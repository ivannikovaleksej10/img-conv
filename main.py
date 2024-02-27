from PIL import Image
import argparse 
import glob
import os

def webp():
    webpDir = input("webp dir: ")
    pngDir = f"{webpDir}/png"
    os.makedirs(pngDir, exist_ok=True)

    for filename in os.listdir(webpDir):
        if filename.endswith(".webp"):
            webpCount = len(glob.glob1(webpDir,"*.webp"))
            try:
                webp_image = Image.open(os.path.join(webpDir, filename))
                png_image = webp_image.convert("RGBA")
                png_image.save(os.path.join(pngDir, filename.replace(".webp", ".png")))

            except Exception as e:
                print(f"An error occurred: {e}")
                exit()


    print(f"{webpCount} webp were successfully converted to png")


def jpg():
    jpgpDir = input("jpg dir: ")
    pngDir = f"{jpgpDir}/png"
    os.makedirs(pngDir, exist_ok=True)

    for filename in os.listdir(jpgpDir):
        if filename.endswith(".jpg"):
            jpgCount = len(glob.glob1(jpgpDir,"*.jpg"))
            try:
                jpg_image = Image.open(os.path.join(jpgpDir, filename))
                png_image = jpg_image.convert("RGBA")
                png_image.save(os.path.join(pngDir, filename.replace(".jpg", ".png")))

            except Exception as e:
                print(f"An error occurred: {e}")
                exit()


    print(f"{jpgCount} jpg were successfully converted to png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI files converter.")
    # parser.add_argument('indir', type=str, help='Input dir')
    parser.add_argument('ext', type=str, help='Input extension')
    
    args = parser.parse_args()

    if args.ext == "webp":
        webp()
    elif args.ext == "jpg":
        jpg()
    else:
        "$ py main.py -h"
