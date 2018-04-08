/*this req file is codegen by abelkhan codegen for c++*/

#ifndef _name_req_h
#define _name_req_h

#include <string>
#include <boost/any.hpp>
#include <boost/uuid/uuid.hpp>
#include <boost/uuid/uuid_generators.hpp>
#include <boost/uuid/uuid_io.hpp>
#include <boost/lexical_cast.hpp>
#include <memory>

#include <module.h>

class cb_func_test{
public:
    boost::signal2::signal<void(int64_t) sigfunc_testcb;
    void cb(int64_t argvs0){
        sigfunc_testcb(argvs0);
    }

    boost::signal2::signal<void(int64_t) sigfunc_testerr;
    void err(int64_t argvs0){
        sigfunc_testerr(argvs0);
    }

}
/*req cb code, codegen by abelkhan codegen*/
class cb_name : public common::imodule {
public:
    cb_name(){
        reg_cb("func_test_rsp", std::bind(&cb_name::func_test_rsp), this, std::placeholders::_1);
    }
    std::map<std::string, std::shared_ptr<cb_func_test> > map_func_test;
    void func_test_rsp(std::shared_ptr<std::vector<boost::any> > argvs){
        auto cb_uuid = boost::any_cast<std::string>(argvs[0];
        auto argv1 = boost::any_cast<int64_t>(argvs[1]);
        std::shared_ptr<cb_func_test> func_cb = map_func_test[cb_uuid];
        func_cb->cb(argv1);
    }
    void func_test_err(std::shared_ptr<std::vector<boost::any> > argvs){
        auto cb_uuid = boost::any_cast<std::string>(argvs[0];
        auto argv1 = boost::any_cast<int64_t>(argvs[1]);
        std::shared_ptr<cb_func_test> func_cb = map_func_test[cb_uuid];
        func_cb->err(argv1);
    }
};

namespace req
{
class name {
private:
    std::shared_ptr<client::client> client_handle_ptr;
    std::shared_ptr<cb_name> cb_name_handle;

public:
    name(std::shared_ptr<client::client> _client) {
        client_handle_ptr = _client;
        cb_name_handle = std::make_shared<cb_name>();
        client_handle_ptr->modules.add_module("name", cb_name_handle);
    }

    ~name(){
    }

    std::shared_ptr<cb_func_test> func_test(std::string hub, std::string func, int64_t argv0, std::shared_ptr<std::vector<boost::any> > argv1, bool argv2){
        boost::uuids::random_generator g;
        auto uuid = boost::lexical_cast<std::string>(g());
        auto v = std::make_shared<std::vector<boost::any> >();
        v->push_back(uuid);
        v->push_back(argv0);
        v->push_back(argv1);
        v->push_back(argv2);
        client_handle_ptr->call_hub(hub, "name", func, v);
        auto cb_func_obj = std::make_shared<cb_func_test>();
        cb_name_handle->map_func_test.insert(std::make_pair(uuid, cb_func_obj));
        return cb_func_obj;
    }

};

}

#endif
