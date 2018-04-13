/*this rsp file is codegen by abelkhan for c++*/

#include <string>
#include <functional>
#include <memory>

#include <boost/any.hpp>

#include <module.h>

#include <hub.h>

namespace rsp
{
    public class name : public common::imodule {
    {
    public:
        string module_name;
        hub::hub hub_handle;

    public:
        name(hub::hub _hub)
        {
            module_name = "name";
            hub_handle = _hub;

            hub::hub::modules->add_module("name", this);
        }

    public:
        boost::signal2::signal<void(int64_t argv0, int64_t argv1, bool argv2, double argv3);  sigfunc_test;
        void func_test(std::shared_ptr<std::vector<boost::any> > argvs)
        {
            auto argv0 = boost::any_cast<int64_t >(argvs[0]);
            auto argv1 = boost::any_cast<int64_t >(argvs[1]);
            auto argv2 = boost::any_cast<bool >(argvs[2]);
            auto argv3 = boost::any_cast<double >(argvs[3]);

            sigfunc_test(argv0, argv1, argv2, argv3);
        }

        boost::signal2::signal<void(std::string argv0, std::shared_ptr<std::vector<boost::any> > argv1, std::shared_ptr<std::unordered_map<std::string, boost::any> > argv2);  sigfunc_test1;
        void func_test1(std::shared_ptr<std::vector<boost::any> > argvs)
        {
            auto argv0 = boost::any_cast<std::string >(argvs[0]);
            auto argv1 = boost::any_cast<std::shared_ptr<std::vector<boost::any> > >(argvs[1]);
            auto argv2 = boost::any_cast<std::shared_ptr<std::unordered_map<std::string, boost::any> > >(argvs[2]);

            sigfunc_test1(argv0, argv1, argv2);
        }

    }
}
