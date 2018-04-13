# 2018-3-16
# build by qianqians
# genmodule

def gencaller(module_name, funcs):
        code = "/*this ntf file is codegen by ablekhan for js*/\n\n"

        code += "function " + module_name + "(hub_ptr){\n"
        code += "    this.get_client = function(uuid){\n"
        code += "        return new " + module_name + "_cliproxy(uuid, hub_ptr);\n" 
        code += "    }\n"
        code += "    this.get_multicast = function(uuids){\n"
        code += "        return new " + module_name + "_cliproxy_multi(uuids, hub_ptr);\n" 
        code += "    }\n"
        code += "    this.get_broadcast = function(){\n"
        code += "        return new " + module_name + "_broadcast(hub_ptr);\n" 
        code += "    }\n"
        code += "}\n\n"

        cp_code = "function " + module_name + "_cliproxy(uuid, hub_ptr){\n"
        cp_code += "     this.uuid = uuid;\n\n"

        cm_code = "function " + module_name + "_cliproxy_multi(uuids, hub_ptr){\n"
        cm_code += "    this.uuids = uuids;\n"

        cb_code = "function " + module_name + "_broadcast(hub_ptr){\n"
        
        for i in funcs:
                func_name = i[0]

                if i[1] != "ntf" and i[1] != "multicast" and i[1] != "broadcast":
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must ntf or broadcast"
                
                argvs = ""
                count = 0
                for item in i[2]:
                        argvs += "argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                argvs += ", "

                tmp_code = "    this." + func_name + " = function("
                tmp_code += argvs
                tmp_code += "){\n"

                if i[1] == "ntf":
                        cp_code += tmp_code
                        cp_code += "        hub_ptr.gates.call_client(uuid, \"" + module_name + "\", \"" + func_name + "\", " + argvs + ");\n"  
                        cp_code += "    }\n"
                elif i[1] == "multicast":
                        cm_code += tmp_code
                        cm_code += "        hub_ptr.gates.call_group_client(uuids, \"" + module_name + "\", \"" + func_name + "\", " + argvs + ");\n"
                        cm_code += "    }\n"
                elif i[1] == "broadcast":
                        cb_code += tmp_code
                        cb_code += "        hub_ptr.gates.call_global_client(\"" + module_name + "\", \"" + func_name + "\", " + argvs + ");\n"
                        cb_code += "    }\n"
        
        cp_code += "}\n\n"
        cm_code += "}\n\n"
        cb_code += "}\n\n"

        return code + cp_code + cm_code + cb_code
