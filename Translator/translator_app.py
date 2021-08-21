
#  @author Varun Singh
#  @email admin@talkhash.com
#  @create date 2021-08-21 16:02:29
#  @modify date 2021-08-21 16:02:29
#  @desc Translates from English to German using Python lin goslate
#        goslate provides you free python API to google translation service by querying google translation website.

import goslate

def translator(sentance, language="en"):
    gs = goslate.Goslate()
    result = gs.translate(sentance, language)
    return result

print(translator("Follow GetRealWithPython group on Facebook!", "de"))