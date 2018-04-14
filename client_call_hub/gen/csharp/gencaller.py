# 2016-7-1
# build by qianqians
# gencaller

import tools

def gencaller(module_name, funcs):
        head_code = "/*this req file is codegen by abelkhan for c#*/\n"
        head_code += "using System;\n"
        head_code += "using System.Collections;\n"
        head_code += "using System.IO;\n\n"

        head_code += "namespace req\n"
        head_code += "{\n"

        cb_func = ""

        cb_code = "    /*this cb code is codegen by abelkhan for c#*/\n"
        cb_code += "    public class cb_" + module_name + " : common.imodule\n    {\n"

        cb_code_Constructor = "        public cb_" + module_name + "()\n        {\n"

        code = "    public class " + module_name + "\n"
        code += "    {\n"
        code += "        private client.client client_handle;\n"
        code += "        private cb_" + module_name + " cb_" + module_name + "_handle;\n\n"
        code += "        public " + module_name + "(client.client cli)\n"
        code += "        {\n"
        code += "            cb_" + module_name + "_handle = new cb_" + module_name + "();\n"
        code += "            client_handle = cli;\n"
        code += "            client_handle.modulemanager.add_module(\"" + module_name + "\", cb_" + module_name + "_handle);\n"
        code += "        }\n\n"
        code += "        public " + module_name + "_hubproxy get_hub(string hub_name)\n"
        code += "        {\n"
        code += "            return new " + module_name + "_hubproxy(hub_name, client_handle);\n"
        code += "        }\n\n"
        code += "    }\n\n"

        code += "    public class " + module_name + "_hubproxy\n"
        code += "    {\n"
        code += "        public string hub_name;\n"
        code += "        public client.client client_handle;\n\n"
        code += "        public " + module_name + "_hubproxy(string _hub_name, client.client _client_handle)\n"
        code += "        {\n"
        code += "            hub_name = _hub_name;\n"
        code += "            client_handle = _client_handle;\n"
        code += "        }\n\n"

        for i in funcs:
                func_name = i[0]

                if i[1] == "ntf":
                        code += "        void " + func_name + "("
                        count = 0
                        for item in i[2]:
                                code += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ")\n        {\n"
                        code += "            client_handle.call_hub(hub_name, \"" + module_name + "\", \"" + func_name + "\","
                        count = 0
                        for item in i[2]:
                                code += " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ");\n        }\n\n"
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        cb_code_Constructor += "            events[\"" + func_name + "_rsp\"] = " + func_name + "_rsp;\n"
                        cb_code_Constructor += "            events[\"" + func_name + "_err\"] = " + func_name + "_err;\n"

                        code += "        cb_" + func_name + " " + func_name + "("
                        count = 0
                        for item in i[2]:
                                code += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ")\n        {\n"
                        code += "            var uuid = System.Guid.NewGuid().ToString();\n"
                        code += "            client_handle.call_hub(hub_name, \"" + module_name + "\", \"" + func_name + "\", uuid,"
                        count = 0
                        for item in i[2]:
                                code += " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ");\n\n"
                        code += "            var cb_" + func_name + "_obj = new cb_" + func_name + "();\n"
                        code += "            cb_" + module_name + "_handle.map_" + func_name + ".Add(uuid, cb_" + func_name + "_obj);\n\n"
                        code += "            return cb_" + func_name + "_obj;\n        }\n\n"

                        cb_code += "        public Hashtable map_" + func_name + " = new Hashtable();\n\n"
                        cb_code += "        public void " + func_name + "_rsp(ArrayList _events)\n        {\n"
                        cb_code += "            string uuid = (string)_events[0];\n"
                        count = 0
                        for item in i[4]:
                                cb_code += "            var argv" + str(count) + " = (" + tools.gentypetocsharp(item) + ")_events[" + str(count) + "];\n"
                                count = count + 1
                        cb_code += "            var rsp = (cb_" + func_name + ")map_" + func_name + "[uuid];\n"
                        cb_code += "            rsp.cb("
                        count = 0
                        for item in i[4]:
                                cb_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_code += ", "
                        cb_code += ");\n"
                        cb_code += "        }\n\n"
                        cb_code += "        public void " + func_name + "_err(ArrayList _events)\n        {\n"
                        cb_code += "            string uuid = (string)_events[0];\n"
                        count = 0
                        for item in i[6]:
                                cb_code += "            var argv" + str(count) + " = (" + tools.gentypetocsharp(item) + ")_events[" + str(count) + "];\n"
                                count = count + 1
                        cb_code += "            var rsp = (cb_" + func_name + ")map_" + func_name + "[uuid];\n"
                        cb_code += "            rsp.err("
                        count = 0
                        for item in i[6]:
                                cb_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_code += ", "
                        cb_code += ");\n"
                        cb_code += "        }\n\n"

                        cb_func += "    public class cb_" + func_name + "\n    {\n"
                        cb_func += "        public delegate void " + func_name + "_handle_cb();\n"
                        cb_func += "        public event " + func_name + "_handle_cb on" + func_name + "_cb;\n"
                        cb_func += "        public void cb("
                        count = 0
                        for item in i[4]:
                                cb_func += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func += ", "
                        cb_func += ")\n        {\n"
                        cb_func += "            if (on" + func_name + "_cb != null)\n            {\n"
                        cb_func += "                on" + func_name + "_cb("
                        count = 0
                        for item in i[4]:
                                cb_func += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func += ", "
                        cb_func += ");\n            }\n"
                        cb_func += "        }\n\n"
                        cb_func += "        public delegate void " + func_name + "_handle_err();\n"
                        cb_func += "        public event " + func_name + "_handle_err on" + func_name + "_err;\n"
                        cb_func += "        public void err("
                        count = 0
                        for item in i[6]:
                                cb_func += tools.gentypetocsharp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func += ", "
                        cb_func += ")\n        {\n"
                        cb_func += "            if (on" + func_name + "_err != null)\n            {\n"
                        cb_func += "                on" + func_name + "_err("
                        count = 0
                        for item in i[6]:
                                cb_func += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func += ", "
                        cb_func += ");\n            }\n"
                        cb_func += "        }\n\n"
                        cb_func += "        void callBack(" + func_name + "_handle_cb cb, " + func_name + "_handle_err err)\n        {\n"
                        cb_func += "            on" + func_name + "_cb += cb;\n"
                        cb_func += "            on" + func_name + "_err += err;\n"
                        cb_func += "        }\n\n"
                        cb_func += "    }\n\n"
                else:
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must req or ntf"

        cb_code += cb_code_Constructor + "        }\n"
        cb_code += "    }\n\n"
        code += "    }\n"
        code += "}\n"

        return head_code + cb_func + cb_code + code
