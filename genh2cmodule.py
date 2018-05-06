# 2018-3-16
# build by qianqians
# genjs

import sys
sys.path.append("./parser")

import os
import jparser

def gen(inputdir, lang, outputdir):
        defmodulelist = []
        defenumlist = []

        syspath = "./hub_call_client/gen/"
        h_suffix = ""
        if lang == 'c++':
                syspath += "c++/"
                h_suffix = "hpp"
        if lang == 'csharp':
                syspath += "csharp/"
                h_suffix = "cs"
        if lang == 'js':
                syspath += "js/"
                h_suffix = "js"
        sys.path.append(syspath)
        import genmodule
        sys.path.remove(syspath)

        syspath = "./enum/"
        if lang == 'c++':
                syspath += "c++/"
                sys.path.append(syspath)
                import genenum
        if lang == 'csharp':
                syspath += "csharp/"
                sys.path.append(syspath)
                import genenum
        if lang == 'js':
                syspath += "js/"
                sys.path.append(syspath)
                import genenum_browser as genenum
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

                module, enum = jparser.parser(genfilestr)
                print module
                print enum
                for module_name, module_info in module.items():
                        if module_name in defmodulelist:
                                raise 'redefined module %s' % module_name

                        if module_info["module_type"] != "hub_call_client":
                                raise ('%s has wrong module type %s' % (module_name, module_info["module_type"]))

                        defmodulelist.append(module_name)

                        modulecode = genmodule.genmodule(module_name, module_info["method"])
                        file = open(outputdir + '//' + module_name + 'module.' + h_suffix, 'w')
                        file.write(modulecode)
                        file.close
                for enum_name, enums in enum.items():
                        if enum_name in defenumlist:
                                raise 'redefined enum %s' % enum_name
                        defmodulelist.append(enum_name)

                        enum_code = genenum.genenum(enum_name, enums)
                        file = open(outputdir + '//' + enum_name + 'enum.' + h_suffix, 'w')
                        file.write(enum_code)
                        file.close()

if __name__ == '__main__':
        gen(sys.argv[1], sys.argv[2], sys.argv[3])
