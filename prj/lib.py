import numpy as np
from pathlib import Path
from mahdi_env import get_env

BINS = np.arange(.3 , 1 , .01)

env = get_env()

class Env :
    pgsf = 'pgsf'

e = Env()

class Dir :
    data = '/disk/genetics/ukb/mahdimir/prj_dta/1144_plot_all_70_bins'
    data = Path(data)

    inp = data / 'inp'
    med = data / 'med'

    plink_out = inp / 'plink_out'
    flt_snps = inp / 'flt_snps'

    dsg = med / 'dsg'
    hc = med / 'hc'

d = Dir()

class File :
    all_flt_snps = d.med / 'all_flt_snps.txt'

f = File()

class FilePattern :
    plink_out = d.plink_out.as_posix() + '/c{chr}.bgen'

fp = FilePattern()

class Vars :
    maf_n = '5'
    info_n = '7'
    rsid_n = '1'

    msk = 'msk'
    ms1 = 'ms1'
    chr = 'chr'

v = Vars()
