import time


def create_export(template_project):
    export = template_project.exports.create()

    # Attendre que l’export soit prêt
    export.refresh()
    print("Export en cours du template...")
    while export.export_status != 'finished':
        time.sleep(1)
        export.refresh()

    return export

def download_export(export):
    with open('/tmp/export.tgz', 'wb') as f:
        export.download(streamed=True, action=f.write)