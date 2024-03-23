
class BaseCommand:
    def __init__(self, vm_param='-mx1600M', model=None):
        self.prefix = 'java ' + vm_param + '-jar ChromHMM.jar'
        self.model = model


class BinarizeBamCommand(BaseCommand):
    def __init__(self, vm_param='-mx1600M', foldthresh='2', binsize='200', chromosomelengthfile=None,
                 cellmarkfiletable=None, inputfile=None, outputfile=None):
        super(BinarizeBamCommand, self).__init__(vm_param, 'BinarizeBam')
        self.foldthresh = foldthresh
        self.binsize = binsize
        self.chromosomelengthfile = chromosomelengthfile
        self.cellmarkfiletable = cellmarkfiletable
        self.inputfile = inputfile
        self.outputfile = outputfile

    def construct_cmd(self):
        status = 0
        cmd = None
        if self.chromosomelengthfile is None or self.cellmarkfiletable is None or self.inputfile is None or self.outputfile is None:
            status = -1
        else:
            cmd = self.prefix + ' ' + self.model + ' -f ' + self.foldthresh + ' -b ' + self.binsize + ' ' + self.chromosomelengthfile + ' ' + self.inputfile + ' ' + self.cellmarkfiletable + ' ' + self.outputfile
        return status, cmd


class LearnModelCommand(BaseCommand):
    def __init__(self, vm_param='-mx1600M', binsize='200', input_dir=None, output_dir=None, numstates='10', assembly=None):
        super(LearnModelCommand, self).__init__(vm_param, 'LearnModel')
        self.binsize = binsize
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.numstates = numstates
        self.assembly = assembly

    def construct_cmd(self):
        status = 0
        cmd = None
        if self.input_dir is None or self.output_dir is None or self.assembly is None:
            status = -1
        else:
            cmd = self.prefix + ' ' + self.model + ' -b ' + self.binsize + ' ' + self.input_dir + ' ' + self.output_dir + ' ' + self.numstates + ' ' + self.assembly
        return status, cmd


if __name__ == '__main__':
    cmd = BinarizeBamCommand(chromosomelengthfile='./text.txt', cellmarkfiletable='/text2.txt', inputfile='./input.txt', outputfile='output.txt')
    print(cmd.construct_cmd())

    cmd2 = LearnModelCommand(input_dir='./test/', output_dir='./output/', assembly='hg19')
    print(cmd2.construct_cmd())
