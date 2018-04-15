# 2018-3-16
# build by qianqians
# genmodule

def genmodule(module_name, funcs):
        code = "/*this imp file is codegen by abelkhan for js*/\n"

        code += "function " + module_name + "(_client){\n"
        code += "    event_cb.call(this);\n\n"
        code += "    this.client_handle = _client;\n"
        code += "    _client.modules.add_module(\"" + module_name + "\", this);\n\n"

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

                code += "        this.call_event(\"" + func_name + "\", ["
                count = 0
                for item in i[2]:
                        code += "argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += "]);\n"

                code += "    }\n\n"

        code += "}\n"

        return code
