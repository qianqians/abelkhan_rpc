# 2016-7-1
# build by qianqians
# gencaller

def gencaller(module_name, funcs):
        head_code = "/*this req file is codegen by abelkhan for js*/\n\n"

        cb_func = ""

        cb_code = "/*this cb code is codegen by abelkhan for js*/\n"
        cb_code += "function cb_" + module_name + "()\n{\n"

        code = "function " + module_name + "(_client_handle)\n{\n"
        code += "    this.client_handle = _client_handle;\n"
        code += "    this.cb_" + module_name + "_handle = new cb_" + module_name + "();\n"
        code += "    _client_handle.modules.add_module(\"" + module_name + "\", cb_" + module_name + "_handle);\n\n"

        for i in funcs:
                func_name = i[0]
                if i[1] == "ntf":
                        code += "    this." + func_name + " = function("
                        count = 0
                        for item in i[2]:
                                code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ")\n    {\n"
                        code += "        _client_handle.call_hub(\"" + module_name + "\", \"" + func_name + "\","
                        count = 0
                        for item in i[2]:
                                code += " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ");\n    }\n\n"
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        code += "    this." + func_name + " = function("
                        count = 0
                        for item in i[2]:
                                code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ")\n    {\n"
                        code += "        const uuidv1 = require('uuid/v1');\n"
                        code += "        var uuid = uuidv1();\n\n"
                        code += "        _client_handle.call_hub(\"" + module_name + "\", \"" + func_name + "\", uuid,"
                        count = 0
                        for item in i[2]:
                                code += " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += ");\n\n"
                        code += "        var cb_" + func_name + "_obj = new cb_" + func_name + "();\n"
                        code += "        this.cb_" + module_name + "_handle[uuid] = cb_" + func_name + "_obj;\n\n"
                        code += "        return cb_" + func_name + "_obj;\n    }\n\n"

                        cb_code += "    this.map_" + func_name + " = {};\n"
                        cb_code += "    this." + func_name + "_rsp = function("
                        cb_code += "uuid, "
                        count = 0
                        for item in i[4]:
                                cb_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_code += ", "
                        cb_code += ")\n    {\n"
                        cb_code += "        var rsp = map_" + func_name + "[uuid];\n"
                        cb_code += "        rsp.cb("
                        count = 0
                        for item in i[4]:
                                cb_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_code += ", "
                        cb_code += ");\n"
                        cb_code += "    }\n\n"

                        cb_code += "    this." + func_name + "_err = function("
                        cb_code += "uuid, "
                        count = 0
                        for item in i[6]:
                                cb_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_code += ", "
                        cb_code += ")\n    {\n"
                        cb_code += "        var rsp = map_" + func_name + "[uuid];\n"
                        cb_code += "        rsp.err("
                        count = 0
                        for item in i[6]:
                                cb_code += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_code += ", "
                        cb_code += ");\n"
                        cb_code += "    }\n\n"
                        
                        cb_func += "function cb_" + func_name + "()\n{\n"
                        cb_func += "    this.event_" + func_name + "_handle_cb = null;\n"
                        cb_func += "    this.cb = function(" 
                        count = 0
                        for item in i[4]:
                                cb_func += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func += ", "
                        cb_func += ")\n    {\n"
                        cb_func += "        if (this.event_" + func_name + "_handle_cb !== null)\n        {\n"
                        cb_func += "            this.event_" + func_name + "_handle_cb("
                        count = 0
                        for item in i[4]:
                                cb_func += "argv" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func += ", "
                        cb_func += ");\n        }\n"
                        cb_func += "    }\n\n"

                        cb_func += "    this.event_" + func_name + "_handle_err = null;\n"
                        cb_func += "    this.err = function(" 
                        count = 0
                        for item in i[6]:
                                cb_func += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func += ", "
                        cb_func += ")\n    {\n"
                        cb_func += "        if (this.event_" + func_name + "_handle_err != null)\n        {\n"
                        cb_func += "            this.event_" + func_name + "_handle_err("
                        count = 0
                        for item in i[6]:
                                cb_func += "argv" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func += ", "
                        cb_func += ");\n        }\n"
                        cb_func += "    }\n\n"

                        cb_func += "    this.callBack = function(cb, err)\n    {\n"
                        cb_func += "        this.event_" + func_name + "_handle_cb += cb;\n"
                        cb_func += "        this.event_" + func_name + "_handle_err += err;\n"
                        cb_func += "    }\n"
                        cb_func += "}\n\n"
                else:
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must req or ntf"

        cb_code += "}\n\n"
        code += "}\n"

        return head_code + cb_func + cb_code + code
