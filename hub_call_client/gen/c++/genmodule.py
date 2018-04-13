# 2016-7-1
# build by qianqians
# genmodule

import tools

def genmodule(module_name, funcs):
        head_code = "/*this rsp file is codegen by abelkhan for c++*/\n\n"
        head_code += "#include <string>\n"
        head_code += "#include <functional>\n"
        head_code += "#include <memory>\n\n"
        
        head_code += "#include <boost/any.hpp>\n\n"

        head_code += "#include <module.h>\n\n"

        head_code += "#include <hub.h>\n\n"

        head_code += "namespace rsp\n"
        head_code += "{\n"

        code = "    public class " + module_name + " : public common::imodule {\n    {\n"
        code += "    public:\n        string module_name;\n"
        code += "        hub::hub hub_handle;\n\n"
        code += "    public:\n        " + module_name + "(hub::hub _hub)\n        {\n"
        code += "            module_name = \"" + module_name + "\";\n"
        code += "            hub_handle = _hub;\n\n"
        code += "            hub::hub::modules->add_module(\"" + module_name + "\", this);\n"
        code += "        }\n\n    public:\n"

        for i in funcs:
                func_name = i[0]

                if i[1] != "ntf" and i[1] != "broadcast":
                        raise "func:" + func_name + " wrong rpc type:" + i[1] + ", must ntf or broadcast"

                code += "        boost::signal2::signal<void("
                count = 0
                for item in i[2]:
                        code += tools.gentypetocpp(item) + " argv" + str(count)
                        count = count + 1
                        if count < len(i[2]):
                                code += ", "
                code += ");  sig" + func_name + ";\n"
                code += "        void " + func_name + "(std::shared_ptr<std::vector<boost::any> > argvs)\n        {\n"
                count = 0
                for item in i[2]:
                        code += "            auto argv" + str(count) + " = boost::any_cast<" + tools.gentypetocpp(item) + " >(argvs[" + str(count) + "]);\n"
                        count = count + 1
                code += "\n            sig" + func_name + "("
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
