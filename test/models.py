from django.db import models
import subprocess

class app(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    # mafft {inputFile} > {outputFile}
    # 'python test/sif_core/Crear_sif_a_partir_del_SBML.py {inputFile} > {outputFile}'
    # wc {inputFile} > {outputFile}
    template = models.CharField(max_length=300)

    def run_app(self, input, output):
        subprocess.run(self.template.format(inputFile=input,outputFile=output), shell=True)
        return 0

