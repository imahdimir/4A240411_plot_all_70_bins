"""


    """

import pandas as pd
import numpy as np

from prj.lib import d , f , v , fp , BINS

class Const :
    dsg = 'DSG'
    hc = 'HC'

c = Const()

def format_file_path(row , cn) :
    return row[cn].as_posix().format(row[v.info_score])

def make_all_combinations() :
    """  """

    ##
    gt = {
            0 : ('FS' , c.dsg , fp.fs_dsg_corr) ,
            1 : ('FS' , c.hc , fp.fs_hc_corr) ,
            2 : ('PO' , c.dsg , fp.po_dsg_corr) ,
            3 : ('PO' , c.hc , fp.po_hc_corr) ,
            }

    bins = BINS * 100
    bins = bins.astype(int)

    df1 = pd.DataFrame.from_dict(data = gt , orient = 'index')
    df2 = pd.DataFrame(data = bins , columns = [v.info_score])

    ##
    df3 = pd.merge(df1 , df2 , how = 'cross')

    ##
    for cn in [2] :
        df3[cn] = df3.apply(lambda r : format_file_path(r , cn) , axis = 1)

    ##
    return df3

##
def get_corr_stats(pair , gt , fpatrn , info) :
    """  """

    ##
    def _test() :
        pass

        ##
        pair = 'FS'
        gt = 'DSG'
        fpatrn = fp.fs_dsg_corr.as_posix()
        info = 30

    ##
    fpth = fpatrn.format(info)
    df0 = pd.read_excel(fpth , names = [v.rsid , v.corr])

    ##
    df = df0[[v.corr]].describe()

    ##
    df.loc[v.n_na] = df0[[v.corr]].isna().sum()

    ##
    df = df.T

    ##
    df = df.rename(columns = {
            'count' : v.n_snps ,
            '50%'   : v.median
            })

    ##
    df[v.inftype] = pair
    df[v.genotype] = gt
    df[v.info_pct] = info

    ##
    reord = {
            v.inftype  : None ,
            v.genotype : None ,
            v.info_pct : None ,
            v.mean     : None ,
            v.std      : None ,
            v.min      : None ,
            v.q1       : None ,
            v.median   : None ,
            v.q3       : None ,
            v.max      : None ,
            v.n_na     : None ,
            v.n_snps   : None ,
            }

    df = df[reord.keys()]

    ##
    df = df.convert_dtypes()

    ##
    return df

##
def main() :
    pass

    ##
    df3 = make_all_combinations()

    ##
    df = pd.DataFrame()
    for pr , gt , ip , iscore in df3.itertuples(index = False) :
        print(pr , gt , ip , iscore)
        _df = get_corr_stats(pr , gt , ip , iscore)
        df = pd.concat([df , _df])

    ##
    df.to_excel(f.corrs , index = False)

    ##

##
def _test() :
    pass

    ##
    df1 = get_corr_stats('FS' , 'DSG' , fp.fs_dsg_corr , 30)

    ##

    ##
