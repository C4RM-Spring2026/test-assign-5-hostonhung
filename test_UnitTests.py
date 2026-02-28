
import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != ''

import BondPrice_File
def test_getBondPrice():
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  1)) == 2170604
    assert round(BondPrice_File.getBondPrice(.03, 2000000, .04, 10,  2)) == 2171686
    assert 'for' not in inspect.getsource(BondPrice_File.getBondPrice)

