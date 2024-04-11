"""

    """

import numpy as np
import pandas as pd
from bgen_reader import open_bgen
from pathlib import Path

from prj.lib import g

def make_df_of_iids_from_bgen_open_obj(bg_opn) :
    bg_opn_s = list(bg_opn.samples)
    df = pd.DataFrame({
            'IID' : bg_opn_s
            })
    # get the IID from FID_IID
    df['IID'] = df['IID'].str.split('_').str[1]
    return df

def open_bgen_ret_iid_df_and_prob_arr(bgen_fp) :
    pass

    ##
    if False :
        pass

        ##
        bgen_fp = '/var/genetics/ws/mahdimir/LOCAL/prj/imputed-genotype-corr-240317/med/plink_out/chr1.bgen'

    ##
    bgo = open_bgen(bgen_fp)

    ##
    df = make_df_of_iids_from_bgen_open_obj(bgo)

    ##
    nd_p = bgo.read()

    ##
    rsids = list(bgo.rsids)  # I had to make a list of it ow the code crashes I don't know why

    ##
    assert len(rsids) == nd_p.shape[1]

    ##
    return df , nd_p , rsids
