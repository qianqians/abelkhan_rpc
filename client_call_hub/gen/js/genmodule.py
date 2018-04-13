# 2016-7-1
# build by qianqians
# genmodule

def genmodule(module_name, funcs):
        head_code = "/*this rsp file is codegen by abelkhan for js*/\n\n"

        rsp_code = ""

        code = "function " + module_name + "(_hub)\n{\n"
        code += "    var event_cb = require(\"event_cb\");\n"
        code += "    event_cb.call(this);\n\n"
        code += "    this.module_name = \"" + module_name + "\";\n"
        code += "    this.hub_handle = _hub;\n"
        code += "    _hub.modules.add_module(\"" + module_name + "\", this);\n\n"

        for i in funcs:
                func_name = i[0]

                code += "    this." + func_name + " = function("
                count = 0
                for item in i[2]:
                        code += "argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += ")\n    {\n"

                if i[1] == "ntf":
                        pass
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        code += "        _hub.modules.rsp = new rsp_" + func_name + "(_hub);\n"
                        
                        rsp_code += "function rsp_" + func_name + "(_hub)\n{\n"
                        rsp_code += "    this.hub_handle = _hub;\n"
                        
                        rsp_code += "    this.call("
                        count = 0
                        for item in i[4]:
                                rsp_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        rsp_code += ", "
                        rsp_code += ")\n    {\n"
                        rsp_code += "        _hub.gates.call_client(_hub.gates.current_client_uuid, \"" + module_name + "\", \"" + func_name + "_rsp\", "
                        count = 0
                        for item in i[4]:
                                rsp_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        rsp_code += ", "
                        rsp_code += ");\n"
                        rsp_code += "    }\n"
                        
                        rsp_code += "    this.err("
                        count = 0
                        for item in i[6]:
                                rsp_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        rsp_code += ", "
                        rsp_code += ")\n    {\n"
                        rsp_code += "        _hub.gates.call_client(_hub.gates.current_client_uuid, \"" + module_name + "\", \"" + func_name + "_rsp\", "
                        count = 0
                        for item in i[6]:
                                rsp_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        rsp_code += ", "
                        rsp_code += ");\n"
                        rsp_code += "    }\n"
                        rsp_code += "}\n\n"
                else:
                        raise "func:%s wrong rpc type:%s must req or ntf" % (func_name, i[1])

                code += "        this.call_event(\"" + func_name + "\", ["
                count = 0
                for item in i[2]:
                        code += "argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += "]);\n"
                
                if i[1] == "ntf":
                        pass
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        code += "        _hub.modules.rsp = null;\n"
                else:
                        raise "func:%s wrong rpc type:%s must req or ntf" % (func_name, i[1])

                code += "    }\n\n"

        code += "}\n"

        return head_code + rsp_code + code
