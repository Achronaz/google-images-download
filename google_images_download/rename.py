import os 
  
def main(): 
    for folder_count, category in enumerate(os.listdir("downloads")):
        dest = 'downloads/' + category + '/' 
        for img_count, img in enumerate(os.listdir(dest)):
            src = dest + img 
            extension = os.path.splitext(img)[1]
            dst = dest + str(img_count) + extension 
            print('mv "' + src + '" "' + dst +'"')
            os.rename(src, dst) 
  
if __name__ == '__main__': 
    main() 