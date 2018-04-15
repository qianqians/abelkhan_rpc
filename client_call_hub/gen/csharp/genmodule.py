# 2016-7-1
# build by qianqians
# genmodule

import tools

def genmodule(module_name, funcs):
        head_code = "/*this rsp file is codegen by abelkhan for c#*/\n\n"
        head_code += "using System;\n"
        head_code += "using System.Collections;\n"
        head_code += "using System.Collections.Generic;\n\n"

        head_code += "using abelkhan;\n\n"

        head_code += "namespace rsp\n{\n"

        rsp_code = ""

        code = "    public class " + module_name + " : abelkhan.Module\n    {\n"
        code += "        public string module_name;\n"
        code += "        public hub.hub hub_handle;\n"
        code += "        public " + module_name + "(hub.hub _hub)\n        {\n"
        code += "            module_name = \"" + module_name + "\";\n"
        code += "            hub_handle = _hub;\n"
        code += "            hub.hub.modules.add_module(\"" + module_name + "\", this);\n"
        code += "        }\n\n"

        for i in funcs:
                func_name = i[0]

                code += "        public delegate void " + func_name + "handle("
                count = 0
                for item in i[2]:
                        code += tools.gentypetocsharp(item) + " argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += ");\n"
                code += "        public event " + func_name + "handle on" + func_name + ";\n"

                if i[1] == "ntf":
                        code += "        public void " + func_name + "("
                        count = 0
                        for item in i[2]:
                                code += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ")\n        {\n"
                        code += "            if(on" + func_name + " != null)\n            {\n"
                        code += "                on" + func_name + "("
                        count = 0
                        for item in i[2]:
                                code += " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ");\n"
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        code += "        public void " + func_name + "(string uuid"
                        count = 0
                        for item in i[2]:
                                code += ", " + tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                        code += ")\n        {\n"
                        code += "            if(on" + func_name + " != null)\n            {\n"
                        code += "                rsp = new rsp_" + func_name + "(uuid);\n"
                        code += "                on" + func_name + "("
                        count = 0
                        for item in i[2]:
                                code += " argv" + str(count+1)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ");\n"

                        rsp_code += "    public class rsp_" + func_name + " : abelkhan.Response\n    {\n"
                        rsp_code += "        public string uuid;\n\n"
                        rsp_code += "        public rsp_" + func_name + "(string _uuid)\n"
                        rsp_code += "        {\n"
                        rsp_code += "            uuid = _uuid;\n"
                        rsp_code += "        }\n\n"

                        rsp_code += "        void call("
                        count = 0
                        for item in i[4]:
                                rsp_code += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        rsp_code += ", "
                        rsp_code += ")\n        {\n"
                        rsp_code += "            hub.hub.gates.call_client(hub.hub.gates.current_client_uuid, \"" + module_name + "\", \"" + func_name + "_rsp\", uuid"
                        count = 0
                        for item in i[4]:
                                rsp_code += ", argv" + str(count)
                                count = count + 1
                        rsp_code += ");\n"
                        rsp_code += "        }\n"

                        rsp_code += "        void err("
                        count = 0
                        for item in i[6]:
                                rsp_code += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        rsp_code += ", "
                        rsp_code += ")\n        {\n"
                        rsp_code += "            hub.hub.gates.call_client(hub.hub.gates.current_client_uuid, \"" + module_name + "\", \"" + func_name + "_err\", uuid"
                        count = 0
                        for item in i[6]:
                                rsp_code += ", argv" + str(count)
                                count = count + 1
                        rsp_code += ");\n"
                        rsp_code += "        }\n"
                        rsp_code += "    }\n\n"
                else:
                        raise "func:%s wrong rpc type:%s must req or ntf" % (func_name, i[1])

                if i[1] == "ntf":
                        pass
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        code += "                rsp = null;\n"
                else:
                        raise "func:%s wrong rpc type:%s must req or ntf" % (func_name, i[1])

                code += "            }\n"
                code += "        }\n\n"

        code += "    }\n"
        code += "}\n"

        return head_code + rsp_code + code
