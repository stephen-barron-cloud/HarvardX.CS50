"""
In a file called extensions.py, implement a program that prompts the user for the name 
of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, 
in any of these suffixes:

    .gif
    .jpeg
    .png
    .pdf
    .txt
    .zip

"""

def main():
    var_filename = input("Enter a file name: ").lower()
    var_filemain,var_fileext = var_filename.split(sep=".")

    match var_fileext:
        case "gif":
            var_MIMEType ="image/gif"
        case "jpg":
           var_MIMEType ="image/jpeg"
        case "png":
            var_MIMEType ="image/png"   
        case "pdf":
            var_MIMEType ="application/pdf" 
        case "txt":
            var_MIMEType = "text/plain"
        case "zip":
            var_MIMEType = "application/zip"

    print("For files ending with extension ", var_fileext," the MIME Type is ",var_MIMEType,".", sep="")


main()