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
    out = data / 'out'

    plink_out = inp / 'plink_out'
    flt_snps = inp / 'flt_snps'

    dsg = med / 'dsg'
    hc = med / 'hc'

    dsg_i = med / 'dsg_i'
    hc_i = med / 'hc_i'

    fs_dsg_corr = out / 'FS_dsg_corr'
    fs_hc_corr = out / 'FS_hc_corr'
    po_dsg_corr = out / 'PO_dsg_corr'
    po_hc_corr = out / 'PO_hc_corr'

d = Dir()

class File :
    fs_po_ids_txt = d.inp / 'fs_po_ids.txt'

    all_flt_snps = d.med / 'all_flt_snps.prq'

    rel = '/disk/genetics/ukb/alextisyoung/haplotypes/relatives/bedfiles/hap.kin0'

    corrs = d.out / 'corrs.xlsx'

f = File()

class FilePattern :
    plink_out = d.plink_out.as_posix() + '/c{chr}.bgen'

    dsg = d.dsg / 'c{}.prq'
    hc = d.hc / 'c{}.prq'

    dsg_i = d.dsg_i / 'i{}.prq'
    hc_i = d.hc_i / 'i{}.prq'

    fs_dsg_corr = d.fs_dsg_corr / 'i{}.xlsx'
    fs_hc_corr = d.fs_hc_corr / 'i{}.xlsx'
    po_dsg_corr = d.po_dsg_corr / 'i{}.xlsx'
    po_hc_corr = d.po_hc_corr / 'i{}.xlsx'

fp = FilePattern()

class Vars :
    info_n = '7'
    iid = 'IID'
    rsid_n_s = '1'

    info_score = 'info_score'
    rsid = 'rsid'
    corr = 'corr'
    n_na = 'n_na'
    n_snps = 'n_snps'
    inftype = 'InfType'
    genotype = 'Genotype'
    median = 'median'
    mean = 'mean'
    std = 'std'
    min = 'min'
    q1 = '25%'
    q3 = '75%'
    max = 'max'
    info_pct = 'Info %'

v = Vars()
