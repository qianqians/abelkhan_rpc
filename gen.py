# 2018-3-16
# build by qianqians
# genjs

import sys
sys.path.append("./parser")

import os
import jparser

def gen(inputdir, lang, outputdir):
        defmodulelist = []

        suffix = ""
        if lang == 'c++':
                suffix = "hpp"

        if not os.path.isdir(outputdir):
                os.mkdir(outputdir)

        for filename in os.listdir(inputdir):
                fname = os.path.splitext(filename)[0]
                fex = os.path.splitext(filename)[1]
                if fex == '.juggle':
                        file = open(inputdir + '//' + filename, 'r')
                        genfilestr = file.readlines()

                        keydict = jparser.parser(genfilestr)
                        print keydict
                                
                        for module_name, module_info in keydict.items():
                                syspath = "./"
                                if module_info["module_type"] == "client_call_hub":
                                        syspath += "client_call_hub/gen/"
                                elif module_info["module_type"] == "hub_call_hub":
                                        syspath += "hub_call_hub/gen/"
                                elif module_info["module_type"] == "hub_call_client":
                                        syspath += "hub_call_client/gen/"
                                if lang == "c++":
                                        syspath += "c++/"
                                sys.path.append(syspath)
                                import gencaller
        
                                if module_name in defmodulelist:
                                        raise 'redefined module %s' % module_name

                                defmodulelist.append(module_name)
                                
                                callercode = gencaller.gencaller(module_name, module_info["method"])
                                file = open(outputdir + '//' + module_name + 'caller.' + suffix, 'w')
                                file.write(callercode)
                                file.close

if __name__ == '__main__':
        gen(sys.argv[1], sys.argv[2], sys.argv[3])
