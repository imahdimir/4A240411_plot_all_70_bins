"""

    """

import numpy as np
import pandas as pd
from bgen_reader import open_bgen
from pathlib import Path

from prj.lib import d , fp

ex_bg_fp = d.plink_out / 'c1.bgen'

def make_df_of_iids_from_bgen_open_obj(bg_opn) :
    bg_opn_s = list(bg_opn.samples)
    df = pd.DataFrame({
            'IID' : bg_opn_s
            })
    # get the IID from FID_IID
    df['IID'] = df['IID'].str.split('_').str[1]
    return df

def open_bgen_ret_iid_df_and_prob_arr(bgen_fp) :
    """ """

    ##
    if False :
        pass

        ##
        bgen_fp = ex_bg_fp

    ##
    bgo = open_bgen(bgen_fp)

    ##
    df = make_df_of_iids_from_bgen_open_obj(bgo)

    ##
    nd_p = bgo.read()

    ##
    # I had to make a list of it ow the code crashes I don't know why
    rsids = list(bgo.rsids)

    ##
    assert len(rsids) == nd_p.shape[1]

    ##
    return df , nd_p , rsids

##
def save_dosages_of_all_vars_from_bgen(bgen_fp: Path) :
    """ """

    ##
    if False :
        pass

        ##
        bgen_fp = ex_bg_fp

    ##
    df_id , nd_p , rsids = open_bgen_ret_iid_df_and_prob_arr(bgen_fp)

    ##
    nd_d = nd_p[: , : , 1] + 2 * nd_p[: , : , 2]

    ##
    df1 = pd.DataFrame(nd_d)
    df1 = df1.astype('object')

    ##
    df1.loc['rsid'] = rsids

    ##
    df1v = df1.head()

    ##
    df1 = df1.T.drop_duplicates(subset = ['rsid']).T

    ##
    df1.columns = df1.loc['rsid']
    df1 = df1.drop('rsid')

    ##
    df_d = pd.concat([df_id , df1] , axis = 1)

    ##
    dfv = df_d.head()

    ##
    _fp = d.dsg / f'{bgen_fp.stem}.prq'
    df_d.to_parquet(_fp , index = False)

##
def save_hard_calls_of_all_vars_from_bgen(bgen_fp) :
    """ """

    ##
    df_id , nd_p , rsids = open_bgen_ret_iid_df_and_prob_arr(bgen_fp)

    ##
    nd_h = np.argmax(nd_p , axis = 2)

    ##
    df1 = pd.DataFrame(nd_h)
    df1 = df1.astype('object')

    ##
    df1.loc['rsid'] = rsids

    ##
    df1 = df1.T.drop_duplicates(subset = ['rsid']).T

    ##
    df1.columns = df1.loc['rsid']
    df1 = df1.drop('rsid')

    ##
    df_h = pd.concat([df_id , df1] , axis = 1)

    ##
    _fp = d.hc / f'{bgen_fp.stem}.prq'
    df_h.to_parquet(_fp , index = False)

##
def main() :
    pass

    ##
    for cn in range(1 , 22 + 1) :
        print(cn)
        bgen_fp = fp.plink_out.format(chr = cn)
        bgen_fp = Path(bgen_fp)
        save_dosages_of_all_vars_from_bgen(bgen_fp)
        save_hard_calls_of_all_vars_from_bgen(bgen_fp)

    ##
