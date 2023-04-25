
import hmac

def vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku: str, data: dict):

    key = bytes(hashstring_predchadzajuceho_bloku, encoding='utf8')
    msg = bytes(str(data), encoding='utf8')
    h = hmac.new(key=key, msg=msg, digestmod='md5')
    result = h.hexdigest()
    print(result)
    return result



databaza = []


# toto je zaciatok nasej retaze
seed = '843b614237935cfbbc9c1a2386e69724'

# toto je prvy vypocitany block naseho blokchainu
prva_transakcia = {'ucet1': 5643765, 'ucet2': 6574654, 'suma': 43}
hashstring = vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku=seed, data=prva_transakcia)

# toto je druhy blok naseho blockchainu
druha_transakcia = {'ucet1': 674576565, 'ucet2': 6574654, 'suma': 16.10}
hashstring = vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku=hashstring, data=druha_transakcia)

# toto je druhy blok naseho blockchainu
tretia_transakcia = {'ucet1': 4582358943, 'ucet2': 6574654, 'suma': 128}
hashstring = vypocitaj_hash_bloku(hashstring_predchadzajuceho_bloku=hashstring, data=tretia_transakcia)