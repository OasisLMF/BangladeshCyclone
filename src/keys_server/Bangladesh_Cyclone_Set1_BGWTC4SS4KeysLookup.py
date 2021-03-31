# -*- coding: utf-8 -*-

__all__ = [
    'Bangladesh_Cyclone_Set1_BGWTC4SS4KeysLookup'
]

from keys_server import CatrisksBaseKeysLookup 

from oasislmf.utils.log import oasis_log


class Bangladesh_Cyclone_Set1_BGWTC4SS4KeysLookup(CatrisksBaseKeysLookup):
    """
    CatRisks MENAEQ model keys lookup logic - at present the MENAEQ lookup logic
    is identical to that of the Catrisks generic keys lookup, but future
    differences can be dealt with by overriding the relevant generic methods here.
    """

    @oasis_log()
    def __init__(self, keys_data_directory=None, supplier='UKMO&BUET', model_name='BGWTCSS4', model_version=None):
        super(self.__class__, self).__init__(keys_data_directory, supplier, model_name, model_version)
