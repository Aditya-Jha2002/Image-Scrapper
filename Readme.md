# Overview

1. **scraping_image.py** is a python script to scrape images from websites
2. **resize_image.py** is a python script to resize images that you gathered from the scraping_image.py script

# Purpose

1. With just a few changes you can use the scraped image to create datasets for your Deep Learning use cases like Face Recognition, Image Classification etc, or you could use these images to use in your Webstie or App
2. You can also resize those images to be of the same size, any size you prefer, This is done as Deep Learning algorithms like CNNs, RCNNs,require images to be of the same size

# Packages Used

1. **Requests** - Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!
2. **Beautiful Soup** - Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree.
3. **Pillow** - The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.

# Hack

You can comment out the following code in resize_images.py
``` 
for i in images:
resize_image(i,output_folder,(224, 224))
```
    
and uncomment the following part

``` 
#ImageFile LOAD_TRUNCATED_IMAGES = True
```

```
#Parallel(n_jobs=12)(
    #delayed(resize_image)(
        #i,
        #output_folder,
        #(224, 224),
    #)for i in tqdm(images)
#)
```

These steps will help you to parrelize the process of resizing image and help you to resize your images faster
