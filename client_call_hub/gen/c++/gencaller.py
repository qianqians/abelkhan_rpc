# 2018-4-8
# build by qianqians
# gencaller

import tools

def gencaller(module_name, funcs):
        head_code = "/*this req file is codegen by abelkhan codegen for c++*/\n\n"
        head_code += "#ifndef _" + module_name + "_req_h\n"
        head_code += "#define _" + module_name + "_req_h\n\n"
        
        head_code += "#include <string>\n"
        head_code += "#include <boost/any.hpp>\n"
        head_code += "#include <boost/uuid/uuid.hpp>\n"
        head_code += "#include <boost/uuid/uuid_generators.hpp>\n"
        head_code += "#include <boost/uuid/uuid_io.hpp>\n"
        head_code += "#include <boost/lexical_cast.hpp>\n"
        head_code += "#include <memory>\n\n"

        head_code += "#include <module.h>\n\n"
        
        cb_code_head = "/*req cb code, codegen by abelkhan codegen*/\n"
        cb_code_head += "class cb_" + module_name + " : public common::imodule {\n"
        cb_code_head += "public:\n"
        cb_code_head += "    cb_" + module_name + "(){\n"

        cb_code = ""
        cb_func_code = ""
        
        code =  "namespace req\n"
        code += "{\n"
        code += "class " + module_name + " {\n"
        code += "private:\n"
        code += "    std::shared_ptr<client::client> client_handle_ptr;\n"
        code += "    std::shared_ptr<cb_" + module_name + "> cb_" + module_name + "_handle;\n\n"
        code += "public:\n"
        code += "    " + module_name + "(std::shared_ptr<client::client> _client) {\n"
        code += "        client_handle_ptr = _client;\n"
        code += "        cb_" + module_name + "_handle = std::make_shared<cb_" + module_name + ">();\n"
        code += "        client_handle_ptr->modules.add_module(\"" + module_name + "\", cb_" + module_name + "_handle);\n"
        code += "    }\n\n"

        code += "    ~" + module_name + "(){\n"
        code += "    }\n\n"

        for i in funcs:
                func_name = i[0]
                if i[1] == "ntf":
                        code += "    void " + func_name + "(std::string hub, std::string func, "
                        count = 0
                        for item in i[2]:
                                code += tools.gentypetocpp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ","
                        code += "){\n"
                        code += "        auto v = std::make_shared<std::vector<boost::any> >();\n"
                        for count in range(len(i[2])):
                            code += "    v->push_back(argv" + str(count) + ");\n"
                        code += "        client_handle_ptr->call_hub(hub, \"" + module_name + "\", func, v);\n"
                        code += "    }\n\n"
                elif i[1] == "req" and i[3] == "rsp" and i[5] == "err":
                        code += "    std::shared_ptr<cb_" + func_name + "> " + func_name + "(std::string hub, std::string func, "
                        count = 0
                        for item in i[2]:
                                code += tools.gentypetocpp(item) + " argv" + str(count)
                                count = count + 1
                                if count < len(i[2]):
                                        code += ", "
                        code += "){\n"
                        code += "        boost::uuids::random_generator g;\n"
                        code += "        auto uuid = boost::lexical_cast<std::string>(g());\n"
                        code += "        auto v = std::make_shared<std::vector<boost::any> >();\n"
                        code += "        v->push_back(uuid);\n"
                        for count in range(len(i[2])):
                            code += "        v->push_back(argv" + str(count) + ");\n"
                        code += "        client_handle_ptr->call_hub(hub, \"" + module_name + "\", func, v);\n"
                        code += "        auto cb_func_obj = std::make_shared<cb_" + func_name + ">();\n"
                        code += "        cb_" + module_name + "_handle->map_" + func_name + ".insert(std::make_pair(uuid, cb_func_obj));\n"
                        code += "        return cb_func_obj;\n"
                        code += "    }\n\n"
                        
                        cb_func_code += "class cb_" + func_name + "{\n"
                        cb_func_code += "public:\n"
                        cb_func_code += "    boost::signal2::signal<void("
                        count = 0
                        for item in i[4]:
                                cb_func_code += tools.gentypetocpp(item)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func_code += ", "
                        cb_func_code += ") sig" + func_name + "cb;\n"
                        cb_func_code += "    void cb("
                        count = 0
                        for item in i[4]:
                                cb_func_code += tools.gentypetocpp(item) + " argvs" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func_code += ", "
                        cb_func_code += "){\n"
                        cb_func_code += "        sig" + func_name + "cb("
                        count = 0
                        for item in i[4]:
                                cb_func_code += "argvs" + str(count)
                                count = count + 1
                                if count < len(i[4]):
                                        cb_func_code += ", "
                        cb_func_code += ");\n"
                        cb_func_code += "    }\n\n"
                        cb_func_code += "    boost::signal2::signal<void("
                        count = 0
                        for item in i[6]:
                                cb_func_code += tools.gentypetocpp(item)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func_code += ", "
                        cb_func_code += ") sig" + func_name + "err;\n"
                        cb_func_code += "    void err("
                        count = 0
                        for item in i[6]:
                                cb_func_code += tools.gentypetocpp(item) + " argvs" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func_code += ", "
                        cb_func_code += "){\n"
                        cb_func_code += "        sig" + func_name + "err("
                        count = 0
                        for item in i[6]:
                                cb_func_code += "argvs" + str(count)
                                count = count + 1
                                if count < len(i[6]):
                                        cb_func_code += ", "
                        cb_func_code += ");\n"
                        cb_func_code += "    }\n\n"
                        cb_func_code += "}\n"

                        cb_code_head += "        reg_cb(\"" + func_name + "_rsp\", std::bind(&cb_" + module_name + "::" + func_name + "_rsp), this, std::placeholders::_1);\n"

                        cb_code += "    std::map<std::string, std::shared_ptr<cb_" + func_name + "> > map_" + func_name + ";\n"
                        cb_code += "    void " + func_name + "_rsp(std::shared_ptr<std::vector<boost::any> > argvs){\n"
                        cb_code += "        auto cb_uuid = boost::any_cast<std::string>(argvs[0];\n"
                        count = 1
                        for item in i[4]:
                                cb_code += "        auto argv" + str(count) + " = boost::any_cast<" + tools.gentypetocpp(item) + ">(argvs[" + str(count) + "]);\n"
                                count = count + 1
                        cb_code += "        std::shared_ptr<cb_" + func_name + "> func_cb = map_" + func_name + "[cb_uuid];\n"
                        cb_code += "        func_cb->cb("
                        count = 1
                        for item in i[4]:
                                cb_code += "argv" + str(count)
                                if count < len(i[4]):
                                        cb_code += ", "
                                count = count + 1
                        cb_code += ");\n"
                        cb_code += "    }\n"
                        cb_code += "    void " + func_name + "_err(std::shared_ptr<std::vector<boost::any> > argvs){\n"
                        cb_code += "        auto cb_uuid = boost::any_cast<std::string>(argvs[0];\n"
                        count = 1
                        for item in i[6]:
                                cb_code += "        auto argv" + str(count) + " = boost::any_cast<" + tools.gentypetocpp(item) + ">(argvs[" + str(count) + "]);\n"
                                count = count + 1
                        cb_code += "        std::shared_ptr<cb_" + func_name + "> func_cb = map_" + func_name + "[cb_uuid];\n"
                        cb_code += "        func_cb->err("
                        count = 1
                        for item in i[6]:
                                cb_code += "argv" + str(count)
                                if count < len(i[6]):
                                        cb_code += ", "
                                count = count + 1
                        cb_code += ");\n"
                        cb_code += "    }\n"
                else:
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must req or ntf"

        cb_code_head += "    }\n"
        code += "};\n\n"
        cb_code += "};\n\n"
        code += "}\n\n"
        code += "#endif\n"

        return head_code + cb_func_code + cb_code_head + cb_code + code
