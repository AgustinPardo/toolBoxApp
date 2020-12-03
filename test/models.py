from django.db import models
import subprocess as sp

class app(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    # mafft {inputFile} > {outputFile}
    template = models.CharField(max_length=150)

    def run_app(self, name):
        return "ready"+ name
    # def run_app(self, inputFile, outputFile):
    #     sp.run(template.format(inputFile=inputFile,outputFile=outputFile))
    #     return 0

