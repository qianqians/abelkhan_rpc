# 2016-7-1
# build by qianqians
# gencaller

import tools

def gencaller(module_name, funcs):
        code = "/*this caller file is codegen by abelkhan for c#*/\n"
        code += "using System;\n"
        code += "using System.Collections;\n"
        code += "using System.IO;\n\n"

        code += "namespace ntf\n"
        code += "{\n"
        code += "    public class " + module_name + "\n"
        code += "    {\n"
        code += "        public " + module_name + "()\n"
        code += "        {\n"
        code += "        }\n\n"
        code += "        public " + module_name + "_cliproxy get_client(string uuid)\n"
        code += "        {\n"
        code += "            return new" + module_name + "_cliproxy(uuid);\n"
        code += "        }\n\n"
        code += "        public " + module_name + "_cliproxy_multi get_multicast(Arraylist uuids)\n"
        code += "        {\n"
        code += "            return new" + module_name + "_cliproxy_multi(uuids);\n"
        code += "        }\n\n"
        code += "        public " + module_name + "_broadcast get_broadcast()\n"
        code += "        {\n"
        code += "            return new" + module_name + "_broadcast(uuid);\n"
        code += "        }\n\n"
        code += "    }\n\n"

        cp_code = "    public class " + module_name + "_cliproxy\n"
        cp_code += "    {\n"
        cp_code += "        private string uuid;\n\n"
        cp_code += "        public " + module_name + "_cliproxy(string _uuid)\n"
        cp_code += "        {\n"
        cp_code += "            uuid = _uuid;\n"
        cp_code += "        }\n\n"

        cm_code = "    public class " + module_name + "_cliproxy_multi\n"
        cm_code += "    {\n"
        cm_code += "        private Arraylist uuids;\n\n"
        cm_code += "        public " + module_name + "_cliproxy_multi(Arraylist _uuids)\n"
        cm_code += "        {\n"
        cm_code += "            uuids = _uuids;\n"
        cm_code += "        }\n\n"

        cb_code = "    public class " + module_name + "_broadcast\n"
        cb_code += "    {\n"
        cb_code += "        public " + module_name + "_broadcast()\n"
        cb_code += "        {\n"
        cb_code += "            uuids = _uuids;\n"
        cb_code += "        }\n\n"

        for i in funcs:
                func_name = i[0]

                if i[1] != "ntf" and i[1] != "multicast" and i[1] != "broadcast":
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must ntf or broadcast"

                tmp_code = "        public void " + func_name + "("
                count = 0
                for item in i[2]:
                        tmp_code += tools.gentypetocsharp(item) + " argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                tmp_code += ", "
                tmp_code += ")\n"
                tmp_code += "        {\n"
                tmp_code += "            ArrayList _argv = new ArrayList();\n"
                for n in range(len(i[2])):
                        tmp_code += "            _argv.Add(argv" + str(n) + ");\n"
                
                if i[1] == "ntf":
                        cp_code += tmp_code
                        cp_code += "            hub.hub.gates.call_client(uuid, \"" + module_name + "\", \"" + func_name + "\", _argv);\n"
                        cp_code += "        }\n\n"
                elif i[1] == "multicast":
                        cm_code += tmp_code
                        cm_code += "            hub.hub.gates.call_group_client(uuids, \"" + module_name + "\", \"" + func_name + "\", _argv);\n"
                        cm_code += "        }\n\n"
                elif i[1] == "broadcast":
                        cb_code += tmp_code
                        cb_code += "            hub.hub.gates.call_global_client(\"" + module_name + "\", \"" + func_name + "\", _argv);\n"
                        cb_code += "        }\n\n"

        cp_code += "    }\n\n"
        cm_code += "    }\n\n"
        cb_code += "    }\n\n"

        end_code = "}\n"

        return code + cp_code + cm_code + cb_code + end_code
