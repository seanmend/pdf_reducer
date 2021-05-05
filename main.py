import img2pdf
import os
from pdf2image import convert_from_path

def print_hi():
    pdf_path = './pdf_images/1.pdf'
    dirname = './tiff_images'
    convert_from_path(pdf_path, output_folder=dirname, fmt='tiff', size=800, dpi=300, grayscale=True)
    # convert all files ending in .tif inside a directory
    with open("output.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(dirname):
            if not fname.endswith(".tif"):
                continue
            path = os.path.join(dirname, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
            # clean up
            # try:
            #     remove(path2)
            # except OSError:
            #     error = 'No file to remove after image resize.'
        f.write(img2pdf.convert(imgs))


if __name__ == '__main__':
    print_hi()





#  THIS WORKS

# import img2pdf
# import os
# from pdf2image import convert_from_path
#
#
# def print_hi():
#     pdf_path = './pdf_images/1.pdf'
#     dirname = './tiff_images'
#     convert_from_path(pdf_path, output_folder=dirname, fmt='tiff', size=800, dpi=300, grayscale=True)
#     # convert all files ending in .tif inside a directory
#     with open("output.pdf", "wb") as f:
#         imgs = []
#         for fname in os.listdir(dirname):
#             if not fname.endswith(".tif"):
#                 continue
#             path = os.path.join(dirname, fname)
#             if os.path.isdir(path):
#                 continue
#             imgs.append(path)
#         f.write(img2pdf.convert(imgs))
#
#
# if __name__ == '__main__':
#     print_hi()









# other option
# def convert_pdf_2_image(uploaded_image_path, uploaded_image,img_size):
#     project_dir = os.getcwd()
#     os.chdir(uploaded_image_path)
#     file_name = str(uploaded_image).replace('.pdf','')
#     output_file = file_name+'.jpg'
#     pages = convert_from_path(uploaded_image, 200)
#     for page in pages:
#         page.save(output_file, 'JPEG')
#         break
#     os.chdir(project_dir)
#     img = Image.open(output_file)
#     img = img.resize(img_size, PIL.Image.ANTIALIAS)
#     img.save(output_file)
#     return output_file