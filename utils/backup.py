__author__ = 'SolPie'
import os
import zipfile
import tempfile


def zip_dir(dirname, zipfilename):
    filelist = []
    if os.path.isfile(dirname):
        filelist.append(dirname)
    else:
        for root, dirs, files in os.walk(dirname):
            for name in files:
                filelist.append(os.path.join(root, name))

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        arcname = tar[len(dirname):]
        #print arcname
        zf.write(tar, arcname)
    zf.close()

#todo email backup.zip
def zip_db_photos(uploads_path, db_path, zipfilename):
    filelist = []
    if os.path.isfile(uploads_path):
        filelist.append(uploads_path)
    else:
        for root, dirs, files in os.walk(uploads_path):
            for name in files:
                filelist.append(os.path.join(root, name))
    if os.path.isfile(db_path):
        filelist.append(db_path)

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        zf.write(tar, tar)
    zf.close()
    return zipfilename


def temp_zip():
    with tempfile.SpooledTemporaryFile() as tmp:
        with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as archive:
            return archive
                # with tempfile.SpooledTemporaryFile() as tmp:
    #     with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zf:


def zip_path(root_path, zipfilename):
    filelist = []
    if os.path.isfile(root_path):
        filelist.append(root_path)
    else:
        for root, dirs, files in os.walk(root_path):
            for name in files:
                file_path = os.path.join(root, name)
                if file_path == zipfilename:
                    continue
                filelist.append(file_path)

    zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    for tar in filelist:
        zf.write(tar, tar)
    zf.close()
    return zipfilename


def unzip_file(zipfilename, unziptodir):
    if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\', '/')

        if name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, name))
        else:

            ext_filename = os.path.join(unziptodir, name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir): os.mkdir(ext_dir, 0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


if __name__ == '__main__':
    zip_dir(r'E:/python/learning', r'E:/python/learning/zip.zip')
    unzip_file(r'E:/python/learning/zip.zip', r'E:/python/learning2')
