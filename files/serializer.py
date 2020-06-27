import base64

from .models import File


def get_files():
    files = []
    for f in File.objects.all().iterator():
        size_in_kb = round(int(f.size) / 1024, 2)
        files.append({
            'name': f.name,
            'size': str(size_in_kb) + ' KB',
            'file64': file64(f.path)
        })
    return files


def file64(a_file):
    return base64.b64encode(a_file.read()).decode('utf-8')
