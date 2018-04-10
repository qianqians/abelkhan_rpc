# 2018-3-16
# build by qianqians
# genjs

import sys
sys.path.append("./parser")

import os
import jparser

def gen(inputdir, clang, hlang, outputdir):
        defmodulelist = []

        syspath = "./client_call_hub/gen/"       
        c_suffix = ""
        if clang == 'c++':
                syspath += "c++/"
                c_suffix = "hpp"
        if clang == 'csharp':
                syspath += "csharp/"
                c_suffix = "cs"
        if clang == 'js':
                syspath += "js/"
                c_suffix = "js"
        sys.path.append(syspath)
        import gencaller
        sys.path.remove(syspath)

        syspath = "./client_call_hub/gen/"    
        h_suffix = ""
        if hlang == 'csharp':
                syspath += "csharp/"
                h_suffix = "cs"
        if hlang == 'js':
                syspath += "js/"
                h_suffix = "js"
        sys.path.append(syspath)
        import genmodule
        sys.path.remove(syspath)
        
        if not os.path.isdir(outputdir):
                os.mkdir(outputdir)

        for filename in os.listdir(inputdir):
                fname = os.path.splitext(filename)[0]
                fex = os.path.splitext(filename)[1]
                if fex != '.juggle':
                        continue
                        
                file = open(inputdir + '//' + filename, 'r')
                genfilestr = file.readlines()

                keydict = jparser.parser(genfilestr)   
                print keydict
                for module_name, module_info in keydict.items():
                        if module_name in defmodulelist:
                                raise 'redefined module %s' % module_name

                        if module_info["module_type"] != "client_call_hub":
                                raise ('%s has wrong module type %s' % (module_name, module_info["module_type"]))

                        defmodulelist.append(module_name)

                        callercode = gencaller.gencaller(module_name, module_info["method"])
                        file = open(outputdir + '//' + module_name + 'caller.' + c_suffix, 'w')
                        file.write(callercode)
                        file.close

                        modulecode = genmodule.genmodule(module_name, module_info["method"])
                        file = open(outputdir + '//' + module_name + 'module.' + h_suffix, 'w')
                        file.write(modulecode)
                        file.close

if __name__ == '__main__':
        gen(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
