# 2016-7-1
# build by qianqians
# genmodule

import tools

def genmodule(module_name, funcs):
        head_code = "/*this imp file is codegen by abelkhan for c#*/\n\n"
        head_code += "using System;\n"
        head_code += "using System.Collections;\n"
        head_code += "using System.Collections.Generic;\n\n"

        head_code += "using common;\n\n"

        head_code += "namespace imp\n"
        head_code += "{\n"

        code = "    public class " + module_name + " : common.imodule {\n    {\n"
        code += "        public string module_name;\n\n"
        code += "        public " + module_name + "()\n"
        code += "        {\n"
        code += "            module_name = \"" + module_name + "\";\n\n"
        code += "            hub::hub::modules.add_module(\"" + module_name + "\", this);\n"
        code += "        }\n\n"

        for i in funcs:
                func_name = i[0]

                if i[1] != "ntf" and i[1] != "multicast" and i[1] != "broadcast":
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must ntf or broadcast"

                code += "        public delegate void " + func_name + "_handle("
                count = 0
                for item in i[2]:
                        code += tools.gentypetocsharp(item) + " argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += ");\n"
                code += "        public event " + func_name + "_handle on" + func_name + ";\n"
                code += "        void " + func_name + "(ArrayList _event)\n"
                code += "        {\n"
                code += "            if (on" + func_name + " == null)\n"
                code += "            {\n"
                code += "                reutrn;\n"
                code += "            }\n\n"
                count = 0
                for item in i[2]:
                        code += "            var argv" + str(count) + " = ((" + tools.gentypetocsharp(item) + ")_event[" + str(count) + "]);\n"
                        count = count + 1
                code += "\n            on" + func_name + "("
                count = 0
                for item in i[2]:
                        code += "argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += ");\n"
                code += "        }\n\n"

        code += "    }\n"
        code += "}\n"

        return head_code + code
