import os, csv, json
import zipfile

class FileManager:
    # 获取当前路径下所有子文件夹
    @staticmethod
    def sub_dir(path):
        return [file for file in os.listdir(path) if os.path.isdir('\\'.join([path,file]))]

    # 获取当前路径下的非目录子文件
    @staticmethod
    def no_subdir_files(path):
        return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    # 获取当前路径下的非目录子文件,包含子目录下文件
    @staticmethod
    def inc_subdir_files(path):
        return [[os.path.join(root, file) for file in files] for root, dirs, files in os.walk(path)]

    # 获取当前路径下的所有指定文件类型的非目录子文件
    @staticmethod
    def no_subdir_type_files(path, type):
        all_file = list()
        for file in FileManager.no_subdir_files(path):
            arr = os.path.splitext(os.path.join(file))
            if arr[1] == type : all_file.append(arr[0])

        return all_file

    # 获取当前路径下的所有指定文件类型的非目录子文件,包含子目录下文件
    @staticmethod
    def inc_subdir_type_files(path, type):
        all_file = list()
        for files in FileManager.inc_subdir_files(path):
            for file in files:
                dir_name, file_name = os.path.split(file)
                arr = os.path.splitext(os.path.join(file_name))
                if arr[1] == type: all_file.append(arr[0])
        return all_file

    @staticmethod
    def write_file(path, data_file):
        [dir_name, file_name] = os.path.split(path)
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            with open(path, 'wb+') as f:
                for chunk in data_file.chunks():
                    f.write(chunk)

            return True
        except:
            return False

    @staticmethod
    def get_extension(file):
        (shotname, extension) = os.path.splitext(file)
        return extension

    @staticmethod
    def get_shotname(file):
        (shotname, extension) = os.path.splitext(file)
        return shotname

    @staticmethod
    def get_filename(file):
        [dir_name, file_name] = os.path.split(file)
        return file_name

    @staticmethod
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if chunk:
                    yield chunk
                else:
                    break

    @staticmethod
    def write2py(path, data):
        [dir_name, file_name] = os.path.split(path)
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(data)
            return True
        except:
            if os.path.exists(path):
                os.remove(path)
            return False

    @staticmethod
    def rm_file(file):
        if os.path.exists(file):
            os.remove(file)

    @staticmethod
    def write_dict2csv(csv_file, title, content_list):
        [dir_name, file_name] = os.path.split(csv_file)
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            with open(csv_file, 'w', newline='', encoding='utf-8-sig') as f:
                spam_writer = csv.writer(f, dialect='excel')
                spam_writer.writerow(title)
                for content in content_list:
                    spam_writer.writerow(content)
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def write_dict2excel(csv_file, title, content_list):
        [dir_name, file_name] = os.path.split(csv_file)
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)

            with open(csv_file, 'w', newline='') as f:
                spam_writer = csv.writer(f, dialect='excel')
                spam_writer.writerow(title)
                for content in content_list:
                    spam_writer.writerow(content)
            return True
        except Exception as e:
            return False

    @staticmethod
    def write2html(path, data):
        [dir_name, file_name] = os.path.split(path)
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(data)
            return True
        except:
            if os.path.exists(path):
                os.remove(path)
            return False

    @staticmethod
    def read_html(filed_path):
        try:
            with open(filed_path, 'r', encoding='utf-8', newline='') as f:
                res = f.read()
        except:
            res = False
        return res

    @staticmethod
    def write_dict2json(path, data):
        [dir_name, file_name] = os.path.split(path)
        try:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            json_str = json.dumps(data, ensure_ascii=False, indent=4)

            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(json_str)
            return True
        except Exception as e:
            print(repr(e))
            if os.path.exists(path):
                os.remove(path)
            return False

    @staticmethod
    def read_json(filed_path):
        with open(filed_path, 'r', encoding='utf-8', newline='') as f:
            load_dict = json.load(f)

        return load_dict

    @staticmethod
    def make_zip(source_dir, output_filename):
        zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()

        return True
